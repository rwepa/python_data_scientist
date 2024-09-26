"""
file     : 2024-02.machine_learning.py
title    : Day2 Python 機器學習
author   : Ming-Chang Lee
date     : 2024.09.26
email    : alan9956@gmail.com
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
"""

##############################
# 5天程式語言應用主題
##############################
# Day1 Python 語言簡介
# Day2 Python 機器學習 🌸
# Day3 資料探勘技術介紹
# Day4 Python程式應用實例
# Day5 大數據程式語言評量測驗與解析

##############################
# Day2 Python 機器學習
##############################

# 大綱
# 1.CRISP-DM 跨產業資料探勘標準作業流程
# 2.機器學習簡介
# 3.非監督式學習與監督式學習
# 4.監督式學習的評估
# 5.scikit-learnd 模組簡介

##############################
# 1.CRISP-DM 跨產業資料探勘標準作業流程
##############################

# https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining

# 跨產業資料探勘標準作業流程 (CRoss Industry Standard Process for Data Mining)
# CRISP-DM是於1990年起，由SPSS以及NCR兩大廠商在合作戴姆克萊斯勒-賓士(Daimler Benz)的
# 資料倉儲以及資料探勘過程中發展出來的。

# 步驟 1：商業理解

# 步驟 2：資料理解(摘要,敘述性統計分析,資料視覺化,資料清除,合併,特徵選擇,資料轉換)
#   + 資料轉換: 正規化(Normalization, L1, L2)
#       + L1: L1-norm is also known as least absolute deviations (LAD).
#       + L2: L2-norm is also known as least squares. 
#   + 標準化(Standardization)
#       + (0,1)標準化.
#       + 最小最大標準化(min-max normalization).
#       + Z-score標準化: 將任意資料轉換為趨近平均值為0, 標準差為1的分配.
#   + 標籤編碼 (Label encoding): YES轉換為1, NO轉換為0.
#   + 數值型資料轉換為類別型資料.
#   + 獨熱編碼 (One-hot encoding): X1轉換為 [1 0 0], X2轉換為 [0 1 0], X3轉換為 [0 0 1].

# 步驟 3：資料準備 
#   + 將資料隨機區分為二大類：訓練集(train dataset), 測試集(test dataset), 有的模型會加上驗證集.
#   + 訓練集: 訓練模型, 佔整體資料的70%
#   + 驗證集: 部分方法考慮區分驗證集 (validation dataset). 用於評估模型的初步判斷與超參數調整.
#             如果模型不具有超參數, 則不用區分此驗證集. 超參數: 例如類神經網路中隱藏單元的數量.
#   + 測試集: 評估模型, 佔整體資料的30%

# 區分比例範例1: 訓練集 70%, 測試集 30%
# 區分比例範例2: 訓練集 80%, 測試集 20%
# 區分比例範例3: 訓練集 80%, 驗證集 10%, 測試集 10%

# k 折交叉驗證 (k-fold cross validation)
# k-fold 劃分方法可以降低數據劃分帶來的影響.
# 將資料區分成 k 份，每次使用 (k-1) 做為訓練集, 另1份做為測試集，計算 k 次的平均交叉驗證準確度
# 並做為模型評估的指標. 一般可以使用 k = 10.

# 步驟 4：模式建立    (使用訓練集)

# 步驟 5：評估與測試  (使用測試集)

# 步驟 6：佈署應用

##############################
# 2.機器學習簡介
##############################

# 機器學習是人工智慧的一個分支.

# 人工智慧的研究歷史: 推理 --> 知識 --> 學習.

# 機器學習是實現人工智慧的一個方法,即是以機器學習為手段解決人工智慧中的問題.

# 機器學習在近30多年已發展為一門多領域交叉學科,涉及機率論,統計學,近似理論,凸分析(最佳化問題),
# 計算複雜性理論等多門學科.

# 機器學習理論主要是設計和分析一些讓電腦可以自動「學習」的演算法.

# 機器學習演算法是一類從資料中自動分析獲得規律,並利用規律對未知資料進行預測的演算法.

# 因為學習演算法中涉及了大量的統計學理論,機器學習與推論統計學關係密切,也被稱為統計學習理論.

# 人工智慧 --> 統計學習 --> 資料探勘 --> 機器學習 (預測+演算法) --> 深度學習 --> 生成式AI

# 常用機器學習包括非監督式學習與監督式學習.

##############################
# 2.非監督式學習與監督式學習
##############################

# 非監督式學習 (unsupervised learning) 又稱為無監督學習, 是機器學習的一種方法,
# 沒有給定事先標記過的訓練範例(Y), 自動對輸入的資料進行分群.

# 非監督學習的主要運用包含:
#   + 集群分析 (cluster analysis)
#   + 關聯規則 (association rule)
#   + 維度縮減 (dimensionality reduce). 例: 主成分分析 (Principal Aomponents Analysis, PCA)

##############################
# 3.監督式學習
##############################

# 監督式學習 (supervised learning): 已知 Y(人為標註的結果, 表示標籤), 進行 X --> 預測 --> Y

# X: 自變數, 獨立變數 independent variable, 預測變量 predictor variable, 
#    解釋變量 explanatory variable, 共變量 covariate.
# Y: 反應變數 response variable, 因變數, 依變數, 應變數, 被解釋變數 dependent variable, 
#    結果變數 outcome variable.

# 迴歸分析 Regression analysis
# 廣義線性模型 General linear model (GLM): 適用於Y為類別型變數或發生次數變數.
# 決策樹 Decision tree
# 天真貝氏法 Naïve-Bayes
# K近鄰法 k-nearest neighbors (KNN)
# 支持向量機 Support vector machine (SVM)
# 隨機森林法 Random forest
# 類神經網路 Neural network (NN)

# 集成學習 (Ensemble learning): 使用多種學習算演算法來獲得比使用單一演算法更好預測結果.
#   Bagging (Bootstrap AGGregatING) 裝袋法 (拔靴集成法)
#   Boosting 提升法
#   XGBoost (eXtreme Gradient Boosting) 極端梯度提升法

##############################
# 4.監督式學習的評估
##############################

# 數值模型常用績效指標:
# 1.均方誤差 (Mean Squared Error, MSE) # https://en.wikipedia.org/wiki/Mean_squared_error
# 2.均方根誤差 (Root Mean Squared Error, RMSE)
# 3.平均絕對誤差 (Mean Absolute Error, MAE)

# 類別模型績效指標
# http://rwepa.blogspot.com/2013/01/rocr-roc-curve.html
# 理解淆矩陣 (Confusion matrix)

##############################
# 5.scikit-learnd 模組簡介
##############################

# Scikit-learn 是使用 Python 程式語言撰寫的自由並開源的機器學習框架之一
# 提供豐富的機器學習演算法和工具，讓使用者可以方便地進行數據分析和建立模型。
# 在機器學習流程中，經常需要進行資料前處理、特徵選擇和模型選擇等一系列步驟皆包括在 Scikit-learn。
# Scikit-learn 與其他 Python 模組可以進行方便使用，例: 
#   + 繪圖      matplotlib, plotly
#   + 陣列計算  numpy
#   + 資料框    pandas
#   + 科學計算  scipy 

# scikit-learn 官網
# https://scikit-learn.org/stable/

# 六大功能
# 1.Classification           分類
# 2.Regression               迴歸
# 3.Clustering               集群
# 4.Dimensionality reduction 維度縮減
# 5.Model selection          模型選取
# 6.Preprocessing            資料預處理

# 1.10.1. Classification
# https://scikit-learn.org/stable/modules/tree.html#classification

# 範例: scikit-learn - iris 決策樹

# 載入模組
from sklearn.model_selection import train_test_split # 訓練集,測試集分割
from sklearn.datasets import load_iris # 載入 iris 資料集
from sklearn.tree import DecisionTreeClassifier # 載入決策樹
from sklearn import tree # 載樹
from matplotlib import pyplot as plt # 載入繪圖

# 載入資料
iris = load_iris()

# 物件型態
type(iris) # sklearn.utils._bunch.Bunch

# 設定自變數 X
X = iris.data

# 設定反應變數 y
y = iris.target

# 訓練集,測試集分割
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# 建立決策樹框架
clf = DecisionTreeClassifier(max_leaf_nodes=5, random_state=0)

# 建立決策樹模型
clf.fit(X_train, y_train)

# 設定繪圖反應變數的標記
class_names = iris["target_names"]

# 設定繪圖大小-英吋
plt.figure(figsize=(12, 12))

# 繪製決策樹視覺化
tree.plot_tree(clf, fontsize=6, class_names=class_names)

# 儲存決策樹
plt.savefig("iris_decision_tree.png", dpi=300)

plt.savefig('iris_decision_tree.pdf', dpi=300)
# end
