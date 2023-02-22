# Python_urllib_toOpenData
[python] 使用內建urllib函式庫 透過政府公開資訊的api 下載資料存至txt檔

## 資料來源 
[臺北市資料大平台](https://data.taipei/)  
[臺北市內湖科技園區廠商名錄的API資料](https://data.taipei/dataset/detail?id=15c3e1ae-899b-466c-a536-208497e3a369)  
請開啟網頁後至下方複製API網址 (因為資料網址可能會有異動)

## Code 說明
* import 函式庫 
urllib 用來從URLs (Uniform Resource Locators) 取得資料的Python模組
json 模組用來解析獲取的json資料
```
import urllib.request as request
import json
```

* 獲取api資訊 (自url獲取資訊並使用json解析)
```
# 如需取前1000筆資料 在網址最後面加上參數即可 &limit=1000
with request.urlopen("https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire") as response:
    json_data = json.load(response)
```

* 寫入txt 檔案 (檔案不需要先建立)
範本
```
with open("檔案名稱",mode="w",encoding="utf-8") as file:
  file.write("寫入資料")
```
mode: r 讀取, w 寫入

```
# 開啟檔案
with open("data.txt",mode="w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")
```
\n 是換行的意思

## 課程資料來源
[Python 網路連線程式、公開資料串接 By 彭彭](https://www.youtube.com/watch?v=sUzR3QVBKIo)
