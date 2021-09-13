import requests as req

requesturl = "https://zipcloud.ibsnet.co.jp/api/search"
code = str(input("郵便番号(7桁の数字):  "))
input_code = f"{requesturl}?zipcode={code}"

url = req.get(input_code).json()["results"]

post1 = url[0]["address1"]
post2 = url[0]["address2"]
post3 = url[0]["address3"]

final = f"検索結果 ({post1}の{post2}{post3}です) "

print(final)
