from random import randint
import math

szamok = []

for i in range(20):
    szamok.append(randint(-100,100))

print(szamok)

#1. Melyik a legnagyobb szám?
legnagyobb = szamok[0]
for szam in szamok: #van benne egy felsleges vizsgálat: az első elemet önmagával fogjuk összehasonlítani.
    if szam > legnagyobb:
        legnagyobb = szam
print(f'A legnagyobb szám: {legnagyobb}')


#2. Hányadik a legnagyobb szám? --> ebből megmondható az is hogy melyik az.
legnagyobb_index = 0 # feltesszük, hogy a 0. elem a legnagyobb.
for i in range(1, len(szamok)): # a 0. elemet direkt kihagyjuk
    if szamok[i] > szamok[legnagyobb_index]:
        legnagyobb_index = i
print(f' A legnagyobb szám {szamok[legnagyobb_index]}, sorszáma: {legnagyobb_index + 1}')



#3. Hányadik a legnagyobb páratlan szám? 
legnagyobb_index = len(szamok) + 1 # olyan elemet kell bele rakni, amelyiket biztosan felül fogjuk írni.
# szamok[legnagyobb_index] # list index out of range
for i in range(len(szamok)):
    if szamok[i] % 2 == 1:
        # if legnagyobb_index == len(szamok) + 1: # az eredetileg belerakott rossz érték van benne.
        #     legnagyobb_index = i
        # elif szamok[i] >szamok[legnagyobb_index]:
        #     legnagyobb_index = i
        if legnagyobb_index == len(szamok) + 1 or szamok[i] > szamok[legnagyobb_index]:
            legnagyobb_index = i
print(f'A legnagyobb páratlan szám: {szamok[legnagyobb_index]}, sorszáma: {legnagyobb_index + 1}')
        

# 3. Hányadik a legnagyobb páratlan szám?
#megoldás v2:

# legnagyobb = -999999999999999  # olyan elemet kell bele rakni, amelyiket biztosan felül fogjuk írni.
legnagyobb= -math.inf # végtelen
legnagyobb_index = False
for i in range(len(szamok)):
    if szamok[i] % 2 == 1 and szamok[i] > legnagyobb:
        legnagyobb = szamok[i]
        legnagyobb_index = i
if legnagyobb_index != False:
    print(f'A legnagyobb páratlan szám: {szamok[legnagyobb_index]}, sorszáma: {legnagyobb_index + 1}')
else:
    print('Nincs egyetlen páratlan szám sem. ')