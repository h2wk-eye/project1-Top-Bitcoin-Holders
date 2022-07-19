import random
from time import sleep
import requests
from bs4 import BeautifulSoup
import json
import csv

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
}
# url = "https://bitinfocharts.com/top-100-richest-bitcoin-addresses.html"
# for i in range(1,6):   # (1, 101)
#     if i > 1 :
#         url = "https://bitinfocharts.com/top-100-richest-bitcoin-addresses-" + str(i) + ".html"
#     req = requests.get(url, headers=headers)
#     src = req.text
#     with open("index.html", "w", encoding="utf-8") as file:
#         file.write(src)
#     with open("index.html", encoding="utf-8") as file:
#         src = file.read()
#     soup = BeautifulSoup(src, "lxml")
#
#     tables = soup.find_all(class_= "table-striped")
#     all_tr=[]
#     for item in tables:
#         half_tr= item.find_all("tr")
#         for i in half_tr:
#             all_tr.append(i)
#     all_tr.pop(0)
#     all_td = []
#     for item in all_tr:
#         td = item.find_all("td")
#         all_td.append(td[1])
#     all_a = []
#     for item in all_td:
#         a = all_a.append(item.find("a"))
#
#     all_a_dict = {}
#
#     for item in all_a:
#         item_text = item.text
#         item_href = item.get("href")
#         all_a_dict[item_text] = item_href
#     with open ("all_a_dict.json", "a", encoding="utf-8") as file:
#             json.dump(all_a_dict, file, indent= 4, ensure_ascii=False)

with open("all_a_dict.json") as file:
    all_links = json.load(file)

# with open(f"all_trans.csv", "w", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         (
#             "Wallet",
#             "Block",
#             "Time",
#             "Amount(BTC)",
#             "Amount(USD)",
#             "Balance(BTC)",
#             "Balance(USD)",
#             "Price"
#         )
#     )

for wallet, wallet_href in all_links.items():
    req = requests.get(url=wallet_href+"-full", headers=headers)
    src = req.text

    with open(f"data/{wallet}.html", "w") as file:
        file.write(src)

    with open(f"data/{wallet}.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    try:
        transacions_of_wallet = soup.find(class_="abtb").find("tbody").find_all("tr")
    except Exception:
        transacions_of_wallet = None
    try:
        for item in transacions_of_wallet:
            try:
                transaction_tds = item.find_all("td")
            except Exception:
                transaction_tds = None
            try:
                block = transaction_tds[0].find("a").text
            except Exception:
                block = None
            try:
                time = transaction_tds[1].text[0:19]
            except Exception:
                time = None
            try:
                amount_BTC = transaction_tds[2].text.split("BTC")[0].strip()
            except Exception:
                amount_BTC = None
            try:
                balance_BTC = transaction_tds[3].text.strip()
            except Exception:
                balance_BTC = None
            try:
                balance_USD = transaction_tds[4].text.split("@")[0].strip()
            except Exception:
                balance_USD = None
            try:
                price = transaction_tds[4].text.split("@")[1].strip()
            except Exception:
                price = None

            rep = [",", "BTC", "$", " ", "+"]
            for s in rep:
                try:
                    if s in amount_BTC:
                        amount_BTC = amount_BTC.replace(s, "")
                except Exception:
                    amount_BTC = None
                try:
                    if s in balance_BTC:
                        balance_BTC = balance_BTC.replace(s, "")
                except Exception:
                    balance_BTC = None
                try:
                    if s in balance_USD:
                        balance_USD = balance_USD.replace(s, "")
                except Exception:
                    balance_USD = None
                try:
                    if s in price:
                        price = price.replace(s, "")
                except Exception:
                    price = None
            try:
                amount_USD = float(amount_BTC)*float(price)
            except Exception:
                amount_USD = None

            if float(amount_BTC)>0.002 or float(amount_BTC)<-0.002:
                with open(f"all_trans.csv", "a", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        (
                            wallet,
                            block,
                            time,
                            amount_BTC,
                            amount_USD,
                            balance_BTC,
                            balance_USD,
                            price
                        )
                    )
    except Exception:
        print('No transactions')
    print(wallet)
    sleep(random.randrange(3, 6))
    # "34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo": "https://bitinfocharts.com/bitcoin/address/34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo",
    # "bc1qgdjqv0av3q56jvd82tkdjpy7gdp9ut8tlqmgrpmv24sq90ecnvqqjwvw97": "https://bitinfocharts.com/bitcoin/address/bc1qgdjqv0av3q56jvd82tkdjpy7gdp9ut8tlqmgrpmv24sq90ecnvqqjwvw97",
    # "1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ": "https://bitinfocharts.com/bitcoin/address/1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ",
    # "3LYJfcfHPXYJreMsASk2jkn69LWEYKzexb": "https://bitinfocharts.com/bitcoin/address/3LYJfcfHPXYJreMsASk2jkn69LWEYKzexb",
    # "3M219KR5vEneNb47ewrPfWyb5jQ2DjxRP6": "https://bitinfocharts.com/bitcoin/address/3M219KR5vEneNb47ewrPfWyb5jQ2DjxRP6",
    # "bc1qazcm763858nkj2dj986etajv6wquslv8uxwczt": "https://bitinfocharts.com/bitcoin/address/bc1qazcm763858nkj2dj986etajv6wquslv8uxwczt",
    # "37XuVSEpWW4trkfmvWzegTHQt7BdktSKUs": "https://bitinfocharts.com/bitcoin/address/37XuVSEpWW4trkfmvWzegTHQt7BdktSKUs",
    # "1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF": "https://bitinfocharts.com/bitcoin/address/1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF",
    # "3Kzh9qAqVWQhEsfQz7zEQL1EuSx5tyNLNS": "https://bitinfocharts.com/bitcoin/address/3Kzh9qAqVWQhEsfQz7zEQL1EuSx5tyNLNS",
    # "bc1qa5wkgaew2dkv56kfvj49j0av5nml45x9ek9hz6": "https://bitinfocharts.com/bitcoin/address/bc1qa5wkgaew2dkv56kfvj49j0av5nml45x9ek9hz6",
    # "bc1qd4ysezhmypwty5dnw7c8nqy5h5nxg0xqsvaefd0qn5kq32vwnwqqgv4rzr": "https://bitinfocharts.com/bitcoin/address/bc1qd4ysezhmypwty5dnw7c8nqy5h5nxg0xqsvaefd0qn5kq32vwnwqqgv4rzr",
    # "bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h": "https://bitinfocharts.com/bitcoin/address/bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h",
    # "1LdRcdxfbSnmCYYNdeYpUnztiYzVfBEQeC": "https://bitinfocharts.com/bitcoin/address/1LdRcdxfbSnmCYYNdeYpUnztiYzVfBEQeC",
    # "1AC4fMwgY8j9onSbXEWeH6Zan8QGMSdmtA": "https://bitinfocharts.com/bitcoin/address/1AC4fMwgY8j9onSbXEWeH6Zan8QGMSdmtA",
    # "3CkUo2ChW6ALJUrU2ugZPJMtisKMJKwz5M": "https://bitinfocharts.com/bitcoin/address/3CkUo2ChW6ALJUrU2ugZPJMtisKMJKwz5M",
    # "bc1qmxjefnuy06v345v6vhwpwt05dztztmx4g3y7wp": "https://bitinfocharts.com/bitcoin/address/bc1qmxjefnuy06v345v6vhwpwt05dztztmx4g3y7wp",
    # "1LruNZjwamWJXThX2Y8C2d47QqhAkkc5os": "https://bitinfocharts.com/bitcoin/address/1LruNZjwamWJXThX2Y8C2d47QqhAkkc5os",
    # "1HiCfvt2NMyoTdUtjBApabZFCd5myJWJzG": "https://bitinfocharts.com/bitcoin/address/1HiCfvt2NMyoTdUtjBApabZFCd5myJWJzG",
    # "3LQUu4v9z6KNch71j7kbj8GPeAGUo1FW6a": "https://bitinfocharts.com/bitcoin/address/3LQUu4v9z6KNch71j7kbj8GPeAGUo1FW6a",
    # "3LCGsSmfr24demGvriN4e3ft8wEcDuHFqh": "https://bitinfocharts.com/bitcoin/address/3LCGsSmfr24demGvriN4e3ft8wEcDuHFqh",
    # "bc1q7ydrtdn8z62xhslqyqtyt38mm4e2c4h3mxjkug": "https://bitinfocharts.com/bitcoin/address/bc1q7ydrtdn8z62xhslqyqtyt38mm4e2c4h3mxjkug",
    # "3JZq4atUahhuA9rLhXLMhhTo133J9rF97j": "https://bitinfocharts.com/bitcoin/address/3JZq4atUahhuA9rLhXLMhhTo133J9rF97j",
    # "38UmuUqPCrFmQo4khkomQwZ4VbY2nZMJ67": "https://bitinfocharts.com/bitcoin/address/38UmuUqPCrFmQo4khkomQwZ4VbY2nZMJ67",
    # "bc1qcdeadk07jkthules0yw9u9ue9pklvr608ez94jgwcf7h2ldzcg6qwxp9er": "https://bitinfocharts.com/bitcoin/address/bc1qcdeadk07jkthules0yw9u9ue9pklvr608ez94jgwcf7h2ldzcg6qwxp9er",
    # "12XqeqZRVkBDgmPLVY4ZC6Y4ruUUEug8Fx": "https://bitinfocharts.com/bitcoin/address/12XqeqZRVkBDgmPLVY4ZC6Y4ruUUEug8Fx",
    # "bc1qx9t2l3pyny2spqpqlye8svce70nppwtaxwdrp4": "https://bitinfocharts.com/bitcoin/address/bc1qx9t2l3pyny2spqpqlye8svce70nppwtaxwdrp4",
    # "3FHNBLobJnbCTFTVakh5TXmEneyf5PT61B": "https://bitinfocharts.com/bitcoin/address/3FHNBLobJnbCTFTVakh5TXmEneyf5PT61B",
    # "12ib7dApVFvg82TXKycWBNpN8kFyiAN1dr": "https://bitinfocharts.com/bitcoin/address/12ib7dApVFvg82TXKycWBNpN8kFyiAN1dr",
    # "385cR5DM96n1HvBDMzLHPYcw89fZAXULJP": "https://bitinfocharts.com/bitcoin/address/385cR5DM96n1HvBDMzLHPYcw89fZAXULJP",
    # "bc1qjysjfd9t9aspttpjqzv68k0ydpe7pvyd5vlyn37868473lell5tqkz456m": "https://bitinfocharts.com/bitcoin/address/bc1qjysjfd9t9aspttpjqzv68k0ydpe7pvyd5vlyn37868473lell5tqkz456m",
    # "12tkqA9xSoowkzoERHMWNKsTey55YEBqkv": "https://bitinfocharts.com/bitcoin/address/12tkqA9xSoowkzoERHMWNKsTey55YEBqkv",
    # "17MWdxfjPYP2PYhdy885QtihfbW181r1rn": "https://bitinfocharts.com/bitcoin/address/17MWdxfjPYP2PYhdy885QtihfbW181r1rn",
    # "1aXzEKiDJKzkPxTZy9zGc3y1nCDwDPub2": "https://bitinfocharts.com/bitcoin/address/1aXzEKiDJKzkPxTZy9zGc3y1nCDwDPub2",
    # "19D5J8c59P2bAkWKvxSYw8scD3KUNWoZ1C": "https://bitinfocharts.com/bitcoin/address/19D5J8c59P2bAkWKvxSYw8scD3KUNWoZ1C",
    # "3FupZp77ySr7jwoLYEJ9mwzJpvoNBXsBnE": "https://bitinfocharts.com/bitcoin/address/3FupZp77ySr7jwoLYEJ9mwzJpvoNBXsBnE",
    # "14m3sd9HCCFJW4LymahJCKMabAxTK4DAqW": "https://bitinfocharts.com/bitcoin/address/14m3sd9HCCFJW4LymahJCKMabAxTK4DAqW",
    # "1932eKraQ3Ad9MeNBHb14WFQbNrLaKeEpT": "https://bitinfocharts.com/bitcoin/address/1932eKraQ3Ad9MeNBHb14WFQbNrLaKeEpT",
    # "19r6sRMjuF5YnMPkohcD1fES8CdGGcpa9F": "https://bitinfocharts.com/bitcoin/address/19r6sRMjuF5YnMPkohcD1fES8CdGGcpa9F",
    # "bc1qtw30nantkrh7y5ue73gm4mmy0zezfqxug3psr94sd967qwg7f76scfmr9p": "https://bitinfocharts.com/bitcoin/address/bc1qtw30nantkrh7y5ue73gm4mmy0zezfqxug3psr94sd967qwg7f76scfmr9p",
    # "17rm2dvb439dZqyMe2d4D6AQJSgg6yeNRn": "https://bitinfocharts.com/bitcoin/address/17rm2dvb439dZqyMe2d4D6AQJSgg6yeNRn",
    # "bc1q4jchcr7nla277su5lpjzttxp3xg5j8wds5lcwg": "https://bitinfocharts.com/bitcoin/address/bc1q4jchcr7nla277su5lpjzttxp3xg5j8wds5lcwg",
    # "1PeizMg76Cf96nUQrYg8xuoZWLQozU5zGW": "https://bitinfocharts.com/bitcoin/address/1PeizMg76Cf96nUQrYg8xuoZWLQozU5zGW",
    # "3K5dmrkBMS8ZVgERMLwiw7PJuG8GWTbo8e": "https://bitinfocharts.com/bitcoin/address/3K5dmrkBMS8ZVgERMLwiw7PJuG8GWTbo8e",
    # "3EEDeu13ex19AqQBTZStVsAFy6j1gRwgWc": "https://bitinfocharts.com/bitcoin/address/3EEDeu13ex19AqQBTZStVsAFy6j1gRwgWc",
    # "3H5JTt42K7RmZtromfTSefcMEFMMe18pMD": "https://bitinfocharts.com/bitcoin/address/3H5JTt42K7RmZtromfTSefcMEFMMe18pMD",
    # "39gUvGynQ7Re3i15G3J2gp9DEB9LnLFPMN": "https://bitinfocharts.com/bitcoin/address/39gUvGynQ7Re3i15G3J2gp9DEB9LnLFPMN",
    # "3FpYfDGJSdkMAvZvCrwPHDqdmGqUkTsJys": "https://bitinfocharts.com/bitcoin/address/3FpYfDGJSdkMAvZvCrwPHDqdmGqUkTsJys",
    # "15pqaBHFwFEphRqmXAPbs3QRLLPB7e2uMb": "https://bitinfocharts.com/bitcoin/address/15pqaBHFwFEphRqmXAPbs3QRLLPB7e2uMb",
    # "34HpHYiyQwg69gFmCq2BGHjF1DZnZnBeBP": "https://bitinfocharts.com/bitcoin/address/34HpHYiyQwg69gFmCq2BGHjF1DZnZnBeBP",
    # "bc1q080rkmk3kj86pxvf5nkxecdrw6nrx3zzy9xl7q": "https://bitinfocharts.com/bitcoin/address/bc1q080rkmk3kj86pxvf5nkxecdrw6nrx3zzy9xl7q",
    # "1GR9qNz7zgtaW5HwwVpEJWMnGWhsbsieCG": "https://bitinfocharts.com/bitcoin/address/1GR9qNz7zgtaW5HwwVpEJWMnGWhsbsieCG",
    # "bc1qr4dl5wa7kl8yu792dceg9z5knl2gkn220lk7a9": "https://bitinfocharts.com/bitcoin/address/bc1qr4dl5wa7kl8yu792dceg9z5knl2gkn220lk7a9",
    # "1KUr81aewyTFUfnq4ZrpePZqXixd59ToNn": "https://bitinfocharts.com/bitcoin/address/1KUr81aewyTFUfnq4ZrpePZqXixd59ToNn",
    # "3BMEXqGpG4FxBA1KWhRFufXfSTRgzfDBhJ": "https://bitinfocharts.com/bitcoin/address/3BMEXqGpG4FxBA1KWhRFufXfSTRgzfDBhJ",
    # "3EMVdMehEq5SFipQ5UfbsfMsH223sSz9A9": "https://bitinfocharts.com/bitcoin/address/3EMVdMehEq5SFipQ5UfbsfMsH223sSz9A9",
    # "1MDq7zyLw6oKichbFiDDZ3aaK59byc6CT8": "https://bitinfocharts.com/bitcoin/address/1MDq7zyLw6oKichbFiDDZ3aaK59byc6CT8",
    # "3DVJfEsDTPkGDvqPCLC41X85L1B1DQWDyh": "https://bitinfocharts.com/bitcoin/address/3DVJfEsDTPkGDvqPCLC41X85L1B1DQWDyh",
    # "1KVpuCfhftkzJ67ZUegaMuaYey7qni7pPj": "https://bitinfocharts.com/bitcoin/address/1KVpuCfhftkzJ67ZUegaMuaYey7qni7pPj",
    # "1BZaYtmXka1y3Byi2yvXCDG92Tjz7ecwYj": "https://bitinfocharts.com/bitcoin/address/1BZaYtmXka1y3Byi2yvXCDG92Tjz7ecwYj",
    # "36rPiyFi4pZmnAyYbDTABqLN3WcWP6yJXS": "https://bitinfocharts.com/bitcoin/address/36rPiyFi4pZmnAyYbDTABqLN3WcWP6yJXS",
    # "bc1q4vxn43l44h30nkluqfxd9eckf45vr2awz38lwa": "https://bitinfocharts.com/bitcoin/address/bc1q4vxn43l44h30nkluqfxd9eckf45vr2awz38lwa",
    # "18saWjMCchDTGWunefuDJSWNdz4p6KtfBL": "https://bitinfocharts.com/bitcoin/address/18saWjMCchDTGWunefuDJSWNdz4p6KtfBL",
    # "1PL2cmmMLmGGDtqaSZJY8DR1iKJaziEPJv": "https://bitinfocharts.com/bitcoin/address/1PL2cmmMLmGGDtqaSZJY8DR1iKJaziEPJv",
    # "3HSMPBUuAPQf6CU5B3qa6fALrrZXswHaF1": "https://bitinfocharts.com/bitcoin/address/3HSMPBUuAPQf6CU5B3qa6fALrrZXswHaF1",
    # "3EKWP3ZviLXudcoAfzammYQKwaz2zJKwQW": "https://bitinfocharts.com/bitcoin/address/3EKWP3ZviLXudcoAfzammYQKwaz2zJKwQW",
    # "38gfemn6Ps54si7KeYZrPX3uLpiseuP7sX": "https://bitinfocharts.com/bitcoin/address/38gfemn6Ps54si7KeYZrPX3uLpiseuP7sX",
    # "1FZy7CPFA2UqqQJYUA1cG9KvdDFbSMBJYG": "https://bitinfocharts.com/bitcoin/address/1FZy7CPFA2UqqQJYUA1cG9KvdDFbSMBJYG",
    # "13nwifHUz5ZfHuQhk5ETJ4BhmqbuQdvTFp": "https://bitinfocharts.com/bitcoin/address/13nwifHUz5ZfHuQhk5ETJ4BhmqbuQdvTFp",
    # "bc1qw0pswznckx7s6tjmd2f5hrx4q6kc5nyrdxku50": "https://bitinfocharts.com/bitcoin/address/bc1qw0pswznckx7s6tjmd2f5hrx4q6kc5nyrdxku50",
    # "3GWUKxq55XsQ7rkzbxAgfSyf6KHp8Ljh3R": "https://bitinfocharts.com/bitcoin/address/3GWUKxq55XsQ7rkzbxAgfSyf6KHp8Ljh3R",
    # "1Cr7EjvS8C7gfarREHCvFhd9gT3r46pfLb": "https://bitinfocharts.com/bitcoin/address/1Cr7EjvS8C7gfarREHCvFhd9gT3r46pfLb",
    # "bc1qqn4q5yv7feltnsfwzxwm3fluryqqzhhp6457h6m4ytq7mauxlxgq872p5f": "https://bitinfocharts.com/bitcoin/address/bc1qqn4q5yv7feltnsfwzxwm3fluryqqzhhp6457h6m4ytq7mauxlxgq872p5f",
    # "35pgGeez3ou6ofrpjt8T7bvC9t6RrUK4p6": "https://bitinfocharts.com/bitcoin/address/35pgGeez3ou6ofrpjt8T7bvC9t6RrUK4p6",
    # "1F34duy2eeMz5mSrvFepVzy7Y1rBsnAyWC": "https://bitinfocharts.com/bitcoin/address/1F34duy2eeMz5mSrvFepVzy7Y1rBsnAyWC",
    # "bc1qud9pc3ne0e94cuyvea9eg97jwe7hjqczyw0g5wgza8xnwu6c4ewspeh3qs": "https://bitinfocharts.com/bitcoin/address/bc1qud9pc3ne0e94cuyvea9eg97jwe7hjqczyw0g5wgza8xnwu6c4ewspeh3qs",
    # "bc1qhd0r5kh3u9mhac7de58qd2rdfx4kkv84kpx302": "https://bitinfocharts.com/bitcoin/address/bc1qhd0r5kh3u9mhac7de58qd2rdfx4kkv84kpx302",
    # "bc1qjh0akslml59uuczddqu0y4p3vj64hg5mc94c40": "https://bitinfocharts.com/bitcoin/address/bc1qjh0akslml59uuczddqu0y4p3vj64hg5mc94c40",
    # "bc1qu5mhu0nghreufhrvp8rrnuftlmukjhdarw8hxscjmwxxpf7csqnsnpy60t": "https://bitinfocharts.com/bitcoin/address/bc1qu5mhu0nghreufhrvp8rrnuftlmukjhdarw8hxscjmwxxpf7csqnsnpy60t",
    # "1f1miYFQWTzdLiCBxtHHnNiW7WAWPUccr": "https://bitinfocharts.com/bitcoin/address/1f1miYFQWTzdLiCBxtHHnNiW7WAWPUccr",
    # "bc1qsxdxm0exqdsmnl9ejrz250xqxrxpxkgf5nhhtq": "https://bitinfocharts.com/bitcoin/address/bc1qsxdxm0exqdsmnl9ejrz250xqxrxpxkgf5nhhtq",
    # "bc1qtef0p08lputg4qazhx2md43ynhc9kp20pn297qnz68068d9z48asmemanj": "https://bitinfocharts.com/bitcoin/address/bc1qtef0p08lputg4qazhx2md43ynhc9kp20pn297qnz68068d9z48asmemanj",
    # "1BAFWQhH9pNkz3mZDQ1tWrtKkSHVCkc3fV": "https://bitinfocharts.com/bitcoin/address/1BAFWQhH9pNkz3mZDQ1tWrtKkSHVCkc3fV",
    # "bc1qe75775tzuvspl59cw77ycc472jl0sgue69x3up": "https://bitinfocharts.com/bitcoin/address/bc1qe75775tzuvspl59cw77ycc472jl0sgue69x3up",
    # "14YK4mzJGo5NKkNnmVJeuEAQftLt795Gec": "https://bitinfocharts.com/bitcoin/address/14YK4mzJGo5NKkNnmVJeuEAQftLt795Gec",
    # "1Ki3WTEEqTLPNsN5cGTsMkL2sJ4m5mdCXT": "https://bitinfocharts.com/bitcoin/address/1Ki3WTEEqTLPNsN5cGTsMkL2sJ4m5mdCXT",
    # "35WHp4Hid61peyH4tuhNunwRj2gtNB41Lo": "https://bitinfocharts.com/bitcoin/address/35WHp4Hid61peyH4tuhNunwRj2gtNB41Lo",
    # "1KbrSKrT3GeEruTuuYYUSQ35JwKbrAWJYm": "https://bitinfocharts.com/bitcoin/address/1KbrSKrT3GeEruTuuYYUSQ35JwKbrAWJYm",
    # "1P1iThxBH542Gmk1kZNXyji4E4iwpvSbrt": "https://bitinfocharts.com/bitcoin/address/1P1iThxBH542Gmk1kZNXyji4E4iwpvSbrt",
    # "12tLs9c9RsALt4ockxa1hB4iTCTSmxj2me": "https://bitinfocharts.com/bitcoin/address/12tLs9c9RsALt4ockxa1hB4iTCTSmxj2me",
    # "1ucXXZQSEf4zny2HRwAQKtVpkLPTUKRtt": "https://bitinfocharts.com/bitcoin/address/1ucXXZQSEf4zny2HRwAQKtVpkLPTUKRtt",
    # "1CPaziTqeEixPoSFtJxu74uDGbpEAotZom": "https://bitinfocharts.com/bitcoin/address/1CPaziTqeEixPoSFtJxu74uDGbpEAotZom",
    # "1LfV1tSt3KNyHpFJnAzrqsLFdeD2EvU1MK": "https://bitinfocharts.com/bitcoin/address/1LfV1tSt3KNyHpFJnAzrqsLFdeD2EvU1MK",
    # "bc1q5nfww5jn5k4ghg7dpa4gy85x7uu3l4g0m0re76": "https://bitinfocharts.com/bitcoin/address/bc1q5nfww5jn5k4ghg7dpa4gy85x7uu3l4g0m0re76",
    # "bc1qvy0sp8cdj3cv2wwh05scucxw6vxqpdlhfjvqn8": "https://bitinfocharts.com/bitcoin/address/bc1qvy0sp8cdj3cv2wwh05scucxw6vxqpdlhfjvqn8",
    # "bc1qm6q8tgml3cr9gpx63a5jqtj2dxlsyz4q3ghjlf": "https://bitinfocharts.com/bitcoin/address/bc1qm6q8tgml3cr9gpx63a5jqtj2dxlsyz4q3ghjlf",
    # "bc1q4srun4yspqem2pqgk47eq9jspcht3fmyrmfdeu": "https://bitinfocharts.com/bitcoin/address/bc1q4srun4yspqem2pqgk47eq9jspcht3fmyrmfdeu",
    # "bc1qe39l9l84sa44r9j2jjkgdc7p4ltj3sracd932k": "https://bitinfocharts.com/bitcoin/address/bc1qe39l9l84sa44r9j2jjkgdc7p4ltj3sracd932k",
    # "1EU2pMence1UfifCco2UHJCdoqorAtpT7": "https://bitinfocharts.com/bitcoin/address/1EU2pMence1UfifCco2UHJCdoqorAtpT7",
    # "bc1qlkdlchlylfdkspvevnlqqlmt4l222hwva2z3n7": "https://bitinfocharts.com/bitcoin/address/bc1qlkdlchlylfdkspvevnlqqlmt4l222hwva2z3n7",
    # "bc1qg6kqkkaexnxpvle8w3zy5j7w4k9uz5rqmrx5lw": "https://bitinfocharts.com/bitcoin/address/bc1qg6kqkkaexnxpvle8w3zy5j7w4k9uz5rqmrx5lw",
    # "bc1qqdykm85ycxjqjh5hrkwmewts02mm6ku5rlck3m": "https://bitinfocharts.com/bitcoin/address/bc1qqdykm85ycxjqjh5hrkwmewts02mm6ku5rlck3m",
    # "bc1qgc5h9vz0zp4cmlxuw0h6jgryetq08e4twen03f": "https://bitinfocharts.com/bitcoin/address/bc1qgc5h9vz0zp4cmlxuw0h6jgryetq08e4twen03f",
    # "bc1qxv55wuzz4qsfgss3uq2zwg5y88d7qv5hg67d2d": "https://bitinfocharts.com/bitcoin/address/bc1qxv55wuzz4qsfgss3uq2zwg5y88d7qv5hg67d2d",
    # "bc1qmjpguunz9lc7h6zf533wtjc70ync94ptnrjqmk": "https://bitinfocharts.com/bitcoin/address/bc1qmjpguunz9lc7h6zf533wtjc70ync94ptnrjqmk",
    # "bc1qyr9dsfyst3epqycghpxshfmgy8qfzadfhp8suk": "https://bitinfocharts.com/bitcoin/address/bc1qyr9dsfyst3epqycghpxshfmgy8qfzadfhp8suk",
    # "bc1q8qg2eazryu9as20k3hveuvz43thp200g7nw7qy": "https://bitinfocharts.com/bitcoin/address/bc1q8qg2eazryu9as20k3hveuvz43thp200g7nw7qy",
    # "bc1q4ffskt6879l4ewffrrflpykvphshl9la4q037h": "https://bitinfocharts.com/bitcoin/address/bc1q4ffskt6879l4ewffrrflpykvphshl9la4q037h",
    # "15ZQJagAa2iUCwpQXUUCZ4BfzFW5TAVyJj": "https://bitinfocharts.com/bitcoin/address/15ZQJagAa2iUCwpQXUUCZ4BfzFW5TAVyJj",
    # "12Gjyd3MMR7Dj2KwCxw71wwzZXVp2xy8nK": "https://bitinfocharts.com/bitcoin/address/12Gjyd3MMR7Dj2KwCxw71wwzZXVp2xy8nK",
    # "14KzHoS5dXbhy2kBevNKLz2ZMtjaqHkKWZ": "https://bitinfocharts.com/bitcoin/address/14KzHoS5dXbhy2kBevNKLz2ZMtjaqHkKWZ",
    # "1E1SKgxgYJFXzaLxgat2FNSnwWeKz1U15N": "https://bitinfocharts.com/bitcoin/address/1E1SKgxgYJFXzaLxgat2FNSnwWeKz1U15N",
    # "1C7u4Zqu6ZZRsiKsFMYVDvNLfCwsGrbeTq": "https://bitinfocharts.com/bitcoin/address/1C7u4Zqu6ZZRsiKsFMYVDvNLfCwsGrbeTq",
    # "17SAATrqavNbzmqBwqxzZc7rK6u9Rmi9hE": "https://bitinfocharts.com/bitcoin/address/17SAATrqavNbzmqBwqxzZc7rK6u9Rmi9hE",
    # "1Dt4Q2ofKUtHwvjN45tAUfikNBfJrDERcZ": "https://bitinfocharts.com/bitcoin/address/1Dt4Q2ofKUtHwvjN45tAUfikNBfJrDERcZ",
    # "13pTeUzSU4nwkM72hM6e8AcP2d8LudZBjc": "https://bitinfocharts.com/bitcoin/address/13pTeUzSU4nwkM72hM6e8AcP2d8LudZBjc",
    # "18oRfGoPpb6bkQdACnD6dVYWceeWURK5R6": "https://bitinfocharts.com/bitcoin/address/18oRfGoPpb6bkQdACnD6dVYWceeWURK5R6",
    # "1M9pAdfhGHtQkhGRijApWAkkrPCduvV6Zi": "https://bitinfocharts.com/bitcoin/address/1M9pAdfhGHtQkhGRijApWAkkrPCduvV6Zi",
    # "3265tcUcp8dBhBBwp4rKN3iyUptuHkzMq7": "https://bitinfocharts.com/bitcoin/address/3265tcUcp8dBhBBwp4rKN3iyUptuHkzMq7",
    # "1KLay1g7rZxAiotuDhGy5YizdXSpqkFxQ9": "https://bitinfocharts.com/bitcoin/address/1KLay1g7rZxAiotuDhGy5YizdXSpqkFxQ9",
    # "bc1qsm3kjcmp63jsuyrqh58kc6k4ydpactjy6r7a6f": "https://bitinfocharts.com/bitcoin/address/bc1qsm3kjcmp63jsuyrqh58kc6k4ydpactjy6r7a6f",
    # "1gvH7pGPrEBNjqmwYS8UDhjFQkyqkKCLE": "https://bitinfocharts.com/bitcoin/address/1gvH7pGPrEBNjqmwYS8UDhjFQkyqkKCLE",
    # "bc1qajh7jfy44sswutqlwj2tz9wcejpxrgflc8penw": "https://bitinfocharts.com/bitcoin/address/bc1qajh7jfy44sswutqlwj2tz9wcejpxrgflc8penw",
    # "1P9fAFAsSLRmMu2P7wZ5CXDPRfLSWTy9N8": "https://bitinfocharts.com/bitcoin/address/1P9fAFAsSLRmMu2P7wZ5CXDPRfLSWTy9N8",
    # "1HLvaTs3zR3oev9ya7Pzp3GB9Gqfg6XYJT": "https://bitinfocharts.com/bitcoin/address/1HLvaTs3zR3oev9ya7Pzp3GB9Gqfg6XYJT",
    # "3KiC6mvNu5GBPnxKhtHKS88Km3UWVxhWtx": "https://bitinfocharts.com/bitcoin/address/3KiC6mvNu5GBPnxKhtHKS88Km3UWVxhWtx",
    # "bc1qh4cpaydaqlzez8ekkasm3ygj4us7gwxsghh047": "https://bitinfocharts.com/bitcoin/address/bc1qh4cpaydaqlzez8ekkasm3ygj4us7gwxsghh047",
    # "bc1q78wmm8xnhveklsparpeq6drlg9wlq4lyahkqfp": "https://bitinfocharts.com/bitcoin/address/bc1q78wmm8xnhveklsparpeq6drlg9wlq4lyahkqfp",
    # "3DwVjwVeJa9Z5Pu15WHNfKcDxY5tFUGfdx": "https://bitinfocharts.com/bitcoin/address/3DwVjwVeJa9Z5Pu15WHNfKcDxY5tFUGfdx",
    # "1J1F3U7gHrCjsEsRimDJ3oYBiV24wA8FuV": "https://bitinfocharts.com/bitcoin/address/1J1F3U7gHrCjsEsRimDJ3oYBiV24wA8FuV",
    # "167ZWTT8n6s4ya8cGjqNNQjDwDGY31vmHg": "https://bitinfocharts.com/bitcoin/address/167ZWTT8n6s4ya8cGjqNNQjDwDGY31vmHg",
    # "bc1qvjl5g620lx8p0dv6amdma5f8gh0cv6dqq295a5": "https://bitinfocharts.com/bitcoin/address/bc1qvjl5g620lx8p0dv6amdma5f8gh0cv6dqq295a5",
    # "36NkTqCAApfRJBKicQaqrdKs29g6hyE4LS": "https://bitinfocharts.com/bitcoin/address/36NkTqCAApfRJBKicQaqrdKs29g6hyE4LS",
    # "bc1qhszrd0ef5we6mg3r7xgl05g8rx06xll8yrwmjh": "https://bitinfocharts.com/bitcoin/address/bc1qhszrd0ef5we6mg3r7xgl05g8rx06xll8yrwmjh",
    # "3ETUmNhL2JuCFFVNSpk8Bqx2eorxyP9FVh": "https://bitinfocharts.com/bitcoin/address/3ETUmNhL2JuCFFVNSpk8Bqx2eorxyP9FVh",
    # "187zSqAYwMKJAxWdWQ4fmp5DyT6G2NPgD7": "https://bitinfocharts.com/bitcoin/address/187zSqAYwMKJAxWdWQ4fmp5DyT6G2NPgD7",
    # "1FzyryYKneS4wTrKKZUyP3oJXkiyRsMYfr": "https://bitinfocharts.com/bitcoin/address/1FzyryYKneS4wTrKKZUyP3oJXkiyRsMYfr",
    # "bc1qdhvtwg0eealy5d2spua2a89sq05ydvtgjy4uau": "https://bitinfocharts.com/bitcoin/address/bc1qdhvtwg0eealy5d2spua2a89sq05ydvtgjy4uau",
    # "366koi4ZU7FyoyN3qXarLGMze8kFdq3Uh1": "https://bitinfocharts.com/bitcoin/address/366koi4ZU7FyoyN3qXarLGMze8kFdq3Uh1",
    # "1Le1X8LJb4VkFsfktiUY7V7wMRhniu5Xgn": "https://bitinfocharts.com/bitcoin/address/1Le1X8LJb4VkFsfktiUY7V7wMRhniu5Xgn",
    # "15URsTiy1ksoMMV7DuEi9hvSqHgqobAtKa": "https://bitinfocharts.com/bitcoin/address/15URsTiy1ksoMMV7DuEi9hvSqHgqobAtKa",
    # "16dyizLarM2N4UjGaEFPESNmJC5vEALtZX": "https://bitinfocharts.com/bitcoin/address/16dyizLarM2N4UjGaEFPESNmJC5vEALtZX",
    # "1BbSZNNhoBUCFGMfnscBDXf7PH1takoMga": "https://bitinfocharts.com/bitcoin/address/1BbSZNNhoBUCFGMfnscBDXf7PH1takoMga",
    # "1Gtpfqoo8stQw2E4vCbZZbJBBZvYzzCeRy": "https://bitinfocharts.com/bitcoin/address/1Gtpfqoo8stQw2E4vCbZZbJBBZvYzzCeRy",
    # "12yePmcVhMzzHYwh4BpVF3Cm1bYL9mqyKc": "https://bitinfocharts.com/bitcoin/address/12yePmcVhMzzHYwh4BpVF3Cm1bYL9mqyKc",
    # "1Fjom9b9wvp3HPi2ZS9hqXQwJpXcjumSYJ": "https://bitinfocharts.com/bitcoin/address/1Fjom9b9wvp3HPi2ZS9hqXQwJpXcjumSYJ",
    # "16BiUbH8yxFmCJs4ArtyTgHKfXQFvkvPNr": "https://bitinfocharts.com/bitcoin/address/16BiUbH8yxFmCJs4ArtyTgHKfXQFvkvPNr",
    # "1Eqj1APg1dkcPH7CmHJ6SzRwtJRLpxtBFA": "https://bitinfocharts.com/bitcoin/address/1Eqj1APg1dkcPH7CmHJ6SzRwtJRLpxtBFA",
    # "1QHVStz4ALAF8LFokjLy9QFaZKUFdraxeo": "https://bitinfocharts.com/bitcoin/address/1QHVStz4ALAF8LFokjLy9QFaZKUFdraxeo",
    # "19F4xZNBxtPAdMqFudr2LDH5efeeUYF21x": "https://bitinfocharts.com/bitcoin/address/19F4xZNBxtPAdMqFudr2LDH5efeeUYF21x",
    # "157ZXCYfK6NqBiFLkoLDt3PN8KyE8xdTu5": "https://bitinfocharts.com/bitcoin/address/157ZXCYfK6NqBiFLkoLDt3PN8KyE8xdTu5",
    # "1GcPTDtNXuPghJU5qSGvkPQ99nhWrbQaYR": "https://bitinfocharts.com/bitcoin/address/1GcPTDtNXuPghJU5qSGvkPQ99nhWrbQaYR",
    # "1GaSQcWg3R98qf5sTWetwjjMh6ehxj25Gp": "https://bitinfocharts.com/bitcoin/address/1GaSQcWg3R98qf5sTWetwjjMh6ehxj25Gp",
    # "1GBzbXJmcMjnDyTW2yKJFfeXUGicG1zpC4": "https://bitinfocharts.com/bitcoin/address/1GBzbXJmcMjnDyTW2yKJFfeXUGicG1zpC4",
    # "13TM7PLtf1Ujo9t9pk9RSyrv1ts119PNK5": "https://bitinfocharts.com/bitcoin/address/13TM7PLtf1Ujo9t9pk9RSyrv1ts119PNK5",
    # "1MH8s3qc4F2GZNod1R43qeysSB2ssZCXb": "https://bitinfocharts.com/bitcoin/address/1MH8s3qc4F2GZNod1R43qeysSB2ssZCXb",
    # "12T7nyMrAnd13UAMYCCJZ8Fw7PpMGPRFsi": "https://bitinfocharts.com/bitcoin/address/12T7nyMrAnd13UAMYCCJZ8Fw7PpMGPRFsi",
    # "1LjUYdf8mQk9DsrVvuPYeHyJKQq5V1MLsT": "https://bitinfocharts.com/bitcoin/address/1LjUYdf8mQk9DsrVvuPYeHyJKQq5V1MLsT",
    # "14ACC7ftHQS6guKJi3FCTEyCw94dHnRZjJ": "https://bitinfocharts.com/bitcoin/address/14ACC7ftHQS6guKJi3FCTEyCw94dHnRZjJ",
    # "13AiVabLoTcYTdaFcFYtpFFmCFagjiUwE2": "https://bitinfocharts.com/bitcoin/address/13AiVabLoTcYTdaFcFYtpFFmCFagjiUwE2",
    # "19yLTkx4jggSnjdiGkkhNwTjZUyY5T8kEA": "https://bitinfocharts.com/bitcoin/address/19yLTkx4jggSnjdiGkkhNwTjZUyY5T8kEA",
    # "1CsAkAsjTTRAuRw39fRQj7pxKn3fjEuYsT": "https://bitinfocharts.com/bitcoin/address/1CsAkAsjTTRAuRw39fRQj7pxKn3fjEuYsT",
    # "18zuLTKQnLjp987LdxuYvjekYnNAvXif2b": "https://bitinfocharts.com/bitcoin/address/18zuLTKQnLjp987LdxuYvjekYnNAvXif2b",
    # "bc1ql33jue567zn2v59ycgnd63vdu9y9lsc3xy4xx9": "https://bitinfocharts.com/bitcoin/address/bc1ql33jue567zn2v59ycgnd63vdu9y9lsc3xy4xx9",
    # "3B1HV46gEobDSpS5uXkUqtuLEPZiEAHCws": "https://bitinfocharts.com/bitcoin/address/3B1HV46gEobDSpS5uXkUqtuLEPZiEAHCws",
    # "3PWn1AGqo8HWH8mXSsxx1Ytk87zMAAziFU": "https://bitinfocharts.com/bitcoin/address/3PWn1AGqo8HWH8mXSsxx1Ytk87zMAAziFU",
    # "198aMn6ZYAczwrE5NvNTUMyJ5qkfy4g3Hi": "https://bitinfocharts.com/bitcoin/address/198aMn6ZYAczwrE5NvNTUMyJ5qkfy4g3Hi",
    # "18f6y4uWnLd7VPzfR2c1dMboihghXYHRH3": "https://bitinfocharts.com/bitcoin/address/18f6y4uWnLd7VPzfR2c1dMboihghXYHRH3",
    # "1Lan1sQzYGViDZskUFmnitJvfejn2jYdNS": "https://bitinfocharts.com/bitcoin/address/1Lan1sQzYGViDZskUFmnitJvfejn2jYdNS",
    # "17RmGC3i2dASQai3mP9iJLX3ZD9TBm2YQV": "https://bitinfocharts.com/bitcoin/address/17RmGC3i2dASQai3mP9iJLX3ZD9TBm2YQV",
    # "15mxk4fKk9ggQ4fikNWKpasahsdXZNdVu2": "https://bitinfocharts.com/bitcoin/address/15mxk4fKk9ggQ4fikNWKpasahsdXZNdVu2",
    # "1Fn4FSiHFr9SgbQ3ccsybN9f3RF1omst4x": "https://bitinfocharts.com/bitcoin/address/1Fn4FSiHFr9SgbQ3ccsybN9f3RF1omst4x",
    # "1HGdi2AtuvBUcdTFe62sKd7ZAFzoG7iQLb": "https://bitinfocharts.com/bitcoin/address/1HGdi2AtuvBUcdTFe62sKd7ZAFzoG7iQLb",
    # "1FDzP5vQGMhCzeb9nH4AcUDnUbcHS22BMZ": "https://bitinfocharts.com/bitcoin/address/1FDzP5vQGMhCzeb9nH4AcUDnUbcHS22BMZ",
    # "17J26KSDtNFPAUhCMwjcRNWhneMsXS75Ba": "https://bitinfocharts.com/bitcoin/address/17J26KSDtNFPAUhCMwjcRNWhneMsXS75Ba",
    # "12US3aeNibsxe7Lhascm4AmvGiTxwSdD4X": "https://bitinfocharts.com/bitcoin/address/12US3aeNibsxe7Lhascm4AmvGiTxwSdD4X",
    # "17GyU83L63BtxtpDgv8LmhhtmvcrXbfVt1": "https://bitinfocharts.com/bitcoin/address/17GyU83L63BtxtpDgv8LmhhtmvcrXbfVt1",
    # "1Dr1pZDgpowHDGJrUNTithDL33TdriFMzE": "https://bitinfocharts.com/bitcoin/address/1Dr1pZDgpowHDGJrUNTithDL33TdriFMzE",
    # "1N4yKFsFPjjoJyo3BAKUWpcs3SUghfgJkH": "https://bitinfocharts.com/bitcoin/address/1N4yKFsFPjjoJyo3BAKUWpcs3SUghfgJkH",
    # "16H2Fe9MgxZ1jXW3TaXbgWh3SJfwyxQUTp": "https://bitinfocharts.com/bitcoin/address/16H2Fe9MgxZ1jXW3TaXbgWh3SJfwyxQUTp",
    # "1KoiNofDvcUrrVfxgqpRZixWXNXo6d2kfQ": "https://bitinfocharts.com/bitcoin/address/1KoiNofDvcUrrVfxgqpRZixWXNXo6d2kfQ",
    # "1FMbcnYvvccZ6hR324cFRpn1QX9TCkqtAe": "https://bitinfocharts.com/bitcoin/address/1FMbcnYvvccZ6hR324cFRpn1QX9TCkqtAe",
    # "1LRXrhZRLVTjGCPFphPsXZfeHesRigm59r": "https://bitinfocharts.com/bitcoin/address/1LRXrhZRLVTjGCPFphPsXZfeHesRigm59r",
    # "15QFkJUWFZ6QRpTrzUitH2Egyf1JTngVgV": "https://bitinfocharts.com/bitcoin/address/15QFkJUWFZ6QRpTrzUitH2Egyf1JTngVgV",
    # "1DdxS8CheskxKAPPbG8Uq4Qts8kS4x1tt2": "https://bitinfocharts.com/bitcoin/address/1DdxS8CheskxKAPPbG8Uq4Qts8kS4x1tt2",
    # "1NJdKoBkKQNg6aYL9HTKyQ5SgfjZQDz3y3": "https://bitinfocharts.com/bitcoin/address/1NJdKoBkKQNg6aYL9HTKyQ5SgfjZQDz3y3",
    # "12mJZGPCWf5C2ap2dUdJiuGr8eWAvi6E5M": "https://bitinfocharts.com/bitcoin/address/12mJZGPCWf5C2ap2dUdJiuGr8eWAvi6E5M",
    # "1GBWcQuY5aD6e2zrbdb38j7pizVr2wcJnC": "https://bitinfocharts.com/bitcoin/address/1GBWcQuY5aD6e2zrbdb38j7pizVr2wcJnC",
    # "1T7m8nSs5Yh3YuLNoHPb5ehwN3LRVEchn": "https://bitinfocharts.com/bitcoin/address/1T7m8nSs5Yh3YuLNoHPb5ehwN3LRVEchn",
    # "1NQWCZqRYvANz3iX1Wnczpm277VEYvcAee": "https://bitinfocharts.com/bitcoin/address/1NQWCZqRYvANz3iX1Wnczpm277VEYvcAee",
    # "1HG6NbWmJjjSE1Z6oPetWG3nnKrQxgBN3a": "https://bitinfocharts.com/bitcoin/address/1HG6NbWmJjjSE1Z6oPetWG3nnKrQxgBN3a",
    # "1FrfmxAhYRNU9ebotDHP9FqLbe54QZVcfi": "https://bitinfocharts.com/bitcoin/address/1FrfmxAhYRNU9ebotDHP9FqLbe54QZVcfi",
    # "1FtHBKrYkDchMA1pwRTpYZ77TpfwSgh6iF": "https://bitinfocharts.com/bitcoin/address/1FtHBKrYkDchMA1pwRTpYZ77TpfwSgh6iF",
    # "1JeTiSWo8pYWcNaTH4c3CfheAwVDYRoy1Q": "https://bitinfocharts.com/bitcoin/address/1JeTiSWo8pYWcNaTH4c3CfheAwVDYRoy1Q",
    # "17wADqWPK8wZfpRmPkauviq2VDBmhm82rM": "https://bitinfocharts.com/bitcoin/address/17wADqWPK8wZfpRmPkauviq2VDBmhm82rM",
    # "1EUgoa25tkqMUYh7PXzDfqqNP5PtHKZmct": "https://bitinfocharts.com/bitcoin/address/1EUgoa25tkqMUYh7PXzDfqqNP5PtHKZmct",
    # "1AfHER73jneZAEAHNiz5dBKnrzeWcMJM5i": "https://bitinfocharts.com/bitcoin/address/1AfHER73jneZAEAHNiz5dBKnrzeWcMJM5i",
    # "1NJdqNoC7uPh7MqQhyEynRn9htstEELZDn": "https://bitinfocharts.com/bitcoin/address/1NJdqNoC7uPh7MqQhyEynRn9htstEELZDn",
    # "15TbabdR3FKJMpRxDeEetezWKGJwdGXbTY": "https://bitinfocharts.com/bitcoin/address/15TbabdR3FKJMpRxDeEetezWKGJwdGXbTY",
    # "1LuEe5Xkf1eA493SvsKwjPTS9RkW9JV9N2": "https://bitinfocharts.com/bitcoin/address/1LuEe5Xkf1eA493SvsKwjPTS9RkW9JV9N2",
    # "1Ja7G9JJRw8w8WWnMzw7PwYehhiZmhESkC": "https://bitinfocharts.com/bitcoin/address/1Ja7G9JJRw8w8WWnMzw7PwYehhiZmhESkC",
    # "1CptxmzfRyU2rF3VJ6q8wa2tkh3cm82p9P": "https://bitinfocharts.com/bitcoin/address/1CptxmzfRyU2rF3VJ6q8wa2tkh3cm82p9P",
    # "1PnsNtAqmHQKxyqKS843J9aegdJsXr5rpD": "https://bitinfocharts.com/bitcoin/address/1PnsNtAqmHQKxyqKS843J9aegdJsXr5rpD",
    # "1JnfbQerGjFHVq28945y1bhoUHpn6vKM9v": "https://bitinfocharts.com/bitcoin/address/1JnfbQerGjFHVq28945y1bhoUHpn6vKM9v",
    # "1AXskHt4ZwVZLonZV8BMDxh4V65ec41KMJ": "https://bitinfocharts.com/bitcoin/address/1AXskHt4ZwVZLonZV8BMDxh4V65ec41KMJ",
    # "1BcAtWddaU1jHWgQvM7dpM5SefoVgUHEuC": "https://bitinfocharts.com/bitcoin/address/1BcAtWddaU1jHWgQvM7dpM5SefoVgUHEuC",
    # "bc1qawmmv08vqqdtcmhym0hjhhmnkyad2twst0paqv": "https://bitinfocharts.com/bitcoin/address/bc1qawmmv08vqqdtcmhym0hjhhmnkyad2twst0paqv",
    # "33eU1zeB2S4x3p4ccSsnAChXcGJgtMrMtZ": "https://bitinfocharts.com/bitcoin/address/33eU1zeB2S4x3p4ccSsnAChXcGJgtMrMtZ",
    # "1BAuq7Vho2CEkVkUxbfU26LhwQjbCmWQkD": "https://bitinfocharts.com/bitcoin/address/1BAuq7Vho2CEkVkUxbfU26LhwQjbCmWQkD",
    # "15Z5YJaaNSxeynvr6uW6jQZLwq3n1Hu6RX": "https://bitinfocharts.com/bitcoin/address/15Z5YJaaNSxeynvr6uW6jQZLwq3n1Hu6RX",
    # "1B4U28Yc1JmSQbpzzSfavEskTPMvBRphyD": "https://bitinfocharts.com/bitcoin/address/1B4U28Yc1JmSQbpzzSfavEskTPMvBRphyD",
    # "34ovCavdkQgEYbrJk9Q1onhK7uWqq6J7DC": "https://bitinfocharts.com/bitcoin/address/34ovCavdkQgEYbrJk9Q1onhK7uWqq6J7DC",
    # "1L3Cqe4Zrk9EVUqE628Tumxo319argfXBX": "https://bitinfocharts.com/bitcoin/address/1L3Cqe4Zrk9EVUqE628Tumxo319argfXBX",
    # "1KHw7yzqoWto1DCGqn7QihoLmzbYWCqNcR": "https://bitinfocharts.com/bitcoin/address/1KHw7yzqoWto1DCGqn7QihoLmzbYWCqNcR",
    # "3A9qNS69dngSU2ak8BwZKEExeVnL2RqpYJ": "https://bitinfocharts.com/bitcoin/address/3A9qNS69dngSU2ak8BwZKEExeVnL2RqpYJ",
    # "14vbdGfYS7UKMvc4334UZDvTMPFA2G7zCB": "https://bitinfocharts.com/bitcoin/address/14vbdGfYS7UKMvc4334UZDvTMPFA2G7zCB",
    # "1K8QG4fuswaWFZ2fmmuxVKaWibi9H95iGw": "https://bitinfocharts.com/bitcoin/address/1K8QG4fuswaWFZ2fmmuxVKaWibi9H95iGw",
    # "1B1gTRphFdSx5MBRgKfh2SRbM6XhzEfVTX": "https://bitinfocharts.com/bitcoin/address/1B1gTRphFdSx5MBRgKfh2SRbM6XhzEfVTX",
    # "3HCdgNiAsjidcGx4eeMK9AXvXBfrnteunW": "https://bitinfocharts.com/bitcoin/address/3HCdgNiAsjidcGx4eeMK9AXvXBfrnteunW",
    # "36uUB2n49FnePNTojY6PhqusPmEmeqEb9b": "https://bitinfocharts.com/bitcoin/address/36uUB2n49FnePNTojY6PhqusPmEmeqEb9b",
    # "1DwSAnZw4Gk9FotgWZhRb3Nzqi4PLdU8M": "https://bitinfocharts.com/bitcoin/address/1DwSAnZw4Gk9FotgWZhRb3Nzqi4PLdU8M",
    # "1JECFWTZsRw65y65DEVR2djXv2KMYfuo7A": "https://bitinfocharts.com/bitcoin/address/1JECFWTZsRw65y65DEVR2djXv2KMYfuo7A",
    # "1JKDzFHcb6KBybKSquvMw1FrxXhvBdMiB5": "https://bitinfocharts.com/bitcoin/address/1JKDzFHcb6KBybKSquvMw1FrxXhvBdMiB5",
    # "1361wC48gW19mKAJmAkdXScLZKYdXgViS9": "https://bitinfocharts.com/bitcoin/address/1361wC48gW19mKAJmAkdXScLZKYdXgViS9",
    # "1Mt6STNGoHGuDziUSCagqTGNGrbDFSBxRn": "https://bitinfocharts.com/bitcoin/address/1Mt6STNGoHGuDziUSCagqTGNGrbDFSBxRn",
    # "3CsoguAb6Jz2dsSEYp8Mn4xJ34LC7fJz9g": "https://bitinfocharts.com/bitcoin/address/3CsoguAb6Jz2dsSEYp8Mn4xJ34LC7fJz9g",
    # "1M14kQL3zfyEAHx6JCM3gsZyAxyiSDMWdp": "https://bitinfocharts.com/bitcoin/address/1M14kQL3zfyEAHx6JCM3gsZyAxyiSDMWdp",
    # "bc1qk2q9ptkvfrtt3769hh85zvq88jyrulk6zgys2h": "https://bitinfocharts.com/bitcoin/address/bc1qk2q9ptkvfrtt3769hh85zvq88jyrulk6zgys2h",
    # "1FZcb6BU1ZbHQJcby7vDF2Na1z9UmkGSSG": "https://bitinfocharts.com/bitcoin/address/1FZcb6BU1ZbHQJcby7vDF2Na1z9UmkGSSG",
    # "19tiUa9nsPTgaqWNHaM9QyCfv4Wm9dVeYa": "https://bitinfocharts.com/bitcoin/address/19tiUa9nsPTgaqWNHaM9QyCfv4Wm9dVeYa",
    # "1JFUG5K3HidvfJD4R7nKyDJikmFpPcBB2": "https://bitinfocharts.com/bitcoin/address/1JFUG5K3HidvfJD4R7nKyDJikmFpPcBB2",
    # "1C1sUtw6fYa1Yr5wexrH2ayT1ZykD9Sobx": "https://bitinfocharts.com/bitcoin/address/1C1sUtw6fYa1Yr5wexrH2ayT1ZykD9Sobx",
    # "19RtRzXV5px91eMbWZFCWLZRUeQX5XxxnJ": "https://bitinfocharts.com/bitcoin/address/19RtRzXV5px91eMbWZFCWLZRUeQX5XxxnJ",
    # "1BTZe5up5x86LCV9T9kz3LQkKGzcotZjYq": "https://bitinfocharts.com/bitcoin/address/1BTZe5up5x86LCV9T9kz3LQkKGzcotZjYq",
    # "1JfXLzQvYPZHNzX4vhH6aoetGDfcPD1YEX": "https://bitinfocharts.com/bitcoin/address/1JfXLzQvYPZHNzX4vhH6aoetGDfcPD1YEX",
    # "bc1qms2la25qtgh69e7v8eddhsz3gwlfzucwh6v0zvwk8ku36r3mczxq4zlfd5": "https://bitinfocharts.com/bitcoin/address/bc1qms2la25qtgh69e7v8eddhsz3gwlfzucwh6v0zvwk8ku36r3mczxq4zlfd5",
    # "18SN8PV997oDGtYmTPPD55GDaPtNNEGWeu": "https://bitinfocharts.com/bitcoin/address/18SN8PV997oDGtYmTPPD55GDaPtNNEGWeu",
    # "35h49kvohPx5Pmtpt26P8o3KuSczsFLo23": "https://bitinfocharts.com/bitcoin/address/35h49kvohPx5Pmtpt26P8o3KuSczsFLo23",
    # "bc1qzk2pyxtahg64cx6gyq02vrw65fdxtpr253r4ygww9n2w2zjyy8wsnyc666": "https://bitinfocharts.com/bitcoin/address/bc1qzk2pyxtahg64cx6gyq02vrw65fdxtpr253r4ygww9n2w2zjyy8wsnyc666",
    # "13eEt6myAo1zAC7o7RK5sVxxCNCAgd6ApH": "https://bitinfocharts.com/bitcoin/address/13eEt6myAo1zAC7o7RK5sVxxCNCAgd6ApH",
    # "1DzjE3ANaKLasY2n6e5ToJ4CQCXrvDvwsf": "https://bitinfocharts.com/bitcoin/address/1DzjE3ANaKLasY2n6e5ToJ4CQCXrvDvwsf",
    # "15YMdTNT83UJqfpaZfDccy9yBYQFxHxVFt": "https://bitinfocharts.com/bitcoin/address/15YMdTNT83UJqfpaZfDccy9yBYQFxHxVFt",
    # "324rP14bzX8kW1JWt1J8ohZjDFyt2G68Kq": "https://bitinfocharts.com/bitcoin/address/324rP14bzX8kW1JWt1J8ohZjDFyt2G68Kq",
    # "1FJuzzQFVMbiMGw6JtcXefdD64amy7mSCF": "https://bitinfocharts.com/bitcoin/address/1FJuzzQFVMbiMGw6JtcXefdD64amy7mSCF",
    # "38C7LhtsbanuGUxeXguEvm2Gm2pSN2K175": "https://bitinfocharts.com/bitcoin/address/38C7LhtsbanuGUxeXguEvm2Gm2pSN2K175",
    # "1Ac6fUJ2Uw4cdXu3YFjCsSqnQGRb7KW1Ec": "https://bitinfocharts.com/bitcoin/address/1Ac6fUJ2Uw4cdXu3YFjCsSqnQGRb7KW1Ec",
    # "186XqVoL7TGxR3osoo4xn32wbYtb527raY": "https://bitinfocharts.com/bitcoin/address/186XqVoL7TGxR3osoo4xn32wbYtb527raY",
    # "19GEVekmu7wAgPFNcQNFHE7SYoj2snindR": "https://bitinfocharts.com/bitcoin/address/19GEVekmu7wAgPFNcQNFHE7SYoj2snindR",
    # "3QsGsAXQ4rqRNvh5pEW55hf3F9PEyb7rVq": "https://bitinfocharts.com/bitcoin/address/3QsGsAXQ4rqRNvh5pEW55hf3F9PEyb7rVq",
    # "bc1qzxwdcxqj36ane625hkgjpg6p0pjg79u29qyrus": "https://bitinfocharts.com/bitcoin/address/bc1qzxwdcxqj36ane625hkgjpg6p0pjg79u29qyrus",
    # "17EFzE9jRZqz72UEVzWV6syu1vvNgcsuVY": "https://bitinfocharts.com/bitcoin/address/17EFzE9jRZqz72UEVzWV6syu1vvNgcsuVY",
    # "1Ac2JdpQ5c9NeSajdGx6dofxeXkn4S35ft": "https://bitinfocharts.com/bitcoin/address/1Ac2JdpQ5c9NeSajdGx6dofxeXkn4S35ft",
    # "bc1qxseuqx06djpmyumvwn02lx3q082mmnj6r0g6zxc28rkypsevpfqs8vz7lr": "https://bitinfocharts.com/bitcoin/address/bc1qxseuqx06djpmyumvwn02lx3q082mmnj6r0g6zxc28rkypsevpfqs8vz7lr",
    # "19iqYbeATe4RxghQZJnYVFU4mjUUu76EA6": "https://bitinfocharts.com/bitcoin/address/19iqYbeATe4RxghQZJnYVFU4mjUUu76EA6",
    # "1LVBnipcnkwqHKaXcHeV9gcbPMvByaJkqk": "https://bitinfocharts.com/bitcoin/address/1LVBnipcnkwqHKaXcHeV9gcbPMvByaJkqk",
    # "1AYLzYN7SGu5FQLBTADBzqKm4b6Udt6Bw6": "https://bitinfocharts.com/bitcoin/address/1AYLzYN7SGu5FQLBTADBzqKm4b6Udt6Bw6",
    # "bc1qtq5zfllw9fs9w6stnfgalf9v59fgrcxxyawuvm": "https://bitinfocharts.com/bitcoin/address/bc1qtq5zfllw9fs9w6stnfgalf9v59fgrcxxyawuvm",
    # "1NpZcfBnaJeoRT9ZqwZVRMw3SRs546VsuE": "https://bitinfocharts.com/bitcoin/address/1NpZcfBnaJeoRT9ZqwZVRMw3SRs546VsuE",
    # "bc1qw8wrek2m7nlqldll66ajnwr9mh64syvkt67zlu": "https://bitinfocharts.com/bitcoin/address/bc1qw8wrek2m7nlqldll66ajnwr9mh64syvkt67zlu",
    # "3JsY8m7nG2K2siHXzqto612u36hAzF7C6X": "https://bitinfocharts.com/bitcoin/address/3JsY8m7nG2K2siHXzqto612u36hAzF7C6X",
    # "1JxmKkNK1b3p7r8DDPtnNmGeLZDcgPadJb": "https://bitinfocharts.com/bitcoin/address/1JxmKkNK1b3p7r8DDPtnNmGeLZDcgPadJb",
    # "bc1q94w3mwak5llpj4np7vj7luxuv8g6xn3my3vuas": "https://bitinfocharts.com/bitcoin/address/bc1q94w3mwak5llpj4np7vj7luxuv8g6xn3my3vuas",
    # "3QFtYbR22en2AizTb7JVFA9bL2rf1fbNJr": "https://bitinfocharts.com/bitcoin/address/3QFtYbR22en2AizTb7JVFA9bL2rf1fbNJr",
    # "bc1qz3m6agu2fsa9p6475xqk777axceyl07mhvwtrv80349mxyckelustuqyc7": "https://bitinfocharts.com/bitcoin/address/bc1qz3m6agu2fsa9p6475xqk777axceyl07mhvwtrv80349mxyckelustuqyc7",
    # "1LBBmkr9muf7RjjBbzQQvzNQpRRaVEnavs": "https://bitinfocharts.com/bitcoin/address/1LBBmkr9muf7RjjBbzQQvzNQpRRaVEnavs",
    # "1JdTWTAubsDWXWd7wcsFwMuSapMBh6efrQ": "https://bitinfocharts.com/bitcoin/address/1JdTWTAubsDWXWd7wcsFwMuSapMBh6efrQ",
    # "1EMQxNyqsSLkguWJsQmGTjwdL7YqbRVcVF": "https://bitinfocharts.com/bitcoin/address/1EMQxNyqsSLkguWJsQmGTjwdL7YqbRVcVF",
    # "3JPauiFhP4K3AevmgNMFfMSN7pLZbuADJQ": "https://bitinfocharts.com/bitcoin/address/3JPauiFhP4K3AevmgNMFfMSN7pLZbuADJQ",
    # "1J3B2ucUpWjWPPpejUCoLN93Gwz3q65CTd": "https://bitinfocharts.com/bitcoin/address/1J3B2ucUpWjWPPpejUCoLN93Gwz3q65CTd",
    # "138EMxwMtKuvCEUtm4qUfT2x344TSReyiT": "https://bitinfocharts.com/bitcoin/address/138EMxwMtKuvCEUtm4qUfT2x344TSReyiT",
    # "13n67sFKgqLDKp8gx8Xvm6scdfY4ZeaU8p": "https://bitinfocharts.com/bitcoin/address/13n67sFKgqLDKp8gx8Xvm6scdfY4ZeaU8p",
    # "1HKrGmgY5W2FyU6FZhbT2Jd4cyLxpDXPYo": "https://bitinfocharts.com/bitcoin/address/1HKrGmgY5W2FyU6FZhbT2Jd4cyLxpDXPYo",
    # "1JtAupan5MSPXxSsWFiwA79bY9LD2Ga1je": "https://bitinfocharts.com/bitcoin/address/1JtAupan5MSPXxSsWFiwA79bY9LD2Ga1je",
    # "3R2Hzkp1vKi5TNuLdUTiQphJQA6SKLa7zS": "https://bitinfocharts.com/bitcoin/address/3R2Hzkp1vKi5TNuLdUTiQphJQA6SKLa7zS",
    # "147sPaNaqeyQp8GS2oAUajhb9d4PZ9xAv9": "https://bitinfocharts.com/bitcoin/address/147sPaNaqeyQp8GS2oAUajhb9d4PZ9xAv9",
    # "18oP9DDaxKrC3XTMC2kZK1wLDGwUcky2oR": "https://bitinfocharts.com/bitcoin/address/18oP9DDaxKrC3XTMC2kZK1wLDGwUcky2oR",
    # "1DR93bfKVCUJkDvPuxbUAEtzYRaJEnwjNt": "https://bitinfocharts.com/bitcoin/address/1DR93bfKVCUJkDvPuxbUAEtzYRaJEnwjNt",
    # "1CCqLR8YrUMPFgYZWwLW8FkezbFjfeXD8n": "https://bitinfocharts.com/bitcoin/address/1CCqLR8YrUMPFgYZWwLW8FkezbFjfeXD8n",
    # "13Sscnm9MNVCLxLHCHm18dcmbroxDyN2X8": "https://bitinfocharts.com/bitcoin/address/13Sscnm9MNVCLxLHCHm18dcmbroxDyN2X8",
    # "bc1quv866t7ke929gxttpgc2u30ffnczpgfrjugwxv": "https://bitinfocharts.com/bitcoin/address/bc1quv866t7ke929gxttpgc2u30ffnczpgfrjugwxv",
    # "1F3Cpgben5uRAMptnPRL9coAbKp9YmWqfb": "https://bitinfocharts.com/bitcoin/address/1F3Cpgben5uRAMptnPRL9coAbKp9YmWqfb",
    # "356Zz26iW3tYd1xWJjVGa8CPbjC9W5EW9f": "https://bitinfocharts.com/bitcoin/address/356Zz26iW3tYd1xWJjVGa8CPbjC9W5EW9f",
    # "3ANziRvoBdNGkmGopgyhvzPuBvcL8sRL7S": "https://bitinfocharts.com/bitcoin/address/3ANziRvoBdNGkmGopgyhvzPuBvcL8sRL7S",
    # "bc1qrj8jwwea530rx00ldc22w8mnaclae4m54e6tgy": "https://bitinfocharts.com/bitcoin/address/bc1qrj8jwwea530rx00ldc22w8mnaclae4m54e6tgy",
    # "19VBqLkbMywnX5QMUg7LsHgbzsLh9as4MS": "https://bitinfocharts.com/bitcoin/address/19VBqLkbMywnX5QMUg7LsHgbzsLh9as4MS",
    # "34Y5ZSnrqjtMHEr4aqQB16Nng8hqpyf7ne": "https://bitinfocharts.com/bitcoin/address/34Y5ZSnrqjtMHEr4aqQB16Nng8hqpyf7ne",
    # "3HroDXv8hmzKRtaSfBffRgedKpru8fgy6M": "https://bitinfocharts.com/bitcoin/address/3HroDXv8hmzKRtaSfBffRgedKpru8fgy6M",
    # "bc1qyd2k46lzcrt3cd3z0nrt9d99z6xnzvyn2r83a5z9xfg8adpyp0ss53fnz4": "https://bitinfocharts.com/bitcoin/address/bc1qyd2k46lzcrt3cd3z0nrt9d99z6xnzvyn2r83a5z9xfg8adpyp0ss53fnz4",
    # "3H3b3kxRwoKDnJbdV2JdhJ5h7iPsHgFN4B": "https://bitinfocharts.com/bitcoin/address/3H3b3kxRwoKDnJbdV2JdhJ5h7iPsHgFN4B",
    # "34Knfd3NYNomfaCTzMbL5mAcYHuMFwWP7Y": "https://bitinfocharts.com/bitcoin/address/34Knfd3NYNomfaCTzMbL5mAcYHuMFwWP7Y",
    # "1BVtDi7txPCG2TH5Crd2Rw5MtpivbmoKgB": "https://bitinfocharts.com/bitcoin/address/1BVtDi7txPCG2TH5Crd2Rw5MtpivbmoKgB",
    # "1Kr6QSydW9bFQG1mXiPNNu6WpJGmUa9i1g": "https://bitinfocharts.com/bitcoin/address/1Kr6QSydW9bFQG1mXiPNNu6WpJGmUa9i1g",
    # "3HNP2s6EE3GRe6bU7wwVhCAUyMucKh8Yzp": "https://bitinfocharts.com/bitcoin/address/3HNP2s6EE3GRe6bU7wwVhCAUyMucKh8Yzp",
    # "3BMEXxSMT2b2kvsnC4Q35d2kKJZ4u9bSLh": "https://bitinfocharts.com/bitcoin/address/3BMEXxSMT2b2kvsnC4Q35d2kKJZ4u9bSLh",
    # "12CEGvJfHFCVGGUBTTA5yUaPHhchBPpuZK": "https://bitinfocharts.com/bitcoin/address/12CEGvJfHFCVGGUBTTA5yUaPHhchBPpuZK",
    # "3PdKaWwshFBWg6vAauToecqEAFtsuzyxGV": "https://bitinfocharts.com/bitcoin/address/3PdKaWwshFBWg6vAauToecqEAFtsuzyxGV",
    # "1BeouDc6jtHpitvPz3gR3LQnBGb7dKRrtC": "https://bitinfocharts.com/bitcoin/address/1BeouDc6jtHpitvPz3gR3LQnBGb7dKRrtC",
    # "15n6boxiQj45oHcmDjtNMjh35sFWZX4PBt": "https://bitinfocharts.com/bitcoin/address/15n6boxiQj45oHcmDjtNMjh35sFWZX4PBt",
    # "1ByHahn2PDryrcyRvbSnQQsUsqXDN3uXPb": "https://bitinfocharts.com/bitcoin/address/1ByHahn2PDryrcyRvbSnQQsUsqXDN3uXPb",
    # "3GTQBv5B4PVVRn1FqhkceoT8YLCFnVEWbo": "https://bitinfocharts.com/bitcoin/address/3GTQBv5B4PVVRn1FqhkceoT8YLCFnVEWbo",
    # "1ARWCREnmdKyHgNg2c9qih8UzRr4MMQEQS": "https://bitinfocharts.com/bitcoin/address/1ARWCREnmdKyHgNg2c9qih8UzRr4MMQEQS",
    # "18xGHNrU26w6HSCEL8DD5o1whfiDaYgp6i": "https://bitinfocharts.com/bitcoin/address/18xGHNrU26w6HSCEL8DD5o1whfiDaYgp6i",
    # "3JkfTdGnpNhK5xBjP6BzRsitZqnnVjQV1B": "https://bitinfocharts.com/bitcoin/address/3JkfTdGnpNhK5xBjP6BzRsitZqnnVjQV1B",
    # "bc1qlfmc6nv27d62s6zygjnjt6wm28klfh2gltg6ym": "https://bitinfocharts.com/bitcoin/address/bc1qlfmc6nv27d62s6zygjnjt6wm28klfh2gltg6ym",
    # "1LH1dY82QFtNGinBpCakU5WcTUKRyuztTz": "https://bitinfocharts.com/bitcoin/address/1LH1dY82QFtNGinBpCakU5WcTUKRyuztTz",
    # "16Jka2DrvEGGJ6ks2kXRpxmQZLQmAFRoGk": "https://bitinfocharts.com/bitcoin/address/16Jka2DrvEGGJ6ks2kXRpxmQZLQmAFRoGk",
    # "1NQEV6T4avmPqUVTvgsKkeB6yc8qnSWfhR": "https://bitinfocharts.com/bitcoin/address/1NQEV6T4avmPqUVTvgsKkeB6yc8qnSWfhR",
    # "19z6WynrjHeD5MMv6919BuQRwybuen1sRv": "https://bitinfocharts.com/bitcoin/address/19z6WynrjHeD5MMv6919BuQRwybuen1sRv",
    # "14RKFqH45xYPMpW4KQ28RB6XtrZ8XpEM5i": "https://bitinfocharts.com/bitcoin/address/14RKFqH45xYPMpW4KQ28RB6XtrZ8XpEM5i",
    # "1DaCQDfStUgkPQXcf53Teeo6LPiKcVMBM9": "https://bitinfocharts.com/bitcoin/address/1DaCQDfStUgkPQXcf53Teeo6LPiKcVMBM9",
    # "1NJQZhzYac89fDhQCmb1khdjekKNVYLFMY": "https://bitinfocharts.com/bitcoin/address/1NJQZhzYac89fDhQCmb1khdjekKNVYLFMY",
    # "bc1q3nkt8j6rphj6ry7jynanqn8j82f9d5fxkan659": "https://bitinfocharts.com/bitcoin/address/bc1q3nkt8j6rphj6ry7jynanqn8j82f9d5fxkan659",
    # "12ytiN9oWQTRGb6JjZiaoWMAvF9nPWdGX1": "https://bitinfocharts.com/bitcoin/address/12ytiN9oWQTRGb6JjZiaoWMAvF9nPWdGX1",
    # "bc1qdxsg7cfsqrg8sq3cs8ptsafqs6drtyuxswrqga": "https://bitinfocharts.com/bitcoin/address/bc1qdxsg7cfsqrg8sq3cs8ptsafqs6drtyuxswrqga",
    # "1LQKFmdYrN9egC5grf8Thbcuwwv4sE4RvP": "https://bitinfocharts.com/bitcoin/address/1LQKFmdYrN9egC5grf8Thbcuwwv4sE4RvP",
    # "bc1qzwmsmdkesqecjtwtgg09zh7jeq0ny2xde9ztfe": "https://bitinfocharts.com/bitcoin/address/bc1qzwmsmdkesqecjtwtgg09zh7jeq0ny2xde9ztfe",
    # "3ELFXnaLivVJzw7s2FBdqgKsGKB4rVT8ma": "https://bitinfocharts.com/bitcoin/address/3ELFXnaLivVJzw7s2FBdqgKsGKB4rVT8ma",
    # "bc1q7fm7g23tr9ap7pktqe32mxj7j3rls8th57edje": "https://bitinfocharts.com/bitcoin/address/bc1q7fm7g23tr9ap7pktqe32mxj7j3rls8th57edje",
    # "13s2ce5YSeVeJbdjCA54r5WykWPYZg3gJH": "https://bitinfocharts.com/bitcoin/address/13s2ce5YSeVeJbdjCA54r5WykWPYZg3gJH",
    # "1Btud1pqADgGzgBCZzxzc2b1o1ytk1HYWC": "https://bitinfocharts.com/bitcoin/address/1Btud1pqADgGzgBCZzxzc2b1o1ytk1HYWC",
    # "1BXZng4dcXDnYNRXRgHqWjzT5RwxHHBSHo": "https://bitinfocharts.com/bitcoin/address/1BXZng4dcXDnYNRXRgHqWjzT5RwxHHBSHo",
    # "1FXHxbZ8HiGDCUrkainA9RKzqfHHkGi1hu": "https://bitinfocharts.com/bitcoin/address/1FXHxbZ8HiGDCUrkainA9RKzqfHHkGi1hu",
    # "1BvNwfxEQwZNRmYQ3eno6e976XyxhCsRXj": "https://bitinfocharts.com/bitcoin/address/1BvNwfxEQwZNRmYQ3eno6e976XyxhCsRXj",
    # "1FVd6EEQnfq8UPDTzfcCBKZTR4uGGJzbgH": "https://bitinfocharts.com/bitcoin/address/1FVd6EEQnfq8UPDTzfcCBKZTR4uGGJzbgH",
    # "1G47mSr3oANXMafVrR8UC4pzV7FEAzo3r9": "https://bitinfocharts.com/bitcoin/address/1G47mSr3oANXMafVrR8UC4pzV7FEAzo3r9",
    # "35j7hbYS9QnKHgdrJF4MozcYwax11J58DT": "https://bitinfocharts.com/bitcoin/address/35j7hbYS9QnKHgdrJF4MozcYwax11J58DT",
    # "17spLhCpZVdQXFz2ZL1aP5gRci6RFVNhrD": "https://bitinfocharts.com/bitcoin/address/17spLhCpZVdQXFz2ZL1aP5gRci6RFVNhrD",
    # "1Miy5sJZSamDZN6xcJJidp9zYxhSrpDeJm": "https://bitinfocharts.com/bitcoin/address/1Miy5sJZSamDZN6xcJJidp9zYxhSrpDeJm",
    # "1AaJfJbaoP553HGpmXvqYwZ9a9q8SE9NgX": "https://bitinfocharts.com/bitcoin/address/1AaJfJbaoP553HGpmXvqYwZ9a9q8SE9NgX",
    # "1Fo497ay4yuv3zQoN9hDWTGuNb33ciioR3": "https://bitinfocharts.com/bitcoin/address/1Fo497ay4yuv3zQoN9hDWTGuNb33ciioR3",
    # "13brDLPdkznmpTRgwaXP7f91NhsTkMP9w4": "https://bitinfocharts.com/bitcoin/address/13brDLPdkznmpTRgwaXP7f91NhsTkMP9w4",
    # "bc1qncsa0qdrgsr58303gsnuwhd5vrm7hlkpd6klmf": "https://bitinfocharts.com/bitcoin/address/bc1qncsa0qdrgsr58303gsnuwhd5vrm7hlkpd6klmf",
    # "bc1qlu098gkdn2enjw424y5s60avpj8mphlkacus6n": "https://bitinfocharts.com/bitcoin/address/bc1qlu098gkdn2enjw424y5s60avpj8mphlkacus6n",
    # "14UeyAD9rQCSJgdJzuzFgShq84gW62Bsat": "https://bitinfocharts.com/bitcoin/address/14UeyAD9rQCSJgdJzuzFgShq84gW62Bsat",
    # "1D3mERfHYY2e96HKUZUsXX7HqHkqUFEadv": "https://bitinfocharts.com/bitcoin/address/1D3mERfHYY2e96HKUZUsXX7HqHkqUFEadv",
    # "1NFPNeet3ygvVZtDbxYeLECfs7g7vH8PSV": "https://bitinfocharts.com/bitcoin/address/1NFPNeet3ygvVZtDbxYeLECfs7g7vH8PSV",
    # "1Kq6hXXiSpdp9bg9hDDyqm8ZfvgZmzchjn": "https://bitinfocharts.com/bitcoin/address/1Kq6hXXiSpdp9bg9hDDyqm8ZfvgZmzchjn",
    # "19CkUw43czT8yQctnHXNiB5ivNtibWbzqS": "https://bitinfocharts.com/bitcoin/address/19CkUw43czT8yQctnHXNiB5ivNtibWbzqS",
    # "1DFv3qVAbravZBZqHmoEphMDtTs2zXPYXk": "https://bitinfocharts.com/bitcoin/address/1DFv3qVAbravZBZqHmoEphMDtTs2zXPYXk",
    # "1JCozFUFS5TBAAbnrr9jRWDVQURo2kGeRq": "https://bitinfocharts.com/bitcoin/address/1JCozFUFS5TBAAbnrr9jRWDVQURo2kGeRq",
    # "18gYq8BpkbcizC4jZ9zyQxo2NBVEQ2p4hM": "https://bitinfocharts.com/bitcoin/address/18gYq8BpkbcizC4jZ9zyQxo2NBVEQ2p4hM",
    # "14Ngt4akcnVgaoAMxoMqz9rPcP3bYsGbbM": "https://bitinfocharts.com/bitcoin/address/14Ngt4akcnVgaoAMxoMqz9rPcP3bYsGbbM",
    # "1NSbFq6rCeSC1p2EBrov5R1uUTFRBu8tcs": "https://bitinfocharts.com/bitcoin/address/1NSbFq6rCeSC1p2EBrov5R1uUTFRBu8tcs",
    # "16b8LpbDa38xrAQHVVDrC3xyztPdRaX5a2": "https://bitinfocharts.com/bitcoin/address/16b8LpbDa38xrAQHVVDrC3xyztPdRaX5a2",
    # "18QCiLiXhko8pb4rqv3mCtC834tSTWHNij": "https://bitinfocharts.com/bitcoin/address/18QCiLiXhko8pb4rqv3mCtC834tSTWHNij",
    # "1PjPfocmxS262puhYqUwaagE9zBJTZHGwK": "https://bitinfocharts.com/bitcoin/address/1PjPfocmxS262puhYqUwaagE9zBJTZHGwK",
    # "1HmiKJMQH4569UMpeGX2QStUfpjx7pBKhW": "https://bitinfocharts.com/bitcoin/address/1HmiKJMQH4569UMpeGX2QStUfpjx7pBKhW",
    # "bc1qnrgvj22yrr5apn2020ssv897nxjaj668a6ydprpxf7gm3g49fknsndfju0": "https://bitinfocharts.com/bitcoin/address/bc1qnrgvj22yrr5apn2020ssv897nxjaj668a6ydprpxf7gm3g49fknsndfju0",
    # "1FvkWMMH9MDMACHqynrerzduaQ5AjjZKDA": "https://bitinfocharts.com/bitcoin/address/1FvkWMMH9MDMACHqynrerzduaQ5AjjZKDA",
    # "1MJZLeLbsoSf2kuDr5gAX3QE93BvhvqkCC": "https://bitinfocharts.com/bitcoin/address/1MJZLeLbsoSf2kuDr5gAX3QE93BvhvqkCC",
    # "18i4YXRrhmHCXjiw5pJoSxFCy3fA4ph9Lz": "https://bitinfocharts.com/bitcoin/address/18i4YXRrhmHCXjiw5pJoSxFCy3fA4ph9Lz",
    # "1HvZQX9XkFFaNa8d5VpwMcYkyebyp6cCXM": "https://bitinfocharts.com/bitcoin/address/1HvZQX9XkFFaNa8d5VpwMcYkyebyp6cCXM",
    # "3CG73de45sR9cYLFAkzF6peRai1Q44R923": "https://bitinfocharts.com/bitcoin/address/3CG73de45sR9cYLFAkzF6peRai1Q44R923",
    # "3L9hddHJMnpE1qzofQ2TSvMiiMf5ejX1Yw": "https://bitinfocharts.com/bitcoin/address/3L9hddHJMnpE1qzofQ2TSvMiiMf5ejX1Yw",
    # "3Pv6S8ZEcQLmXigA694aUZhVmnLUjNzxcc": "https://bitinfocharts.com/bitcoin/address/3Pv6S8ZEcQLmXigA694aUZhVmnLUjNzxcc",
    # "3HNYrC3gDn3jqe1GGvSnLMpyCzPT4ugjCr": "https://bitinfocharts.com/bitcoin/address/3HNYrC3gDn3jqe1GGvSnLMpyCzPT4ugjCr",
    # "18VmXvkF4cgLi35RtMiHHDpvMjUCyVpQ9x": "https://bitinfocharts.com/bitcoin/address/18VmXvkF4cgLi35RtMiHHDpvMjUCyVpQ9x",
    # "1DDWbJhKqfidczaHF1ugGP2KzPgcaU3tGD": "https://bitinfocharts.com/bitcoin/address/1DDWbJhKqfidczaHF1ugGP2KzPgcaU3tGD",
    # "16aEn4p6hK4FMpLtJGpoQZMZ946sDg1Z6n": "https://bitinfocharts.com/bitcoin/address/16aEn4p6hK4FMpLtJGpoQZMZ946sDg1Z6n",
    # "bc1qd6dhl3px06pux9rmzw07rkd2kwj9ef36dwgqdg": "https://bitinfocharts.com/bitcoin/address/bc1qd6dhl3px06pux9rmzw07rkd2kwj9ef36dwgqdg",
    # "bc1qgzxtj07yh9jhyv0aexm2y9s4un0lz57eejyrur": "https://bitinfocharts.com/bitcoin/address/bc1qgzxtj07yh9jhyv0aexm2y9s4un0lz57eejyrur",
    # "bc1q8wlq09pnue9hpl9r5r37zek2qapafjfhj85dgj": "https://bitinfocharts.com/bitcoin/address/bc1q8wlq09pnue9hpl9r5r37zek2qapafjfhj85dgj",
    # "bc1q0r3hp96aqq4akjcalasn2v79nmvewasl2sjh84": "https://bitinfocharts.com/bitcoin/address/bc1q0r3hp96aqq4akjcalasn2v79nmvewasl2sjh84",
    # "bc1q4hm96naa2ydcqlxpwlvljvrnt5svm8ejcqnhj0": "https://bitinfocharts.com/bitcoin/address/bc1q4hm96naa2ydcqlxpwlvljvrnt5svm8ejcqnhj0",
    # "bc1q2x6v47z3xhxu8suuzqtehf8t7v997g3cjhc6kl": "https://bitinfocharts.com/bitcoin/address/bc1q2x6v47z3xhxu8suuzqtehf8t7v997g3cjhc6kl",
    # "bc1qlnexsqagmk27ju9dmmvj470l6jsl4j6t4lm34x": "https://bitinfocharts.com/bitcoin/address/bc1qlnexsqagmk27ju9dmmvj470l6jsl4j6t4lm34x",
    # "bc1qfkdljt8e3hqqk43nz7wsl4usrylsp4rl5d62p4": "https://bitinfocharts.com/bitcoin/address/bc1qfkdljt8e3hqqk43nz7wsl4usrylsp4rl5d62p4",
    # "bc1qxhkn652vt72zy9n2s3mkv2dk5y7ny7dmt02lr4": "https://bitinfocharts.com/bitcoin/address/bc1qxhkn652vt72zy9n2s3mkv2dk5y7ny7dmt02lr4",
    # "1MLiPwYjNACQHREFKwGtkPpWgd8PqpbuQ4": "https://bitinfocharts.com/bitcoin/address/1MLiPwYjNACQHREFKwGtkPpWgd8PqpbuQ4",
    # "1G6KK2j1C7DAsPmQ6joZpAY4gN84z5Te4E": "https://bitinfocharts.com/bitcoin/address/1G6KK2j1C7DAsPmQ6joZpAY4gN84z5Te4E",
    # "1D387jd5ZuvudpUQrSv8vK5b2M1SBnvdY8": "https://bitinfocharts.com/bitcoin/address/1D387jd5ZuvudpUQrSv8vK5b2M1SBnvdY8",
    # "1Ly9nQEyaRQoRPSAE4dABrpav2SaAR383W": "https://bitinfocharts.com/bitcoin/address/1Ly9nQEyaRQoRPSAE4dABrpav2SaAR383W",
    # "1GuLYGgr9FZwCBBQfDmMiJfTF4cvyrJSeu": "https://bitinfocharts.com/bitcoin/address/1GuLYGgr9FZwCBBQfDmMiJfTF4cvyrJSeu",
    # "1Ms4LPLVYWCyYTAqBcotXAeizHgE778abE": "https://bitinfocharts.com/bitcoin/address/1Ms4LPLVYWCyYTAqBcotXAeizHgE778abE",
    # "1ZK5rrghS3Uhnra64LiuZVupa6WTSuPfF": "https://bitinfocharts.com/bitcoin/address/1ZK5rrghS3Uhnra64LiuZVupa6WTSuPfF",
    # "15SGg7PpcJ7bMhENw4gc3Qp4LT6c5uLGza": "https://bitinfocharts.com/bitcoin/address/15SGg7PpcJ7bMhENw4gc3Qp4LT6c5uLGza",
    # "152BK6BQa672Dy8PHf4JQtS27pBRBiYy6e": "https://bitinfocharts.com/bitcoin/address/152BK6BQa672Dy8PHf4JQtS27pBRBiYy6e",
    # "1FUpBduq45UfULPACj1Phw9hRvwroJqYUX": "https://bitinfocharts.com/bitcoin/address/1FUpBduq45UfULPACj1Phw9hRvwroJqYUX",
    # "15n6GcFRFm3287FotAWunZe58D9yXx13AB": "https://bitinfocharts.com/bitcoin/address/15n6GcFRFm3287FotAWunZe58D9yXx13AB",
    # "1Cm9ugUjEUyMvjB3uWxESapa861uEtcVyc": "https://bitinfocharts.com/bitcoin/address/1Cm9ugUjEUyMvjB3uWxESapa861uEtcVyc",
    # "154sxXJekWHQ5nPxkkaWnMghy4o9qWaNdU": "https://bitinfocharts.com/bitcoin/address/154sxXJekWHQ5nPxkkaWnMghy4o9qWaNdU",
    # "1Gc6ggvqHRRwyyx6rrW9Wn17bqzV7voWvD": "https://bitinfocharts.com/bitcoin/address/1Gc6ggvqHRRwyyx6rrW9Wn17bqzV7voWvD",
    # "1Cw9Kyr8hKsucXTtcwuGVqeBHDrnRtXC8D": "https://bitinfocharts.com/bitcoin/address/1Cw9Kyr8hKsucXTtcwuGVqeBHDrnRtXC8D",
    # "12GQSEPmoCiw7zrWJbsYa5SD3hkKPSzyAq": "https://bitinfocharts.com/bitcoin/address/12GQSEPmoCiw7zrWJbsYa5SD3hkKPSzyAq",
    # "1AwimXdGoX8nR9dMagCDMGJQB62GNHgrqM": "https://bitinfocharts.com/bitcoin/address/1AwimXdGoX8nR9dMagCDMGJQB62GNHgrqM",
