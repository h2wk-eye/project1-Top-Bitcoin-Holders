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

# for i in range(1, 6):
#     if i>1:
#         url = "https://bitinfocharts.com/top-100-richest-bitcoin-addresses-" + str(i) + ".html"
req = requests.get(url, headers = headers)
src = req.text
soup = BeautifulSoup(src, "lxml")

tables = soup.find_all(class_= "table-striped")
all_tr=[]
