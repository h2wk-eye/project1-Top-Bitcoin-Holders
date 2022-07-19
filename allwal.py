import random
from time import sleep
import requests
from bs4 import BeautifulSoup
import csv
import json

headers = {
"Accept": "*/*",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
}

url = "https://bitinfocharts.com/top-100-richest-bitcoin-addresses.html"
with open(f"all_wallets.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(
        (
                'Place',
                'Wallet',
                'Balance_BTC',
                'Del_Week',
                'Del_Month',
                'Per_of_coins',
                'First_In',
                'Last_In',
                'First_Out',
                'Last_Out',
                'Ins',
                'Outs'
        )
    )
for i in range(1, 6):
    if i>1:
        url = "https://bitinfocharts.com/top-100-richest-bitcoin-addresses-" + str(i) + ".html"
    req = requests.get(url, headers = headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    wallets_all = soup.find_all(class_= "table-striped")
    all_a_dict = {}
    for item in wallets_all:
        half_tr = item.find_all("tr")
        all_tr = []
        for item2 in half_tr:
            all_tr.append(item2)
        for item3 in all_tr:
            wallet_tds = item3.find_all("td")
            try:
                a = wallet_tds[1].find("a").text.replace('.', '')
                b = wallet_tds[1].find("a").get("href")
                all_a_dict[a] = b
            except Exception:
                print('')
            try:
                place = wallet_tds[0].text
            except Exception:
                place = None
            try:
                Address = wallet_tds[1].find("a").text.replace('.', '')
            except Exception:
                Address = None
            try:
                Balance_BTC = wallet_tds[2].text.split(" ")[0]
                Balance_BTC = Balance_BTC.replace(",", "")
            except Exception:
                Balance_BTC = None
            try:
                Del_Week = wallet_tds[2].find_all("span")[1].text.split(" ")[0]
                Del_Week = Del_Week.replace("+", "")
            except Exception:
                Del_Week = None
            try:
                Del_Month = wallet_tds[2].find_all("span")[2].text.split(" ")[0]
                Del_Month = Del_Month.replace("+", "")
            except Exception:
                Del_Month = None
            try:
                Per_of_coins = wallet_tds[3].text.split("%")[0]
            except Exception:
                Per_of_coins = None
            try:
                First_In = wallet_tds[4].text[0:19]
            except Exception:
                First_In = None
            try:
                Last_In = wallet_tds[5].text[0:19]
            except Exception:
                Last_In = None
            try:
                First_Out = wallet_tds[7].text[0:19]
            except Exception:
                First_Out = None
            try:
                Last_Out = wallet_tds[8].text[0:19]
            except Exception:
                Last_Out = None
            try:
                Ins = wallet_tds[6].text
            except Exception:
                Ins = None
            try:
                Outs = wallet_tds[9].text
            except Exception:
                Outs = None
            with open(f"all_wallets.csv", "a", encoding = "utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                (
                place,
                Address,
                Balance_BTC,
                Del_Week,
                Del_Month,
                Per_of_coins,
                First_In,
                Last_In,
                First_Out,
                Last_Out,
                Ins,
                Outs
                ) )
    sleep(random.randrange(2, 4))
    with open ("all_a_dict.json", "a", encoding="utf-8") as file:
            json.dump(all_a_dict, file, indent= 4, ensure_ascii=False)
