# 課程: Python程式語言應用專題報告
# 主題: 股價預測
# 學號: 168
# 姓名: 李明昌
# 日期: 2024年10月10日

# 注意:
# 1. 本研究使用 Jupyter notebook 撰寫, 版本如下:
# !jupyter --version

# 2. 將 Jupyter notebook 轉換為 py 方法如下:
# !jupyter nbconvert --to script report_stock_prediction.ipynb

# 3. 下載舊版 Anaconda
# 下載最新版 Anaconda: https://www.anaconda.com/download
# 如果 Jupyter notebook 使用時有異常, 可以下載舊版 Anaconda.
# https://repo.anaconda.com/archive/
# 範例： Anaconda3-2024.02-1-Windows-x86_64.exe.
# https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Windows-x86_64.exe

# 4.報告規範:
# https://github.com/rwepa/python_data_scientist/blob/main/report_readme.txt


# # 1.商業理解

# 研究目的: 探討使用機器學習的監督式學習進行股票的預測 
# 資料來源: Machine Learning and Data Science Blueprints for Finance, 2020.
# URL: https://www.amazon.com/Machine-Learning-Science-Blueprints-Finance/dp/1492073059
# 報告名稱: report_stock_prediction.ipynb

# 研究的目標是建立一個機器學習模型, 使用監督式學習的演算法, 參考技術指標與基本面資料. 對股票價格進行預測並提供決策參考.

# 預測的反應變數為微軟股票的週報酬率(Weekly return of Microsoft stock).
 
# 研究的獨立變數(Independent variables)包括:
 
# + IBM股票
# + Google股票
# + 美元／日元(USD/JPY)貨幣
# + 英鎊／美元匯率(GBP/USD)貨幣
# + 標準普爾500指數(S&P 500), 參考: https://zh.wikipedia.org/wiki/S%26P_500
# + 道瓊工業指數(Dow Jones Industrial Average Index, 簡稱Dow Jones, Dow), 參考: https://zh.wikipedia.org/wiki/道琼斯工业平均指数
# + 波動率指數(芝加哥選擇權交易所市場波動率指數, VIX), 參考: https://zh.wikipedia.org/wiki/VIX指数

# # 2.資料理解

# 資料理解包括以下主題, 其中資料匯入與資料摘要為必需主題:
# 
# + 資料匯入
# + 資料摘要
# + 探索性資料分析
# + 資料視覺化
# + 資料清理
# + 資料合併
# + 特徵選擇
# + 資料轉換
# 
# 本研究使用 Python 程式語言(Python, 2024)並參考RWEPA網站資料(Lee, 2024)與Tatsat et al.(2020).

# ## 2.1 模組與資料匯入

# 讀取股票模組
# 原範例使用 pandas_datareader 讀取股票資料會有錯誤, 已經修改使用 yfinance 模組讀取股票資料.
# 參考: https://github.com/ranaroussi/yfinance
# pip install yfinance
import yfinance as yf

# 使用 pandas_datareader 模組讀取貨幣,指標資料結果為正常顯示.
# pip install pandas_datareader
import pandas_datareader.data as web

# 載入監督式迴歸模型
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR

# 載入資料處理與模型評估模組
# from sklearn.model_selection import train_test_split
# 本例因時間序列資料, 暫無須使用 train_test_split.
# 如果是一般監督式學習, 可使用 train_test_split 隨機區分訓練集與測試集
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error

# 載入 pandas 資料處理與視覺化模組
import numpy as np
import pandas as pd
from matplotlib import pyplot
from pandas.plotting import scatter_matrix
import seaborn as sns

# 設定股票代號
stk_tickers = ['MSFT', 'IBM', 'GOOGL']

# 設定貨幣代號
ccy_tickers = ['DEXJPUS', 'DEXUSUK']

# 設定指數代號
idx_tickers = ['SP500', 'DJIA', 'VIXCLS']

# 設定開始日期
start = "2010-1-1"
start

# 設定結束日期
end = "2024-10-10"
end

# 1.載入股票資料
# df = web.DataReader("MSFT", "yahoo", start, end)
# AttributeError: 'NoneType' object has no attribute 'group'


# <div class="alert alert-block alert-info">
# <b>注意: </b>因 yahoo參數已更新, 但 pandas_datareader.DataReader 尚未更新會有錯誤. 部分資料擷取改用 yfinace.download.
# </div>

# 改用 yfinace 模組
# 使用 MSFT 指標測試
tmp = yf.download("MSFT")
tmp # Open, High, Low, Close, Adj Close, Volume

stk_data = yf.download(stk_tickers)
stk_data

type(stk_data) # pandas.core.frame.DataFrame

# DataFrame with MultiIndex (多重指標)
# 欄位名稱
stk_data.columns

type(stk_data.columns) # pandas.core.indexes.multi.MultiIndex

stk_data.index # DatetimeIndex with datetime64

type(stk_data.index) # pandas.core.indexes.datetimes.DatetimeIndex

# 篩選研究日期範圍
mask = (stk_data.index >= start) & (stk_data.index <= end)
stk_data = stk_data.loc[mask]
stk_data # 3718*18

# 2.載入貨幣資料
ccy_data = web.DataReader(ccy_tickers, "fred", start, end)
ccy_data # 3851*2

# 3.載入指數資料
idx_data = web.DataReader(idx_tickers, "fred", start, end)
idx_data # 3855*3

# 在資料分析的心法中提及三大技巧: 1群組 2時間 3建立評變數.
# 本研究加入建立評估變,  其中 MSFT 的落後5日, 15日, 30日, 60日票平均報酬率為新增建立的評估變數

# 考慮一週的交易日數為5天, 設定5日的報酬基準
return_period = 5

# 取出 multiple index value
stk_data.loc[:, ('Adj Close', 'MSFT')]

# 計算 log 轉換與落後5日
# 2024年10月1,2,3,4,7,8,9,10日
# 2024年10月10日的5日差異=2024.10.10 - 2024.10.3
np.log(stk_data.loc[:, ('Adj Close', 'MSFT')]).diff(return_period)

# np.log 自然對數
# diff 計算落後5天報酬
# shift: 正數表示整列向下移動, 負數表示整列向上移動
Y = np.log(stk_data.loc[:, ('Adj Close', 'MSFT')]).diff(return_period).shift(-return_period)
Y.name = Y.name[-1]+'_pred'
Y

# pandas 序列(Series)物件
# https://github.com/rwepa/python_data_scientist/blob/main/2024-01.python_tutorial.py#L1112
type(Y) # pandas.core.series.Series

# X1: Google, IBM-5日股票報酬
X1 = np.log(stk_data.loc[:, ('Adj Close', ('GOOGL', 'IBM'))]).diff(return_period).dropna()
X1.columns = X1.columns.droplevel()
X1 # 3713*2

# X2: USD/JPY, GBP/USD 5日股票報酬
X2 = np.log(ccy_data).diff(return_period).dropna()
X2 #3546*2

# X3: S&P 500, Dow Jones, VTX 5日股票報酬 
X3 = np.log(idx_data).diff(return_period).dropna()
X3 # 2426*3

# <div class="alert alert-block alert-info">
# <b>注意: </b>使用資料分析的心法-建立評估變數X4.
# </div>

# X4: 將時間序列資料重新建構為基於監督式學習-迴歸模型架構
# pd.concat(..., axis=1) 表示行的左右合併
# for 迴圈表示依序針對{1週期日,3週期日,6週期日,12週期日}計算調整後收盤價的報酬.
# dropna() 表示刪除資料列中有任何一行為 nan 值.
X4 = pd.concat([np.log(stk_data.loc[:, ('Adj Close', 'MSFT')]).diff(i) for i in [return_period, return_period*3, return_period*6, return_period*12]], axis=1).dropna()

X4.columns = ['MSFT_DT', 'MSFT_3DT', 'MSFT_6DT', 'MSFT_12DT']
X4 # 3658*4

# <div class="alert alert-block alert-info">
# <b>注意: </b>本研究因為各資料集 index 資料型態不相同, 因此須先進行 pd.to_datetime() 資料轉換.
# </div>

# 將 X1, X2, X3, X4 執行資料行合併
# https://pandas.pydata.org/docs/reference/api/pandas.concat.html

# 因為 index 資料型態不相同, 因此直接合併會有錯誤.
# TypeError: Cannot join tz-naive with tz-aware DatetimeIndex
# X = pd.concat([X1, X2, X3, X4], axis=1)

# 理解各資料 index 資料型態
X1.index.dtype # datetime64[ns, UTC]

X2.index.dtype # dtype('<M8[ns]')

X3.index.dtype # dtype('<M8[ns]')

X4.index.dtype # datetime64[ns, UTC]

# 將 X2.index, X3.index 轉換為 datetime64[ns, UTC]
X2.index = pd.to_datetime(X2.index, utc=True)
X2.index.dtype # datetime64[ns, UTC]

X3.index = pd.to_datetime(X3.index, utc=True)
X3.index.dtype # datetime64[ns, UTC]

# 資料合併
X = pd.concat([X1, X2, X3, X4], axis=1).dropna()
X # 2368*11

# 合併 Y, X
dataset = pd.concat([Y, X], axis=1).dropna().iloc[::return_period, :]
dataset

# 反應變數
Y = dataset.loc[:, Y.name]
Y

# 自變數
X = dataset.loc[:, X.columns]
X

# ## 2.2 資料摘要

# 資料物件
type(dataset) # pandas.core.frame.DataFrame

# 資料型態
dataset.dtypes # 所有變數皆為 float64

# 資料摘要
pd.set_option('display.precision', 4)
dataset.describe(include='all')

# 反應變數: 
 
# MSFT_pred : 微軟週(5日)報酬率
 
# 自變數區分為三大屬性, 合計11個:
#
# 1.股票: 6個
# 
# 2.貨幣: 2個
# 
# 3.指數: 3個
# 
# **股票**
# 
# GOOGL   : Google報酬
# 
# IBM     : IBM報酬
# 
# MSFT_DT : 微軟落後5日報酬
# 
# MSFT_3DT: 微軟落後15日報酬
# 
# MSFT_6DT: 微軟落後30日報酬
# 
# MSFT_12DT: 微軟落後60日報酬
# 
# **貨幣**
# 
# DEXJPUS : USD/JPY 美元/日元匯率
# 
# DEXUSUK : GBP/USD 英鎊/美元匯率
# 
# **指數**
# 
# SP500   : 標準普爾500指數
# 
# DJIA    : 道瓊工業平均指數
# 
# VIXCLS  : 芝加哥選擇權交易所市場波動率指數(波動率指數)

# ## 2.3 探索性資料分析(Exploratory Data Analysis, EDA)

# 資料列數與行數
dataset.shape

# 欄位名稱
dataset.columns

# 檢查 NA 值
dataset.isnull().sum() # 所有變數皆沒有NA值

# 顯示前5筆
dataset.head()

# 顯示後5筆
dataset.tail()

# ## 2.4 資料視覺化

# **相關係數矩陣(correlation coefficient matrix)**

# 計算相關係數
correlation = dataset.corr()
pyplot.figure(figsize=(10,10))
pyplot.title('Correlation Matrix')
sns.heatmap(correlation, vmax=1, square=True,annot=True,cmap='cubehelix')

# 上方相關係數圖顯示以下之特質:
# 
# + 反應變數 (MSFT_pred)與微軟落後5日, 15日, 30日, 60日報酬具有相關性.
# 
# + 波動率指數(VIX)與許多股票報酬率存在較高的負相關.

# **散佈圖矩陣(scatter plot matrix)**

scatter_matrix(dataset, figsize=(15,15))
pyplot.show()


# 上方散佈圖矩陣顯示以下之特質:
# 
# + 反應變數(MSFT_pred)與微軟落後15日, 30日, 60日報酬具有線性關係.
# 
# + 反應變數(MSFT_pred)與其他自變數無顯著線性關係.

# # 3.資料準備
# 
# + 資料準備主要工作是將資料隨機區分為二大類：訓練集（train dataset）與測試集（test dataset）為主。
# 
# + 時間序列值的順序很重要, 資料不可隨機區分, 可以採用任意樣本點做為區分依據.

# 設定測試集比例約 20%, 訓練集個數 = 474*0.8 ~ 379筆資料.
test_size = 0.2
train_size = int(len(X) * (1-test_size))
train_size

# 區分自變數訓練集, 測試集
X_train, X_test = X[0:train_size], X[train_size:len(X)]

# 自變數-訓練集
X_train

# 自變數-測試集
X_test

# 區分反應變數的訓練集與測試集
Y_train, Y_test = Y[0:train_size], Y[train_size:len(X)]

# 反應變數-訓練集
Y_train

# 反應變數-測試集
Y_test

# # 4.建立模型

# + 本研究使用 10折交叉驗證(10-fold cross validation, CV)來決定模型的超參數.
# 
# + 針對數值型預測採用均方誤差指標(mean squared error metric).

num_folds = 10
scoring = 'neg_mean_squared_error'


# 建立模型方法包括推論統計、機器學習、深度學習與生成式學習等方法。本研究使用監督式學習。
# 
# + LinearRegression: https://en.wikipedia.org/wiki/Linear_regression
# 
# + Lasso: https://en.wikipedia.org/wiki/Lasso_(statistics)
# 
# + ElasticNet: https://en.wikipedia.org/wiki/Elastic_net_regularization
# 
# + KNN (k-nearest neighbors algorithm): https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
# 
# + Decision Tree Regression: https://en.wikipedia.org/wiki/Decision_tree_learning
# 
# + SVR (Support Vector Regression): https://en.wikipedia.org/wiki/Support_vector_machine

# 設定模型清單
models = []
models.append(('LR', LinearRegression()))
models.append(('LASSO', Lasso()))
models.append(('EN', ElasticNet()))
models.append(('KNN', KNeighborsRegressor()))
models.append(('CART', DecisionTreeRegressor()))
models.append(('SVR', SVR()))
models

# 建立模型
names = []
kfold_results = []
test_results = []
train_results = []
for name, model in models:
    names.append(name)
    
    ## K Fold analysis:
    seed = 168
    kfold = KFold(n_splits=num_folds)
    #converted mean square error to positive. The lower the beter
    cv_results = -1* cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    kfold_results.append(cv_results)
    

    # Full Training period
    res = model.fit(X_train, Y_train)
    train_result = mean_squared_error(res.predict(X_train), Y_train)
    train_results.append(train_result)
    
    # Test results
    test_result = mean_squared_error(res.predict(X_test), Y_test)
    test_results.append(test_result)
    
    msg = "%s: %f (%f) %f %f" % (name, cv_results.mean(), cv_results.std(), train_result, test_result)
    print(msg)


# **使用交叉驗證比較演算法**

kfold_results

fig = pyplot.figure()
fig.suptitle('Algorithm Comparison: Kfold results with K=10')
ax = fig.add_subplot(111)
pyplot.boxplot(kfold_results)
ax.set_xticklabels(names)
fig.set_size_inches(15,8)
pyplot.show()

# 上方演算法比較圖顯示以下之特質:
# 
# + 儘管幾個模型的結果看起來不錯, 但線性迴歸和正規化迴歸（套索迴歸LASSO, 彈性網路 EN) 似乎表現最好.
# 
# + 結果顯示反應變數和自變數之間存在著線性關係.

# # 5.評估與測試

# **以下針對訓練集與測試集進行比較**

fig = pyplot.figure()
ind = np.arange(len(names)) # the x locations for the groups
width = 0.35 # the width of the bars
fig.suptitle("Algorithm Comparison for Test dataset")
ax = fig.add_subplot(111)
pyplot.bar(ind - width/2, train_results, width=width, label='Train Error')
pyplot.bar(ind + width/2, test_results, width=width, label='Test Error')
fig.set_size_inches(15,8)
pyplot.legend()
ax.set_xticks(ind)
ax.set_xticklabels(names)
pyplot.show()

# 訓練集與測試集的評估結果:
#     
# + 針對訓練集與測試集誤差, 線性模型具有較佳的表現.
# 
# + 決策樹迴歸法(CART)訓練資料過度擬合，並在測試集上產生非常高的誤差。

# # 6.佈署應用與結論

# **結論**
# 
# 1. 本研究已經完成使用監督式學習建立微軟股票報酬模型做為決策參考.
# 
# 2. 研究變數包括股票,貨幣與指數相關資料集.
# 
# 3. 資料採用網路擷取方式獲得.
# 
# 4. 結果顯示迴歸模型有較佳結果.

# **未來研究**
# 
# 未來研究主題可加入以下二個演算法:
# 
# 1. 時間序列應用 (Time series: https://en.wikipedia.org/wiki/Time_series)
# 
# 2. 深度學習-LSTM 應用 (LSTM: https://en.wikipedia.org/wiki/Long_short-term_memory)

# # 參考文獻
# 
# 1. Ming-Chang, Lee. (2024). RWEPA網站. https://rwepa.blogspot.com. Last accessed on October 10, 2024.
# 2. Python 3.13.0 Reference Documentation. (2024). https://docs.python.org/3/. Last accessed on October 10, 2024.
# 3. Tatsat, H., Puri, S., & Lookabaugh, B. (2020). Machine Learning and  Data  Science  Blueprints  for  Finance. In O’Reilly Media, Inc.

# end
