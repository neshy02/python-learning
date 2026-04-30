# https://stepik.org/lesson/488831/step/2?thread=solutions&unit=480067

frst = input().lower()
sec = input().lower()
res_frst = {}
res_sec = {}

for ch in frst:
    if ch in res_frst:
        res_frst[ch] += 1
    else:
        res_frst.update({ch: 1})

for ch in sec:
    if ch in res_sec:
        res_sec[ch] += 1
    else:
        res_sec.update({ch: 1})

if res_frst == res_sec:
    print('YES')
else:
    print('NO')
