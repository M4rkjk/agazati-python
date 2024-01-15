def maganhangzok_szama(nap):
    maganhangzok = 'aáeéiíoóöőuúüű'
    darab = 0
    for n in nap:
        if n in maganhangzok:
            darab += 1
    return darab


napok = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']
# legnagyobb_indexe = 0
# for i, nap in enumerate(napok):
#     if maganhangzok_szama(nap) > maganhangzok_szama(napok[legnagyobb_indexe]):
#         legnagyobb_indexe = i

legnagyobb = napok[0]
for nap in napok:
    if maganhangzok_szama(nap) > maganhangzok_szama(legnagyobb):
        legnagyobb = nap
print(f'A legtöbb magánhangzó a {legnagyobb}-ben van.')
