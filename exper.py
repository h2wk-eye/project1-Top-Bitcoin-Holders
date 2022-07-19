# import requests
# import time
# from bs4 import BeautifulSoup
#
#
# # url = "https://bitinfocharts.com/bitcoin/address/3ETUmNhL2JuCFFVNSpk8Bqx2eorxyP9FVh"
# # #
# # headers = {
# #     "Accept": "*/*",
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
# # }
# # req = requests.get(url, headers=headers)
# # src = req.text
# # with open("index1.html", "w", encoding="utf-8") as file:
# #     file.write(src)
# with open("index1.html", encoding="utf-8") as file:
#     src = file.read()
# soup = BeautifulSoup(src, "lxml")
#
# a = soup.find("table", class_="abtb").find_all("tr")[2].find_all("td")
# for i in a:
#     print(i.text)
spoon= list("2022-06-0722:19:15UTC")
print(spoon)
spoon.insert(10, " ")
print(spoon)
