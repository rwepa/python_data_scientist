# file     : line_chart_plotly.py
# title    : line chart with pandas and plotly
# author   : Ming-Chang Lee
# date     : 2024.10.18
# YouTube  : https://www.youtube.com/@alan9956
# RWEPA    : http://rwepa.blogspot.tw/
# GitHub   : https://github.com/rwepa
# Email    : alan9956@gmail.com

# 載入套件
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio

# 設定中文字型
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# Spyder plotly plot for browser
pio.renderers.default = "browser"

df = pd.DataFrame({'日期': ['113年1月初', '113年2月初', '113年3月初'],
                   '指標1': [20, 60, 40],
                   '指標2': [70.5, 55, 90.5]})
df
df.dtypes

# 將民國年改為西元年
years = pd.to_numeric(df["日期"].str.split("年", expand = True)[0])+1911
years

# 修改月資料
months = pd.to_numeric(df["日期"].str.split("年", expand = True)[1].str.split("月初", expand = True)[0])
months

# 合併西元年/月/01 為日期格式
df["日期"] = pd.to_datetime(years.astype(str) + "/" + months.astype(str) + "/01")
df

# Line chart with pandas
df.plot(x='日期', y=['指標1', '指標2'], figsize=(20, 15))
plt.xlabel('Date')
plt.ylabel('Index')
plt.title('Index plot')
plt.legend(loc='best')

# Line chart with plotly
fig = px.line(df, x="日期", 
              y=['指標1', '指標2'], 
              title='Index plot')
fig.show()
# end
