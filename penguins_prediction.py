"""
File     : penguins_prediction.py
Title    : 企鵝資料集-island預測
Author   : Ming-Chang Lee
YouTube  : https://www.youtube.com/@alan9956
RWEPA    : http://rwepa.blogspot.tw/
GitHub   : https://github.com/rwepa
Email    : alan9956@gmail.com
"""

# AI提示詞: penguins.csv 機器學習 python 應用範例. 反應變數是 species.
# 目標: 熟悉 Spyder 之操作與監督式學習應用

# 載入模組
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 下載企鵝資料集
# https://github.com/rwepa/DataDemo/blob/master/penguins.csv

# 讀取資料
df = pd.read_csv("penguins.csv")
df # 344*8

# 刪除缺失值
df = df.dropna().copy()

# 建立各欄位專用 Encoder
species_encoder = LabelEncoder()
island_encoder = LabelEncoder()
sex_encoder = LabelEncoder()

# 執行變數轉換: 0, 1, 2,...
df["species"] = species_encoder.fit_transform(df["species"])
df["island"] = island_encoder.fit_transform(df["island"])
df["sex"] = sex_encoder.fit_transform(df["sex"])

# 特徵與標籤
X = df.drop("species", axis=1)
y = df["species"]

# 切分資料集
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=168,
    stratify=y
)

# 建立模型
model = DecisionTreeClassifier(random_state=123)

# 訓練
model.fit(X_train, y_train)

# 預測
y_pred = model.predict(X_test)

# 評估
print("Accuracy:", accuracy_score(y_test, y_pred)) # 正確率達97%

# 建立新資料預測
new_data = pd.DataFrame([{
    "island": island_encoder.transform(["Dream"])[0],
    "bill_length": 46.0,
    "bill_depth": 15.0,
    "flipper_length": 210,
    "body_mass": 5000,
    "sex": 0,
    "year": 2008
}])

# 新資料預測
prediction = model.predict(new_data)

# 顯示預測結果
print("Predicted species:", species_encoder.inverse_transform(prediction)[0])
# end
