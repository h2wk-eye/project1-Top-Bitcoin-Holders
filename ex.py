import pandas as pd
import numpy as np
mt = pd.read_csv('connectedwallets1.csv', sep=',', header = None)

s = mt.to_numpy()
wallets = []


for i in range(564):
    if s[i][0] not in wallets:
        wallets.append(s[i][0])
    if s[i][1] not in wallets:
        wallets.append(s[i][1])

dict = {}
for i in range(len(wallets)):
    dict[wallets[i]]= i


arr = np.zeros([len(wallets),len(wallets)], dtype= int)

for i in range(564):
    arr[dict[s[i][0]]][dict[s[i][1]]] = 1

for i in range(len(wallets)):
    for j in range(len(wallets)):
        print(arr[i][j], end=', ')
    print('\n')
