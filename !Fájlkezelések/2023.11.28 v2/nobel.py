from dijazott import dijazott

dijazottak: list[dijazott] = []

fajl = open('nobel.csv', 'r', encoding='utf8')
fajl.readline()
for sor in fajl:
    dijazottak.append(dijazott(sor.strip()))
fajl.close()

for d in dijazottak:
    if d.teljesnev == 'Arthur B. McDonald':
        print(f'3. feladat: {d.tipus}')
        break

for d in dijazottak:
    if d.ev == 2017 and d.tipus == 'irodalmi':
        print(f'4. feladat: {d.teljesnev}')


print('5. feladat: ')
for d in dijazottak:
    if d.vezeteknev == '' and d.ev >= 1990:
        print(f'\t{d.ev}: {d.keresztnev}')
    
print('6. feladat: ')
for d in dijazottak:
    if 'Curie' in d.vezeteknev:
        print(f'\t{d.ev}: {d.teljesnev}')

print('7. feladat: ')
stat: dict[str, int] = {}
for d in dijazottak:
    if d.tipus in stat.keys():
        stat[d.tipus] += 1
    else:
        stat[d.tipus] = 1
for key, value in stat.items():
    print(f'\t{key.ljust(20)} {value}')

fajl = open('orvosi.txt', 'w', encoding='utf8')
for d in dijazottak:
    if d.tipus == 'orvosi':
        fajl.write(f'{d.ev}:{d.teljesnev}\n')
fajl.close()

def nobeldijak_szama():
    
