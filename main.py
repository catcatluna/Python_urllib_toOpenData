import urllib.request as request
import json
# 如需取前1000筆資料 在網址最後面加上參數即可 &limit=1000
with request.urlopen("https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire") as response:
    json_data = json.load(response)


# 將公司名稱列表
clist = json_data["result"]["results"]
# 開啟檔案
with open("data.txt",mode="w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")


