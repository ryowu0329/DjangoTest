# encoding: utf-8
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.core.paginator import Paginator 
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from xhtml2pdf.default import DEFAULT_FONT
from django_pdfkit import PDFView
from users.models import *
from .models import *
from .forms import *
from .resources import *
from django.db import transaction


def export_yfcase(reauest):
  yfcase_resource = YfcaseResource()
  yfcase = yfcase_resource.export()
  response = HttpResponse(yfcase.xlsx,content_type='application/vnd.ms-excel')
  response['Content-Disposition'] = 'attachment; filename="member.xlsx"'
  return response



# @method_decorator(login_required,name='dispatch')   
# class YfcaseListView(ListView):
#   model=Yfcase
#   template_name="home.html"

# 所有(List)
@login_required
def yfcase_list_all(request):
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404
  queryset_list = Yfcase.objects.all()
  query = request.GET.get('q')
  if query:
    queryset_list = queryset_list.filter(
      Q(yfcaseCaseNumber__icontains=query)|
      Q(yfcaseCityWithTownship__icontains=query)|
      Q(yfcaseStreet__icontains=query)|
      Q(yfcaseNumber__icontains=query)|
      Q(finaldecisions__finalDecision__icontains=query)|
      Q(finaldecisions__regionalHead__icontains=query)|
      Q(user__userFullName__icontains=query)
    ).distinct()
  paginator = Paginator(queryset_list, 10) 

  page = request.GET.get('page')
  queryset = paginator.get_page(page)

  context={
    "object_list" : queryset,
    "title": "List"
    }
  return render(request, "home.html", context)
  
# 個人(List)
@login_required
def yfcase_list(request):
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404
  # 登入者姓名
  request_userid=request.user.id
  queryset_list = Yfcase.objects.filter(user_id=request_userid)
  query = request.GET.get('q')
  if query:
    queryset_list = queryset_list.filter(
      Q(yfcaseCaseNumber__icontains=query)|
      Q(yfcaseCityWithTownship__icontains=query)|
      Q(yfcaseStreet__icontains=query)|
      Q(yfcaseNumber__icontains=query)|
      Q(finaldecisions__finalDecision__icontains=query)|
      Q(finaldecisions__regionalHead__icontains=query)|
      Q(user__userFullName__icontains=query)
    ).distinct()
  paginator = Paginator(queryset_list, 10) 

  page = request.GET.get('page')
  queryset = paginator.get_page(page)

  context={
    "object_list" : queryset,
    "title": "List"
    }
  return render(request, "home.html", context)


@method_decorator(login_required,name='dispatch')
class YfcaseDetailView(DetailView):
  model=Yfcase
  form_class = YfcaseForm
  template_name="yfcase/yfcase_detail.html"
  success_url = reverse_lazy('yfcase:yfcase_detail')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = '建立項目'
    return context

class YfcaseCreateView(CreateView):
  model=Yfcase
  form_class = YfcaseForm
  template_name="yfcase/yfcase_create.html"
  success_url = reverse_lazy('yfcase:home')

  def get_context_data(self, **kwargs):
    context = super(YfcaseCreateView,self).get_context_data(**kwargs)
    context["author_id"]=self.request.user.id
    context['value'] = '建立'
    context['title'] = '新增基本資料'
    return context

class YfcaseUpdateView(UpdateView):
  model=Yfcase
  form_class = YfcaseForm
  template_name='yfcase/yfcase_update.html'
    
  def get_success_url(self, **kwargs):
    return reverse_lazy("yfcase:yfcase_detail", args=(self.object.id,))

  def form_valid(self, form):
    if form.cleaned_data['yfcaseCaseNumber'] is None:
        form.add_error('yfcaseCaseNumber', 'Incident with this email already exist')
        return self.form_invalid(form)
    return super(YfcaseUpdateView, self).form_valid(form)
    
  def get_context_data(self, **kwargs):
    context = super(YfcaseUpdateView,self).get_context_data(**kwargs)
    context["author_id"]=self.request.user.id
    context['value'] = '更新'
    context['title'] = '更新基本資料'
    return context

class YfcaseDeleteView(DeleteView):
  model=Yfcase
  template_name="yfcase/yfcase_delete.html"
  success_url=reverse_lazy('yfcase:home')

# ==========================  Land  =========================
def land_create(request,yfcase_id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404
  form = LandForm(request.POST or None)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    return redirect("yfcase:yfcase_detail", yfcase_id)
  context = {
    "form" : form, 
    "instance_yfcase": instance_yfcase,
    "title": "新增地號",
  }
  return render(request, "land/land_form.html",context)

def land_update(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(Land,id=id)
  form=LandForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Update")
    # 這裡的instance_yfcase.id指的是父類的id(Yfcase)
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context={
    "instance" : instance,
    "instance_yfcase" : instance_yfcase,
    "form" : form,
    "title": "更新地號",
  }
  return render(request, "land/land_form.html",context)

def land_delete(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(Land, id=id)
  if request.method == "POST":
    instance.delete()
    # messages.success(request, 'Data Deleted.')
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context = {
    "instance": instance,
    "instance_yfcase": instance_yfcase,
    "title": "刪除建號"
  }
  return render(request, "land/land_delete.html", context)

# ==========================  Build  =========================
def build_create(request,yfcase_id=None):
  # 要配合url回傳的yfcase_id，來取得超類的資料
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404
  form = BuildForm(request.POST or None)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Created")
    # 把父類的yfcase_id(不可寫成instance.id，回傳到子類的id)回傳給yfcase_detail
    return redirect("yfcase:yfcase_detail", yfcase_id)
  context = {
    "form" : form, 
    "instance_yfcase": instance_yfcase,
    "title": "新增建號",
  }
  return render(request, "build/build_form.html",context)

def build_update(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(Build,id=id)
  form=BuildForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Update")
    # 這裡的instance_yfcase.id指的是父類的id(Yfcase)
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context={
    "instance" : instance,
    "instance_yfcase" : instance_yfcase,
    "form" : form,
    "title": "更新建號",
  }
  return render(request, "build/build_form.html",context)

def build_delete(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(Build, id=id)
  if request.method == "POST":
    instance.delete()
    # messages.success(request, 'Data Deleted.')
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context = {
    "instance": instance,
    "instance_yfcase": instance_yfcase,
    "title": "刪除建號"
  }
  return render(request, "build/build_delete.html", context)

# ==========================  Auction  =========================
def auction_create(request,yfcase_id=None):
  # 要配合url回傳的yfcase_id，來取得超類的資料
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404
  form = AuctionForm(request.POST or None)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Created")
    # 把父類的yfcase_id(不可寫成instance.id，回傳到子類的id)回傳給yfcase_detail
    return redirect("yfcase:yfcase_detail", yfcase_id)
  context = {
    "form" : form, 
    "instance_yfcase": instance_yfcase,
    "title": "新增拍賣資訊",
  }
  return render(request, "auction/auction_form.html",context)

def auction_update(request,yfcase_id=None,id=id):
  # 要配合url回傳的yfcase_id，來取得超類的資料
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(Auction,id=id)
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404
  form = AuctionForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Created")
    # 把父類的yfcase_id(不可寫成instance.id，回傳到子類的id)回傳給yfcase_detail
    return redirect("yfcase:yfcase_detail", yfcase_id)
  context = {
    "instance" : instance,
    "form" : form, 
    "instance_yfcase": instance_yfcase,
    "title": "更新拍賣資訊",
  }
  return render(request, "auction/auction_form.html",context)

# ==========================  Survey  =========================
def survey_create(request,yfcase_id=None):
  # 要配合url回傳的yfcase_id，來取得超類的資料
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404
  form = SurveyForm(request.POST or None)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Created")
    # 把父類的yfcase_id(不可寫成instance.id，回傳到子類的id)回傳給yfcase_detail
    return redirect("yfcase:yfcase_detail", yfcase_id)
  context = {
    "form" : form, 
    "instance_yfcase": instance_yfcase,
    "title": "新增拍賣資訊",
  }
  return render(request, "survey/survey_form.html",context)

def survey_update(request,yfcase_id=None,id=id):
  # 要配合url回傳的yfcase_id，來取得超類的資料
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(Survey,id=id)
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404
  form = SurveyForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Created")
    # 把父類的yfcase_id(不可寫成instance.id，回傳到子類的id)回傳給yfcase_detail
    return redirect("yfcase:yfcase_detail", yfcase_id)
  context = {
    "instance" : instance,
    "form" : form, 
    "instance_yfcase": instance_yfcase,
    "title": "更新拍賣資訊",
  }
  return render(request, "survey/survey_form.html",context)
  
# ==========================  ObjectBuild  =========================
def objectbuild_create(request,yfcase_id=None):
  # 要配合url回傳的yfcase_id，來取得超類的資料
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404
  form = ObjectBuildForm(request.POST or None)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Created")
    # 把父類的yfcase_id(不可寫成instance.id，回傳到子類的id)回傳給yfcase_detail
    return redirect("yfcase:yfcase_detail", yfcase_id)
  context = {
    "form" : form, 
    "instance_yfcase": instance_yfcase,
    "title": "新增參考物件",
  }
  return render(request, "objectbuild/objectbuild_form.html",context)

def objectbuild_update(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(ObjectBuild,id=id)
  form=ObjectBuildForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Update")
    # 這裡的instance_yfcase.id指的是父類的id(Yfcase)
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context={
    "instance" : instance,
    "instance_yfcase" : instance_yfcase,
    "form" : form,
    "title": "更新參考物件",
  }
  return render(request, "objectbuild/objectbuild_form.html",context)

def objectbuild_delete(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(ObjectBuild, id=id)
  if request.method == "POST":
    instance.delete()
    # messages.success(request, 'Data Deleted.')
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context = {
    "instance": instance,
    "instance_yfcase": instance_yfcase,
    "title": "刪除參考物件"
  }
  return render(request, "objectbuild/objectbuild_delete.html", context)

# ==========================  ScoreA  =========================
def score_a_adj(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(ObjectBuild,id=id)
  form=ScoreAForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Update")
    # 這裡的instance_yfcase.id指的是父類的id(Yfcase)
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context={
    "instance" : instance,
    "instance_yfcase" : instance_yfcase,
    "form" : form,
    "title": "調整勘查員A評分",
  }
  return render(request, "score/score_a_form.html",context)

def score_a_clean(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(ObjectBuild,id=id)
  form=ScoreAForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Update")
    # 這裡的instance_yfcase.id指的是父類的id(Yfcase)
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context={
    "instance" : instance,
    "instance_yfcase" : instance_yfcase,
    "form" : form,
    "Title": "清除勘查員A評分",
  }
  return render(request, "score/score_a_delete.html",context)

# ==========================  ScoreB  =========================
def score_b_adj(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(ObjectBuild,id=id)
  form=ScoreBForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Update")
    # 這裡的instance_yfcase.id指的是父類的id(Yfcase)
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context={
    "instance" : instance,
    "instance_yfcase" : instance_yfcase,
    "form" : form,
    "title": "調整勘查員B評分",
  }
  return render(request, "score/score_b_form.html",context)

def score_b_clean(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(ObjectBuild,id=id)
  form=ScoreBForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Update")
    # 這裡的instance_yfcase.id指的是父類的id(Yfcase)
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context={
    "instance" : instance,
    "instance_yfcase" : instance_yfcase,
    "form" : form,
    "Title": "清除勘查員B評分",
  }
  return render(request, "score/score_b_delete.html",context)

# ==========================  ScoreC  =========================
def score_c_adj(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(ObjectBuild,id=id)
  form=ScoreCForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Update")
    # 這裡的instance_yfcase.id指的是父類的id(Yfcase)
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context={
    "instance" : instance,
    "instance_yfcase" : instance_yfcase,
    "form" : form,
    "title": "調整勘查員C評分",
  }
  return render(request, "score/score_c_form.html",context)

def score_c_clean(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(ObjectBuild,id=id)
  form=ScoreCForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Update")
    # 這裡的instance_yfcase.id指的是父類的id(Yfcase)
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context={
    "instance" : instance,
    "instance_yfcase" : instance_yfcase,
    "form" : form,
    "Title": "清除勘查員C評分",
  }
  return render(request, "score/score_c_delete.html",context)

# ==========================  FinalDecision(regionalHead)  =========================
def finaldecision_create(request,yfcase_id=None):
  # 要配合url回傳的yfcase_id，來取得超類的資料
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404
  form = FinalDecisionForm(request.POST or None)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Created")
    # 把父類的yfcase_id(不可寫成instance.id，回傳到子類的id)回傳給yfcase_detail
    return redirect("yfcase:yfcase_detail", yfcase_id)
  context = {
    "form" : form, 
    "instance_yfcase": instance_yfcase,
    "title": "新增最終判定",
  }
  return render(request, "finaldecision/finaldecision_form.html",context)


def finaldecision_update(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(FinalDecision,id=id)
  form=FinalDecisionForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Update")
    # 這裡的instance_yfcase.id指的是父類的id(Yfcase)
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context={
    "instance" : instance,
    "instance_yfcase" : instance_yfcase,
    "form" : form,
    "title": "變更最終判定",
  }
  return render(request, "finaldecision/finaldecision_form.html",context)

def finaldecision_delete(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(FinalDecision, id=id)
  if request.method == "POST":
    instance.delete()
    # messages.success(request, 'Data Deleted.')
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context = {
    "instance": instance,
    "instance_yfcase": instance_yfcase,
    "title": "刪除最終判定"
  }
  return render(request, "finaldecision/finaldecision_delete.html", context)

# ==========================  SubSigntrueA  =========================
def subsignture_a_update(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(FinalDecision,id=id)
  form=SubSigntrueAForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Update")
    # 這裡的instance_yfcase.id指的是父類的id(Yfcase)
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context={
    "instance" : instance,
    "instance_yfcase" : instance_yfcase,
    "form" : form,
    "title": "新增/變更副署人員1的簽核",
  }
  return render(request, "finaldecision/subsignture_a_form.html",context)

def subsignture_a_delete(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(FinalDecision,id=id)
  form=SubSigntrueAForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Update")
    # 這裡的instance_yfcase.id指的是父類的id(Yfcase)
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context={
    "instance" : instance,
    "instance_yfcase" : instance_yfcase,
    "form" : form,
    "Title": "刪除副署人員1的簽核",
  }
  return render(request, "finaldecision/subsignture_a_delete.html",context)

# ==========================  SubSigntrueB  =========================
def subsignture_b_update(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(FinalDecision,id=id)
  form=SubSigntrueBForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Update")
    # 這裡的instance_yfcase.id指的是父類的id(Yfcase)
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context={
    "instance" : instance,
    "instance_yfcase" : instance_yfcase,
    "form" : form,
    "title": "新增/變更副署人員2的簽核",
  }
  return render(request, "finaldecision/subsignture_b_form.html",context)

def subsignture_b_delete(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(FinalDecision,id=id)
  form=SubSigntrueBForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Update")
    # 這裡的instance_yfcase.id指的是父類的id(Yfcase)
    return redirect("yfcase:yfcase_detail", instance_yfcase.id)
  context={
    "instance" : instance,
    "instance_yfcase" : instance_yfcase,
    "form" : form,
    "Title": "刪除副署人員2的簽核",
  }
  return render(request, "finaldecision/subsignture_b_delete.html",context)

def load_townships(request):
  city_id = request.GET.get('city')
  townships = Township.objects.filter(city_id=city_id).order_by('name')
  return render(request, 'yfcase/township_dropdown_list_options.html', {'townships': townships})


# ==========================  Result  =========================
def result_create(request,yfcase_id=None):
  # 要配合url回傳的yfcase_id，來取得超類的資料
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  if not request.user.is_staff or not request.user.is_superuser:
    raise Http404
  form = ResultForm(request.POST or None)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    # messages.success(request,"successfully Created")
    # 把父類的yfcase_id(不可寫成instance.id，回傳到子類的id)回傳給yfcase_detail
    return redirect("yfcase:yfcase_detail", yfcase_id)
  context = {
    "form" : form, 
    "instance_yfcase": instance_yfcase,
    "title": "新增執行結果",
  }
  return render(request, "result/result_form.html",context)

def result_update(request,yfcase_id=None,id=None):
  instance_yfcase = get_object_or_404(Yfcase,id=yfcase_id)
  instance = get_object_or_404(Result,id=id)
  form=ResultForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance=form.save(commit=False)
    instance.save()
    return redirect("yfcase:yfcase_detail", yfcase_id)
  context={
    "instance" : instance,
    "instance_yfcase" : instance_yfcase,
    "form" : form,
    "title": "更新執行結果",
  }
  return render(request, "result/result_form.html",context)

# ==========================  PDF(評量表)  =========================
def font_path():
  pdfmetrics.registerFont(TTFont('yh', '{}/fonts/TaipeiSansTCBeta-Regular.ttf'.format(settings.STATICFILES_DIRS[0])))
  DEFAULT_FONT['helvetica'] = 'yh'


# PDFkit-評量表
class yfratingscalePDFView(PDFView):
  template_name = './pdf/yfratingscale_pdf.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    pk = kwargs.get('pk')
    yfcase = Yfcase.objects.get(pk=pk)
    context.update({
        'yfcase': yfcase,
    })
    return context
