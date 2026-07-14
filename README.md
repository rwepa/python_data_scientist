# Python 資料科學家

## 主題: Python與人工智慧實務應用工作坊

+ 單位：教育部產學連結執行辦公室-國立臺北科技大學

+ 日期：2026/07/23,24,25

+ 大綱:

  + Day 1 Python 與資料分析基礎

  + Day 2 機器學習應用

  + Day 3 Streamlit App 開發應用

+ 下載: https://github.com/rwepa/python_data_scientist/tree/main/tutorial_python_ai_app

+ PDF: https://github.com/rwepa/python_data_scientist/blob/main/tutorial_python_ai_app/python_ai_app.pdf

+ ipynb: https://github.com/rwepa/python_data_scientist/blob/main/tutorial_python_ai_app/python_ai_app.ipynb

## 如何將 python_ai.ipynb 轉換為 python_ai.pdf

+ 步驟1 先下載 TeX Live: 官網: https://tug.org/texlive/ (支援 Windows / MacOS / Linux 版本)

  + Windows 版本下載: https://mirror.ctan.org/systems/texlive/tlnet/install-tl-windows.exe

+ 步驟2 安裝 install-tl-windows.exe, 安裝目錄與選項保持預設值, 不可以修改. 注意: 安裝時間要很久 zzZZZ ....

![image](https://github.com/rwepa/python_data_scientist/blob/main/tutorial_python_ai_app/tex_live_install.png)

+ 步驟3 在 Anaconda Prompt 視窗輸入: **jupyter nbconvert python_ai.ipynb --to latex**

+ 步驟4 在上一個步驟執行完成會建立 python_ai.tex, 使用記事本開啟 python_ai.tex

+ 步驟5 在第5列空白處新增中文字型與網址自動換列處理:

    \usepackage{fontspec}
  
    \usepackage{xeCJK}

    \setCJKmainfont{Microsoft JhengHei}

    \usepackage{xurl}

+ 步驟6 在 \maketitle 之後預留一列空白列(第415列), 在第416列位置, 新增2列自動建立目錄與換頁符號, 如無目錄需求, 亦可省略.

    \tableofcontents

    \clearpage

+ 步驟7 關閉修正完成的 python_ai.tex

+ 步驟8 在 Anaconda Prompt 視窗輸入: **xelatex python_ai.tex** 完成後會自動建立 python_ai.pdf, PDF檔案亦會建立PDF書籤.

## 2026.7.11 企鵝資料集-island預測

+ 檔名: penguins_prediction.py

+ 下載: https://github.com/rwepa/python_data_scientist/blob/main/penguins_prediction.py

## 主題: Python程式語言財金應用

單位: 財團法人中華民國證券暨期貨市場發展基金會/國立臺中科技大學

日期: 2024/09/19~2024/10/24

## Day1 Python 語言簡介

+ 大綱:

  1.RWEPA簡介

  2.資料分析暨視覺化的心法

  3.Python 簡介

  4.Anaconda 簡介

  5.資料型態與四大資料物件

  6.pandas 資料處理

+ pdf: https://github.com/rwepa/python_data_scientist/blob/main/2024-01.python_tutorial.pdf

+ python: https://github.com/rwepa/python_data_scientist/blob/main/2024-01.python_tutorial.py

## Day2 Python 機器學習

+ 大綱:

  1.CRISP-DM 跨產業資料探勘標準作業流程
  
  2.機器學習簡介
  
  3.非監督式學習與監督式學習
  
  4.監督式學習的評估
  
  5.scikit-learnd 模組簡介

+ python: https://github.com/rwepa/python_data_scientist/blob/main/2024-02.machine_learning.py

## Day3 資料探勘技術介紹

+ python: https://github.com/rwepa/python_data_scientist/blob/main/2024-03.data_mining.ipynb

## Day4 Python程式應用實例

+ **Tutorial-投資人投資組合-集群法應用(期末報告)**

下載: https://github.com/rwepa/python_data_scientist/blob/main/report_investor_portfolio/report_168_alan.ipynb

+ **Tutorial-股票預測(期末報告)**

下載: https://github.com/rwepa/python_data_scientist/blob/main/report_stock_prediction/report_stock_prediction.ipynb

+ **Tutorial-iris鳶尾花卉物種分類預測(決策樹)**

下載: https://github.com/rwepa/python_data_scientist/blob/main/tutorial_iris_decision_tree/iris_decisiion_tree.ipynb

決策樹模型視覺化: ![image](https://github.com/rwepa/python_data_scientist/blob/main/tutorial_iris_decision_tree/tree_cart.png)

決策樹文字模型: https://github.com/rwepa/python_data_scientist/blob/main/tutorial_iris_decision_tree/tree_cart.txt

+ **Tutorial - Open data - 臺北市立平均每生分攤經費資料分析**

下載: https://github.com/rwepa/python_data_scientist/blob/main/tutorial_taipei_student_funding/taipei_student_funding.ipynb

+ **Tutorial - 空氣品質指標(AQI)-集群法**

🌸YouTube 【中文字幕】：https://youtu.be/0UJbhVWDuI4
 
🌸程式碼下載: https://github.com/rwepa/python_data_scientist/blob/main/tutorial_air_quality_index/tutorial_air_quality_index.ipynb

🌸LINK: https://rwepa.blogspot.com/2025/03/python-aqi-application.html

+ **Tutorial - 螺旋槳性能最佳化-KNN填補法**

下載: https://github.com/rwepa/python_data_scientist/blob/main/tutorial_propeller_design_optimization/tutorial_propeller_design_optimization.ipynb

+ **Tutorial - 黃金價格預測-深度學習LSTM**

下載: https://github.com/rwepa/python_data_scientist/blob/main/tutorial_gold_prediction_lstm/tutorial_gold_prediction_lstm.ipynb

## Day5 大數據程式語言評量測驗與解析

+ 期末報告注意事項: https://github.com/rwepa/python_data_scientist/blob/main/report_readme.txt

## 參考資料

+ RWEPA: http://rwepa.blogspot.com/

+ Python 程式設計-李明昌 <免費電子書> http://rwepa.blogspot.com/2020/02/pythonprogramminglee.html

+ R入門資料分析與視覺化應用教學(付費) https://mastertalks.tw/products/r?ref=MCLEE

+ R商業預測與應用(付費) https://mastertalks.tw/products/r-2?ref=MCLEE

+ 辛苦啦,完成 Python 程式之旅 ~~
