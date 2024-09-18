"""
file     : 2024-01.python_tutorial.py
author   : Ming-Chang Lee
date     : 2024.09.19
email    : alan9956@gmail.com
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
"""

##############################
# 5天程式語言應用主題
##############################
# 🌸Day1 Python 語言簡介
# Day2 Python 機器學習
# Day3 資料探勘技術介紹
# Day4 Python程式應用實例
# Day5 大數據程式語言評量測驗與解析

##############################
# Day1 Python 語言簡介
##############################
# 大綱
# 1.RWEPA簡介
# 2.資料分析暨視覺化的心法
# 3.Python 簡介
# 4.Anaconda 簡介
# 5.資料型態與四大資料物件
# 6.pandas 資料處理

##############################
# 1.RWEPA簡介
##############################

# RWEPA簡介 http://rwepa.blogspot.com/

##############################
# 2.資料分析暨視覺化的心法
##############################

# 資料分析架構 --> APC方法
# 1.群組
# 2.時間
# 3.建立評估變數

# 如何學習 Python?
尋找答案 = {"方法1": "同事,同學,朋友等",
            "方法2": "Google", 
            "方法3": "alan9956@gmail.com"}

尋找答案
type(尋找答案)

# R+Shiny, Python+Streamlit 互動式平台

# 2020新型冠狀病毒視覺化
# http://rwepa.blogspot.com/2020/02/2019nCoV.html

# shiny 顧客連接分析
# https://rwepa.shinyapps.io/shinyCustomerConnect/

# 品質管制圖(quality control chart)應用
# http://rwepa.blogspot.com/2021/10/r-shiny-quality-control-chart.html

# Taiwan Stock App
# https://rwepa.shinyapps.io/shinyStockVis/

# RWEPA | shiny企業實務應用 第4集-shiny銷售儀表板
# Shiny: https://rwepa.shinyapps.io/shinySalesDashboard/
# Ubuntu Shiny Server: https://shiny.rwepa.net/shiny-sales/
# YouTube: https://youtu.be/4GgZlf8heQk
# Slide: https://rwepa.quarto.pub/r-shiny-04-sales-project/
# Code: https://github.com/rwepa/business_analytics/tree/main/r-shiny-04-sales-project
# 謝謝 ^_^ 訂閱、讚、開啟小鈴鐺

# RWEPA | shiny企業實務應用 第6集-小明算命師(下) - 第1季完結篇
# Ubuntu Shiny Server: https://shiny.rwepa.net/shiny-hr-teller/
# YouTube: https://youtu.be/rrD6KV3eV-w
# Slide: https://rwepa.quarto.pub/r-shiny-06-hr-teller/
# Code: https://github.com/rwepa/business_analytics/tree/main/r-shiny-06-hr-teller

# Power BI 進行RFM分析
# 🌸YouTube：https://youtu.be/Lkr9HmzLTtg
# 🌸http://rwepa.blogspot.com/2023/07/rwepa-rfm-analysis-using-power-bi.html

# Tableau - 智慧製造應用
# https://github.com/rwepa/Talks
# https://public.tableau.com/app/profile/ming.chang.lee/vizzes

# Tableau 教學
# Tableau資料分析與視覺化工具實作教師工作坊(初階)
# https://github.com/rwepa/Talks/blob/main/tableau_tutorial_basic.pdf

# Tableau資料分析與視覺化工具實作教師工作坊(進階)
# https://github.com/rwepa/Talks/blob/main/tableau_tutorial_advanced.pdf

# Tableau與R語言實務應用
# https://github.com/rwepa/Talks/blob/main/tableau_r.pdf

# Tableau與MySQL資料庫實務應用
# https://github.com/rwepa/Talks/blob/main/tableau_mysql.pdf

# 登山路線視覺化分析平台 (Python + Streamlit)
# YouTube：https://youtu.be/-_zghs2qrIg
# 系統展示：https://rwepa-climb.streamlit.app/

# RWEPA錄製R教學: 上集,下集
# R入門資料分析與視覺化應用(7小時28分鐘)
# https://mastertalks.tw/products/r?ref=MCLEE

# R商業預測應用(8小時53分鐘)
# https://mastertalks.tw/products/r-2?ref=MCLEE

##############################
# 3.Python 簡介
##############################
# https://www.python.org/ 

# PyPI (Python Package Index)
# https://pypi.org/

pip list

##############################
# 4.Anaconda 簡介
##############################

# Anaconda 下載
# https://www.anaconda.com/

# 實作練習
# 在 jupyter notebook 輸入以下程式碼練習
# positron_python_plotnine.ipynb

# 安裝plotnine 模組
# !pip install plotnine
from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap
from plotnine.data import mtcars
(
ggplot(mtcars, aes("wt", "mpg", color="factor(gear)"))
+ geom_point()
+ stat_smooth(method="lm")
+ facet_wrap("gear")
)

# jupyter notebook – 更改預設目錄
# cd C:\
# 切換至D磁碟 D:
# jupyter-notebook

# 實作練習
# 開啟下列 ipynb 檔案
# Python 程式設計-李明昌 <免費電子書>
# http://rwepa.blogspot.com/2020/02/pythonprogramminglee.html

# https://github.com/rwepa/DataDemo/blob/master/Python_Programming_Lee_ipynb.zip

# 使用命令提示列 開啟 Orange
# python -m Orange.canvas

# Python Orange - 關聯規則教學
# YouTube: https://youtu.be/rh5GxJamtNg
# https://rwepa.blogspot.com/2022/07/python-orange-associate-tutorial.html

# 顯示已安裝模組
!conda list

# RWEPA | Python 安裝 Anaconda 軟體之後, 如何理解已安裝模組清單?
# http://rwepa.blogspot.com/2023/11/python-anaconda-packages-list.html

# 尋找官網套件
# conda search matplotlib

# 安裝模組
# conda install 模組名稱

# 更新模組
# conda update 模組名稱

# Spyder 軟體簡介

# Spyder 更新
# 步驟1.Anaconda 整體更新
# conda update anaconda

# 步驟2.Spyder 更新
# conda update spyder

# 實作練習
# 熟悉自動換列等設定
# Tools \ Preferences \ Editor \ Display \ Wrap lines

# 恭喜您, 開啟人生 - Python 學習之旅 ^_^

# Python 執行-命令提示列
# 建立 C:\mydata\helloworld.py

# cd C:\mydata
# python --version
# dir
# python helloworld.py

# 變數

# 合法
大數據 = 1 # 中文亦可,建議不要使用
CustomerSaleReport = 1
_CustomerSaleReport = 1
Customer_Sale_Report = 1
customer_sale_report = 1

# 不合法變數
$CustomerSaleReport = 1 # SyntaxError: invalid syntax
2020_sale = 100 # SyntaxError: invalid decimal literal
break = 123 # SyntaxError: invalid syntax

# 內建保留字
dir(__builtins__)
len(dir(__builtins__)) # 159

# 指派多個變數
x, y, z = "台北", "台中", "高雄"
print(x,y,z)
type(x) # str

address = ["台北", "台中", "高雄"]
x, y, z = address
print(x)
print(y)
print(z)

# Python Style Rules
# https://google.github.io/styleguide/pyguide.html

# Python 註解
# 使用一個 #	   用於1行註解
# 使用二個 """  用於超過1行註解或函數之說明文件

# 內縮4個空白鍵之語法

##############################
# 5.資料型態與四大資料物件
##############################

##############################
# 資料型態
##############################

# https://docs.python.org/3/library/stdtypes.html

# 整數 int (早期有長整數 long)
x1 = 1
type(x1)

# 浮點數 float
x2 = 1.234
type(x2)

# 複數  complex
x3 = 1+2j
type(x3)

# 布林值 (Boolean)
x4 = True
type(x4)
x4 + 10

# None值
import numpy as np
None == False
None == 0
False == 0
True == 1
None == np.nan
None == None

# 整數亂數
import random
random.seed(168)
myrandom = random.randrange(1, 100)
myrandom

##############################
# 基本運算
##############################

# 運算子
3 + 5
3 + (5 * 4)
3 ** 2
"Hello" + "World"
1 + 1.234
7 / 2
7 // 2
7 % 2
2 ** 10
1.234e3 - 1000

x5 = 1 == 2
x5
x5 + 10

# 位移運算子: << 向左位移
# 位移運算子: >> 向右位移
a = 4 << 3 # 0100 --> 0100000, 32 16 8 4 2 1
print(a)

b = a * 4.5
print(b)

c = (a+b)/2.5

# 指派運算子
x = 9
x+=2
print(x)

##############################
# 資料物件
##############################

# Tuple (序列/元組) - (value,...) 不可修改
# List (串列/清單)  - [value,...]
# Set 集合          - {value,...}
# Dict 字典         - {key:value,...}

##############################
# Tuple 序列 (元組)
##############################

# 建立序列
f = (2,3,4,5) # A tuple of integers
g = () # An emptmy tuple
h = (2, [3,4], (10,11,12)) 	# A tuple containing mixed objects

# Tuples操作
x = f[1] # Element access. x = 3
x

y = f[1:3] # Slices. y = (3,4)
y

z = h[1][1] 	# Nesting. z = 4
z

# 基本型態 – Tuple
xy = (2, 3)
xy

personal = ('Hannah',14,5*12+6)
personal

singleton = ("hello",)
singleton
type(singleton) # tuple

singleton1 = ("hello")
singleton1
type(singleton1) # str

# single format: tuple[index]
# index : 0  ~  len(tuple)-1
# index: -len(tuple)  ~  -1
f= (2,3,4,5)
f[0]
f[-1] # 索引 -1 表示倒數第1個元素
f[-2]
f[len(f)-1]

# slice format: tuple [start:end ]. Items from start to (end -1)
t=((1,2), (2,"Hi"), (3,"RWEPA"), 2+3j, 6E23)
t[2]
t[:3]
t[3:]
t[-1]
t[-3:]

# tuple 長度
len(t) # 5

##############################
# tuple 建構子
##############################
# 使用 tuple(( ... )) 或 tuple([ ... ]) 
employeeGender = tuple(("男", "女", "女"))
employeeGender

# tuple unpacking - 將元素指派至變數
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# TRY: green, yellow, red = fruits

##############################
# tuple unpacking - 使用萬用字元*
##############################
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# tuple - loop 處理
fruits = ("apple", "banana", "cherry")

# 方法1. tuple - 取出元素, 使用for
for x in fruits:
  print(x)

# 方法2. tuple - 取出元素, 使用while
i = 0
while i < len(fruits):
  print(fruits[i])
  i = i + 1
  
# 方法3. tuple - 取出元素, 使用指標 range, len
for i in range(len(fruits)):
  print(fruits[i])

# tuple - join 結合
tuple1 = ("台北", "台中", "高雄")
tuple2 = ("男", "女", "女")
tuple3 = tuple1 + tuple2
print(tuple3)

# tuple - 重複
tuple1*3
3*tuple1

# count 次數統計
tuple = ("男", "女", "女", "男", "女")
tuple.count("男") # 2
tuple.count("女") # 3

##############################
# List 串列(清單)
##############################

# 建立串列
a = [2, 3, 4]            # 整數串列
b = [2, 7, 3.5, "Hello"] # 混合資料串列
c = []	                 # 空串列
d = [2, [a, b]]	         # 巢狀串列

# 串列的操作
a
a[1] 	   # 取得第2個元素
a[-1]      # 取得最後一個元素
b[1:3] 	   # 串列篩選
d[1][0][2] # 巢狀串列操作
b[0]       # 2
b[0] = 42  # 修改元素值
b[0]       # 42

# 串列 slice format
t=[1, 2, (3,"Hi"), [4,"RWEPA"], 2+3j, 6E7]
t

t[2]
t[:3]
t[3:]
t[-1]
t[-3:]

# 串列長度
len(t)

# list 建構子
# 使用 list(( ... )) 或 list([ ... ])
mylist1 = list(("男", "女", "女"))
mylist1

mylist2 = list(["男", "女", "女"])
mylist2

mylist1 == mylist2

# 串列 unpacking - 將元素指派至變數
fruits = ["apple", "banana", "cherry"]
green, yellow, red = fruits
print(green)
print(yellow)
print(red)
type(green) # str

# 串列 unpacking - 使用萬用字元*
fruits = ["apple", "banana", "cherry", "strawberry", "raspberry"]
green, yellow, *red = fruits
print(green)
print(yellow)
print(red)
type(green) # str

# 串列 - loop 處理
mylist = [1, 2, 3, [4, 5], ["A", "B", "C"]]
# 練習 loop 方法

# 方法1. list - 取出元素, 使用for
for x in mylist:
  print(x)

# 方法2. list - 取出元素, 使用while
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1

# 方法3. list - 取出元素, 使用指標 range, len
for i in range(len(mylist)):
  print(mylist[i])

# 方法4. list - 取出元素, 使用串列包含法 (List Comprehension)
[print(x) for x in mylist]

# 串列包含法應用

# for 資料篩選-包括字母 a
codes = ["Python", "R", "SQL", "Julia", ".NET", "Java", "JavaScript"]
newlist = []
for x in codes:
  if "a" in x:
    newlist.append(x)
print(newlist)

# 串列包含法應用1
# 亦可用於序列, 集合, 字典等可反覆運算物件(可迭代物件, iterable object)
codes = ["Python", "R", "SQL", "Julia", ".NET", "Java", "JavaScript"]
newlist = [x for x in codes if "a" in x]
print(newlist)

# 串列包含法應用2
newlist = [x.upper() for x in codes]
print(newlist)

codes.upper() # AttributeError: 'list' object has no attribute 'upper'

# 串列包含法應用3
newlist = ['RWEPA' for x in codes]
print(newlist)

# 串列 join 結合
e = a + b  # Join two lists
e

# 串列 repeat 重複
f1 = a*3    # repeat lists
f1

f2 = 3*a
f2

# 串列排序-預設為遞增排序,英文字母先大寫,再小寫
codes = ["python", "R", "SQL", "Julia", ".NET", "java", "JavaScript"]
codes.sort()
print(codes)

# 串列排序-先全部小寫,再排序
codes = ["python", "R", "SQL", "Julia", ".NET", "java", "JavaScript"]
codes.sort(key = str.lower)
print(codes)

# 串列排序-遞減排序
codes = ["python", "R", "SQL", "Julia", ".NET", "java", "JavaScript"]
codes.sort(reverse =True)
print(codes)

# 串列反序
codes = ["python", "R", "SQL", "Julia", ".NET", "java", "JavaScript"]
codes.reverse()
print(codes)

# 串列複製,使用等號會建立參考物件
a = [1, 2, 3]
a
b = a
b[0] = 999 # 修改b,亦會修改a
b
a # a已經更新

# 串列複製-使用 copy
a = [1, 2, 3]
b = a.copy()
b
b[0] = 999
b
a # a保持不變

# 串列複製-使用 list
a = [1, 2, 3]
c = list(a)
c
c[0] = 123
c
a # a保持不變

# 附加元素 append
a = [1, 2, 3]
a.append(['BigData', 'SQL']) # 新增1個元素
a
a.append('2021/8/14')
a

# 延伸元素 extend
a.extend(['Python', 'R', "Julia"]) # 新增一個串列
a

# 延伸元素 extend - 加入tuple,list,set,dict
a = [1, 2, 3]
a.extend(('4', '5', 'RWEPA')) # 延伸一個序列
a

a.extend({'8', '8', '10'}) # 延伸一個集合
a

a.extend({'a':'R', 'b':'Python'}) # 延伸一個字典-ONLY KEY, NO VALUE
a

# 串列 – insert

# 插入元素
a = list(range(5))
a
a.insert(2, 999) # 在指標為2的位置,插入新元素
a

# 串列 – remove, pop, del

# 刪除指定元素
a.remove(999)
a

# 刪除指定指標元素
a.pop(1)
a

# 刪除指定指標元素
del a[1]
a

# 刪除第一個元素
a.pop(0)
a

# 刪除最後一個元素
a.pop()
a

# 清空物件元素,物件仍存在記憶體
a.clear()
a

# 刪除物件,物件不存在記憶體
del a
print(a) # NameError: name 'a' is not defined

# 串列 - zip 應用
a = ("x1", "x2", "x3")
b = ("y1", "y2", "y3")
c = (1, 2, 3)

x = zip(a, b, c)
x
list(x)

# 顯示方法
print(dir(list))

##############################
# Set 集合
##############################

# 集合與字典相似, 但字典沒有key,只有值
# 集合內容不可以修改
# 集合是  unordered
# 集合是  unindexed
# 集合會忽略重複的值

a = set() # 空集合
type(a)

b = {"台北市", "新北市", "桃園市", "台中市", "台北市", "新北市", "高雄市"}
b # {'台中市', '台北市', '新北市', '桃園市', '高雄市'}

# b[0] = 1 # TypeError: 'set' object does not support item assignment
# b[0]     # TypeError: 'set' object is not subscriptable

len(b)

# 使用 myset 練習集合 - loop 方法
myset = {"台北市", "新北市", "桃園市", "台中市", "高雄市"}
myset

# 集合新增元素 add, 因為集合是unordered, 不一定新增在最後一個
myset = {"台北市", "新北市", "桃園市", "台中市", "高雄市"}
myset.add("台南市")
myset

# 集合新增集合
myset.update({"澎湖", "金門"})
myset

# 刪除指定元素
myset.remove("澎湖")
myset

# 清空物件兀素,物件仍存在記憶體
myset.clear()
myset

# 刪除物件,物件不存在記憶體
del myset
myset # NameError: name 'myset' is not defined

# 集合運算
x = {1,2,3,4,5}
y = {1,3,5,7}

x & y # {1, 3, 5} # 交集

x.intersection(y) # 交集

x | y # {1, 2, 3, 4, 5, 7} # 聯集

x.union(y) # 聯集

x ^ y # {2, 4, 7} # XOR 互斥

x - y # 差集

x.difference(y) # 差集

##############################
# Dict 字典
##############################

# 字典宣告
mydict = {
    "language": "Python",
    "designer": "Guido van Rossum",
    "year": 1991
    }

print(mydict)

type(mydict) # dict

# 重複 key, 只保留1個
mydict1 = {
    "language": "Python",
    "designer": "Guido van Rossum",
    "year": 1991,
    "year": 2021
    }

print(mydict1)

# 字典存取元素
b = {
     "uid": 168, 
     "login": "marvelous", 
     "name" : 'Alan Lee'
     }
b

# dict 取得所有 keys
mykeys = b.keys()
print(mykeys)

# dict 取得所有 values
myvalues = b.values()
print(myvalues)

# dict 取得key的值
u = b["uid"] # 168
print(u)

# dict 更新值
b.update({"uid": 123})
print(b)

# dict 新增元素
b["shell"] = "/bin/sh"
print(b)

# dict 刪除元素 - pop
b.pop("shell")
print(b)

# dict 刪除元素 - del
del b["login"]
print(b)

# dict 清空整個物件 - clear
b.clear()
b

# dict 刪除整個物件 -del
del b
b

# dict - items 物件, 回傳 [(key1,value1), (key2,value2,...)]
# 回傳 list[(序列1), (序列2), ...]
b = {
     "uid": 168, 
     "login": "marvelous", 
     "name" : 'Alan Lee',
     "shell": "/bin/sh"
     }
b
x = b.items()
print(x)

# 檢查 key 是否存在
# AttributeError: 'dict' object has no attribute 'has_key'
# 早期版本使用 has_key
if b.has_key("uid"):
	d = b["uid"]
else:
	d = None

# 使用 in
if "uid" in b:   # v3.x 直接使用 in
    d = b["uid"]
else:
    d = None
print(d)

# 使用 get
d = b.get("uid", None) # 較簡潔
print(d)

# dict - loop 處理
mydict = {
    "uid": 168, 
    "login": "marvelous", 
    "name" : 'Alan Lee'
    }
mydict

# for - 回傳 keys
for x in mydict:
    print(x)
    
# for - 使用 keys
for x in mydict.keys():
    print(x)

# for - 回傳 values
for x in mydict:
    print(mydict[x])

# for - 使用 values()
for x in mydict.values():
    print(x)

# for - 回傳 (key, value) 使用 items()
for x,y  in mydict.items():
    print(x, y)

# 字典複製-使用 copy
mydict = {
    "uid": 168, 
    "login": "marvelous", 
    "name" : 'Alan Lee'
    }
mydict

mydict2 = mydict.copy()
print(mydict2)

# 字典複製-使用 dict
mydict3 = dict(mydict)
print(mydict3)

mydict2 == mydict3 # True

# 巢狀字典 (Nested Dictionaries)

# 方法1 一次建立一個巢狀字典
mycodes = {
    "code1" : {
         "name" : "Fortran77",
         "year" : 1977
         },
    "code2" : {
        "name" : "Python",
        "year" : 1991
        },
    "code3" : {
        "name" : "R",
        "year" : 2000
        }
    }

mycodes

# 方法2 建立三個字典,再合併為一項字典
mycode1 = {
    "name" : "Fortran77",
    "year" : 1977
    }

mycode2 = {
    "name" : "Python",
    "year" : 1991
    }

mycode3 = {
    "name" : "R",
    "year" : 2000
    }

mycodes2 = {
  "程式1" : mycode1,
  "程式2" : mycode2,
  "程式3" : mycode3
}

mycodes2

##############################
# 模組 Modules
##############################

# 使用模組
import math
math.sqrt(9)

from math import sqrt
sqrt(9)

# 切換工作目錄
import os
os.getcwd() # 讀取工作目錄
os.chdir("C:/") # 變更工作目錄
os.getcwd()
os.listdir(os.getcwd()) # 顯示檔案清單

# 模組的搜尋路徑
import sys
sys.path
# '' 表示現行目錄

##############################
# 判斷式 if elif else
##############################

"""
# case 1
if 布林值:
 	若布林值為 True，執行命令

# case 2
if 布林值:
 	若布林值為 True，執行命令
else:
    若布林值為 False，執行命令

# case 3
if 布林值一:
 	若布林值一為 True，執行命令
elif 布林值二:
 	若布林值二為 True，執行命令
...
else:
 	若布林值一和二...都是 False，執行命令
"""

# elif敘述
a = '+'

if a == '+':
	op = 'PLUS'
elif a == '-':
	op = 'MINUS'
else:
	op = 'UNKNOWN'

op

# 布林表示式 – and, or, not
a = 1
b = 6
c = 9

if b >= a and b <= c:
	print('b is between a and c')
    
if not (b < a or c > c):
	print('b is still between a and c')

# if 範例 - 測試所有輸入情形
mynameage = input('輸入姓名與年齡: ')

name = mynameage.split(',')[0]
age = mynameage.split(',')[1]

if name == 'Alan':
    print('Hi, Alan.')
elif age < 20:
    print('You are not Alan.')

# 邏輯錯誤 (Logical Errors)
# if 範例 - age > 200 不會執行
name = 'RWEPA'
age = 300
if name == 'Alan':
    print('Hi, Alan.')
elif age < 20:
    print('You are not Alan.')
elif age > 100:
    print('You are not Alan. 大大')
elif age > 200:
    print('年齡異常')
# You are not Alan. 大大

##############################
# 迴圈 (Loops)
##############################

# while 迴圈
name = ''
while name != 'Alan Lee':
    print('Please type your name.')
    name = input()
print('Thank you!')

# while + break
while True:
    print('Please type your name.')
    name = input()
    if name == 'Alan Lee':
        break
print('Thank you!')

# while + break + continue
while True:
    print('Who are you?')
    name = input()
    if name != 'Alan':
        continue
    print('Hello, Alan. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

# for + range

# 顯示list元素
for i in [3, 4, 10, 25]:
	print(i)

# 顯示一個字元
for c in "Hello":
	print(c)

# 顯示 range 元素
for i in range(1, 4):
	print(i)

for i in range(4, -2, -1):
	print(i)

# 零數值判斷, 以下結果皆為 True
0 == False
0.0 == False
0.000 == False
'' == False

# 非零數值判斷
1 == True     # True
1.23 == True  # False
1.23 == False # False

# 實作練習10
# for + continue 迴圈練習, 篩選出 list 的字串資料
# 提示: 使用 if, for, append, continue 順序非固定
# 結果 ['python', '123.45', 'RWEPA', 'R']
mylist = [1, 3, "python", '123.45', "RWEPA", 100, "R"]

##############################
# def 宣告函數
##############################

# 回傳 a/b 之商數與餘數

def divide(a,b):
	q = int(a/b)
	r = a - q*b
	return q,r

x, y = divide(42,5) # x = 8, y = 2
print(x)
print(y)

##############################
# 6.pandas 資料處理
##############################

# 10 minutes to pandas
# https://pandas.pydata.org/docs/user_guide/10min.html

# 載入2大套件 numpy, pandas
import numpy as np  # Python Scientific Computing Library
import pandas as pd # Python Data Analysis Library

##############################
# pandas 序列(Series)物件
##############################

# s = pd.Series(data, index=index)
# data 包括使用 array, Iterable, dict, scalar value
# 序列包括指標(Index) 與值(Value), 指標採用預設整數型態指標 0,1,2,...

# (1).Series - 使用 ndarray
s = pd.Series(data = np.random.randn(5), index=["a", "b", "c", "d", "e"])
s
# a   -0.492604
# b   -0.073386
# c   -0.063632
# d    0.197128
# e    0.178333
# dtype: float64
type(s) # pandas.core.series.Series

# (2).Series -使用 Iterable - 序列(tuple)
s1 = pd.Series((1,3,5,np.nan,6,8))
s1

# (3).Series - 使用 Iterable - 串列(List)
s2 = pd.Series([1,3,5,np.nan,6,8])
s2

s1 == s2 # equality 相等, 比較每個元素是否相同, 大部分使用此功能.
s1 is s2 # identity 相同, 比較二物件是否指向同一個記憶體

id(s1)
id(s2) # 與id(s1) 不相等

# "==" 與 "is" ("is not") 應用

# identity - 使用 id 函數, 查看說明 help(id). 相同程式 id 結果,每次不一定相同.
# https://realpython.com/python-is-identity-vs-equality/

a = 'Hello world'
b = 'Hello world'
a == b
a is b
id(a)
id(b)

# 整數 [-5 ~ 256] 會使用相同記憶體位址功能
a = 256
b = 256
a == b   # True
a is b   # True
id(a)
id(b)

a = 1000
b = 1000
a == b   # True
a is b   # False
id(a)
id(b)

x1 = np.nan
x2 = np.nan
id(x1)
id(x2) # 與上面結果相同
x1 == x2 # False
x1 is x2 # True

# (4).Series - 使用 Iterable - 字典(Dict)
# 在 pandas 模組之中, NaN 表示為 "not a number"
x = {"x1": 1, "x2": 2, "a": np.nan, "b": 3, "c": 4}
c = pd.Series(x)
c

# (5).Series - 使用 scalar value
pd.Series(999.0, index=["a", "b", "c", "d", "e"])

##############################
# Series 使用 ndarray-like 操作
##############################
c
# x1    1.0
# x2    2.0
# a     NaN
# b     3.0
# c     4.0
# dtype: float64

c[0]              # 1.0
c[1]              # 2.0
c[-1]             # 4.0
c[:3]
# x1    1.0
# x2    2.0
# a     NaN
# dtype: float64

c[c > c.median()]
c[[1, 3, 2]]
np.exp(c)
c.dtype

# Series.array 是 pandasExtensionArray.
# ExtensionArray 是包括一個或多個 numpy.ndarray 的 thin wrapper類別
c.array      # 將 series 轉換為 PandasArray

c1 = c.to_numpy() # 將 series 轉換為 NumPy ndarray
c1

c2 = c.to_numpy
c2

c1 == c2
c1 is c2

##############################
# Series 使用 dict-like 操作
##############################
c

c['x1']
c['a'] = np.pi

'x1' in c

c.get("a")
c.get("e") # None

##############################
# pandas 資料框(DataFrame)物件
##############################

# 方法1.建立指標與值,再合併為資料框

# 步驟1-建立 DatetimeIndex 物件
dates = pd.date_range('20210801', periods=6) # 日期指標
dates
type(dates)

# 步驟2-建立 DataFrame
# 欄位名稱: A, B, C, D
df1 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df1
type(df1)

# 方法2.使用字典建立資料框
df2 = pd.DataFrame({ 'A' : 1.,
    'B' : pd.Timestamp('20210801'),
    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
    'D' : np.array([3] * 4,dtype='int32'),
    'E' : pd.Categorical(["test","train","test","train"]),
    'F' : 'foo' })
df2

# dtypes: 顯示各欄位的資料型態
df2.dtypes

# 方法3.使用 list of dicts 建立資料框

# 預設指標
mydata = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]
df3 = pd.DataFrame(mydata)
df3

# 客製化指標
df4 = pd.DataFrame(mydata, index=["first", "second"])
df4

# 方法4.使用 dict of tuples 建立資料框
# 使用 tuples dictionary, 可建立 MultiIndexed dataframe(階層式指標資料框)
df5 = pd.DataFrame(
    {
        ("a", "b"): {("A", "B"): 1, ("A", "C"): 2},
        ("a", "a"): {("A", "C"): 3, ("A", "B"): 4},
        ("a", "c"): {("A", "B"): 5, ("A", "C"): 6},
        ("b", "a"): {("A", "C"): 7, ("A", "B"): 8},
        ("b", "b"): {("A", "D"): 10, ("A", "B"): 11},
    }
)
df5
type(df5)

# 方法5.使用 list of dataclasses 建立資料框
# pandas 1.1.0 新增功能, 參考 PEP 557 -- Data Classes
# list of dataclasses 類似於 list of dictionaries
# https://www.python.org/dev/peps/pep-0557/

from dataclasses import make_dataclass
Mydata = make_dataclass("Stations", [("x", int), ("y", int)])
Mydata
df6 = pd.DataFrame([Mydata(0, 0), Mydata(0, 3), Mydata(2, 3), Mydata(1, 2)])
df6

##############################
# 排序
##############################

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html

# (1).排序 sort_index

# axis為排序的軸，0表示 rows index(列指標)，1表示 columns index(行指標)
# 當對資料"列" 進行排序時，axis必須設置為0.
# df.sort(["A"]) 新版不支援 sort 函數, 改用 sort_values 或 sort_index

# ascending =FALSE, 即遞增是FALSE, 表示遞減是TRUE, 結果為D,C,B,A
df1.sort_index(axis=1, ascending=False)

# (2).排序 sort_values

# 依照 B 欄大小, 由小至大排序 (預設值是遞增)
df1.sort_values(by='B')

# 依照 B 欄大小, 改為由大至小排序 (遞減)
df1.sort_values(by='B', ascending = False)

# 依照 B 欄大小, 將 nan 排在最前面或最後面
df1.iloc[2, 0] = np.nan
df1
df1.sort_values(by='A')
df1.sort_values(by='A', na_position = 'first')

# 實作練習
# 使用 mydf 進行A欄位遞增, B欄位遞減排序
#    A   B   C
# 0  1  10  aa
# 1  2  24  bb
# 2  2  26  cc
# 3  4   9  dd
# 4  2  29  aa

##############################
# 資料列,行選取
##############################

import numpy as np
import pandas as pd
np.random.seed(123)
dates = pd.date_range('20210801', periods=6) # 日期指標
df1 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df1

# 選取行
df1['A']
df1.A
df1[['A', 'B']]

# 選取列, df[1:4]選取第1至第3列(4-1=3), 此功能與 R 不同.
df1
df1[1:4]

# 使用 loc
df1.loc[:, ['A','B']]

# 使用 iloc
df1.iloc[2] # 指標為第2列

df1.iloc[2:4,]
df1.iloc[2:4, :]

df1.iloc[, 2]    # ERROR
df1.iloc[:, 2]   # OK
df1.iloc[:, 2:4] # OK

# Boolean Indexing 邏輯值(條件式)資料選取
df1.loc[dates[2]]
df1.loc['20210803']

df1.loc['20210803', ['A', 'B']]
df1.loc['20210802':'20210804', ['A', 'B']]

df1.iloc[[1,2,4],[0,2]] # 選取不連續範圍

df1.iloc[2,2]
df1.iat[2,2]

df1[df1 > 1.5]
df1[df1.A > 1.5]

# 使用 .isin - 範例1
df1[df1.index.isin(['2021-08-02', '2021-08-04'])]

# 使用 .isin - 範例2

df2 = df1.copy()
df2['E'] = ['one', 'one','two','three','four','three']
df2
df2[df2['E'].isin(['two','four'])]

##############################
# Missing Data 遺漏值 NaN
##############################

# Python: np.NaN (np.nan)
# R: 使用NA
df3 = df1.reindex(index=dates[0:4], columns=list(df1.columns) + ['E'])
df3.loc[dates[0]:dates[1],'E'] = 1
df3

# 判斷何者為NaN
pd.isnull(df3)

# 刪除列中包括 NaN
df3.dropna(how='any')

# 將遺漏值填入值
df3.fillna(value=999)

##############################
# 群組 Grouping
##############################
# https://github.com/rwepa/DataDemo/blob/master/Cars93.csv

import pandas as pd
df = pd.read_csv('C:/mydata/Cars93.csv')
df

df = df[['Manufacturer', 'Price', 'AirBags', 'Horsepower', 'Origin']]

df.head()

df_AirBags = df.groupby('AirBags')
type(df_AirBags)

print(df_AirBags.groups)

# 群組 - 2個維度
df_AirBagsOrigin = df.groupby(['AirBags', 'Origin'])

# 群組大小
df_AirBagsOrigin.size()

# 篩選群組
df_AirBags.get_group('Driver & Passenger')

# 群組總和
df_AirBags.sum()

# 群組平均
df_AirBags.mean()

# agg - 每行計算min
df_AirBags.agg('min')

# agg - 每行計算max
df_AirBags.agg('max')

# 資料摘要
import pandas as pd
df = pd.read_csv('C:/mydata/Cars93.csv')
df

df.dtypes # object: 字串, float64: 含小數點數值

df.describe() # 無法顯示所有欄位
df.describe(include='all') # 顯示所有欄位

# 顯示所有資料
pd.set_option('display.max_rows', None, 'display.max_columns', None) # None 沒有限制
df.describe()
df

##############################
# 檔案匯入 pandas
##############################

# pandas IO 模組
# https://pandas.pydata.org/docs/user_guide/io.html

##############################
# 讀取 Excel
##############################

# 匯入 Excel 檔案, 全國訂單明細.xlsx
# https://github.com/rwepa/DataDemo/blob/master/全國訂單明細.xlsx

sales = pd.read_excel(io = 'C:/mydata/全國訂單明細.xlsx', sheet_name = '全國訂單明細')
sales # 8568*19
sales.head()

sales['產品包箱']
sales['產品包箱'].value_counts()
sales['產品包箱'].value_counts(dropna=False)

##############################
# 資料匯出
##############################
df = pd.DataFrame({'姓名': ['ALAN', 'LEE'],
                   '地址': ['台北市', '新北市'],
                   '年資': [10, 20]})
df
#      姓名   地址  年資
# 0  ALAN  台北市  10
# 1   LEE  新北市  20

df.to_csv('data/df.csv', index = False) # 中文亂碼

df.to_csv('data/df.csv', index = False, encoding = 'utf-8') # 中文亂碼

df.to_csv('data/df.csv', index = False, encoding = 'utf_8_sig') # OK

# 參考資料 -----

# RWEPA
# http://rwepa.blogspot.com/

# Python 程式設計-李明昌 <免費電子書>
# http://rwepa.blogspot.com/2020/02/pythonprogramminglee.html

# R入門資料分析與視覺化應用教學(付費)
# https://mastertalks.tw/products/r?ref=MCLEE

# R商業預測與應用(付費)
# https://mastertalks.tw/products/r-2?ref=MCLEE
# end
# 辛苦啦,完成 Python 程式之旅 ~~
