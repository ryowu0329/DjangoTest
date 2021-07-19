import numpy as np
from urllib.parse import quote
from decimal import *
from django import template
from datetime import datetime
from django.utils.safestring import mark_safe

 
register=template.Library()
 
# 平方公尺 * 0.3025 = 坪
# 使用方式 value|m2toping
@register.filter
def m2toping(value):
  newlist=[]
  try:
    return value * Decimal(float(0.3025))
  except:
    newlist.append(0)

# 將兩個數相乘
# 使用方式 value|multiplication:100
@register.filter
def multiplication(value, arg):
  newlist=[]
  try:
    return value * arg
  except:
    newlist.append(0)

# 將兩個數相除
# 使用方式 value|divide:10
@register.filter
def divide(value, arg):
  try:
    return int(value) / int(arg)
  except (ValueError, ZeroDivisionError):
    return None

# 判斷是否為兩週內 
# 使用方式 auctionDate|less_two_week:"1拍"
@register.filter
def less_two_week(auctionDate,auctionStr):
  # 取得目前的日期，要用from datetime import datetime,不可用import datetime
  today = datetime.now()
  # 修改對應日期的格式
  auctionDateValue = datetime.strptime(auctionDate,'%Y-%m-%d')
  DateValue = (auctionDateValue-today).days + 1
  if DateValue >= 0 and DateValue <= 14 :
    return auctionStr + "(" + str(DateValue) + "天後)"
    
    
# 計算轄區字數是否超過3個字元(例如：雙北桃竹苗)
# 用法 {{ finaldecision.subSigntrueWorkAreaA|isWordCountOverFour }}
@register.filter
def isWordCountOverFour(value):
  if len(value) >= 4 :
    return mark_safe( "<div style='font-size: 11pt; height: 37px; line-height: 30px; color: red;'>" + str(value) +  "</div>")
  else:
    return mark_safe( "<div style='font-size: 16pt; height: 37px; line-height: 30px; color: red;'>" + str(value) +  "</div>")

# 計算轄區字數是否超過3個字元(例如：雙北桃竹苗)--用於評量表PDF
# 用法 {{ finaldecision.subSigntrueWorkAreaA|isWordCountOverFour2 }}
@register.filter
def isWordCountOverFour2(value):
  if len(value) >= 4 :
    return mark_safe( "<div style='font-size: 9pt; height: 30px; line-height: 22px; color: red;'>" + str(value) +  "</div>")
  else:
    return mark_safe( "<div style='font-size: 14pt; height: 30px; line-height: 22px; color: red;'>" + str(value) +  "</div>")

# 判定scoreItem是否存在，是：scoreItem連同scoreValue一起出現，否：不顯示(同於參考物件評分)
# 用法 {% isItem scoreItem scoreValue %}
@register.simple_tag(name='isItem')
def isItem(item, value):
  if item == None :
    return ""
  else:
    if value >= 0:
      return mark_safe( "<div style='color: blue;text-align: left;'>&#10148" + "(+" + str(value) + ")" + item+ "</div>")
    elif value < 0:
      return mark_safe( "<div style='color: red;text-align: left;'>&#10148" + "(" + str(value) + ")" + item + "</div>")
    else:
      return ""

# 判定scoreItem是否存在，是：scoreItem連同scoreValue一起出現，否：不顯示(同於評量表PDF)
# 用法 {% isItem2 scoreItem scoreValue %}
@register.simple_tag(name='isItem2')
def isItem2(item, value):
  if item == None :
    return ""
  else:
    if value >= 0:
      return "(+" + str(value) + ")" + item
    elif value < 0:
      return "(" + str(value) + ")" + item
    else:
      return ""

# 民國年份
# 用法 {{ yfcase.yfcaseDeedtaxEstablishmentDate|chinese_year }}
@register.filter
def chinese_year(chinese_date):
  if chinese_date:
    return int(chinese_date.year)-1911


# 數字改為中文    
# 用法 {{ coownerinfo.coOwnerLandHPAll|num2cn2 }}
@register.filter   
def num2cn2(number, traditional=False): 
  """ 
  數字轉換成中文（簡體和繁體，目前支持到12位數值） 
  :param number: 
  :param traditional:
  :return: 
  """ 
  if traditional: 
    chinese_num = {0: '零', 1: '壹', 2: '貳', 3: '叄', 4: '肆', 5: '伍', 6: '陸', 7: '柒', 8: '捌', 9: '玖'} 
    chinese_unit = ['仟', '', '拾', '佰'] 
  else: 
    chinese_num = {0: '零', 1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八', 9: '九'} 
    chinese_unit = ['千', '', '十', '百'] 
  extra_unit = ['', '萬', '億'] 
  num_list = list(str(number)) 
  num_cn = [] 
  zero_num = 0 # 連續0的個數 
  prev_num = '' # 遍歷列表中當前元素的前一位 
  length = len(num_list) 
  for num in num_list: 
    tmp = num 
    if num == '0': # 如果num為0，記錄連續0的數量 
      zero_num += 1 
      num = '' 
    else: 
      zero = '' 
      if zero_num > 0: 
        zero = '零' 
      zero_num = 0 
      # 處理前一位數字為0，後一位為1，並且在十位數上的數值
      if prev_num in ('0', '') and num == '1' and chinese_unit[length % 4] in ('十', '拾'): 
        num = zero + chinese_unit[length % 4] 
      else: 
        num = zero + chinese_num.get(int(num)) + chinese_unit[length % 4] 
    if length % 4 == 1: # 每隔4位加'萬'、'億'拼接 
      if num == '零': 
        num = extra_unit[length // 4] 
      else: 
        num += extra_unit[length // 4] 
    length -= 1 
    num_cn.append(num) 
    prev_num = tmp 
  num_cn = ''.join(num_cn) 
  return num_cn

# 計算轄區字數是否超過3個字元(例如：住宅大樓-11層含以上有電梯)
# 用法 {{ build.buildTypeUse|isWordCount:5 }}
@register.filter
def isWordCount(value,wordCount):
  if len(value) >= wordCount:
    return mark_safe( "<div style='font-size: 9pt;margin:3px 0px;'>" + str(value) +  "</div>")
  else:
    return mark_safe( "<div style='font-size: 12pt;'>" + str(value) +  "</div>")

# 編號由2開始，回傳陣列中對應字串的第幾個位置
# 用法{{coowners.all|times:coownerinfo.coOwnerName}}
# coowners.all為QuestSet ,coownerinfo.coOwnerName為coowners.all其中一人的名字
@register.filter(name='times') 
def times(cownerinfo,coownername):
  return list(cownerinfo.values_list('coOwnerName',flat=True)).index(coownername)+2



