from fordulo import *


beolvas('toto.txt')

print('3. feladat: Toto')
print('3.1 feladat: Adatok beolvasás és tárolása')
print(f'3.2 feladat: Fogadási fordulók száma: {osszes_fordulo()}')
print(f'3.3 feladat: Telitatlálatos szelvények száma: {telitatalalatos_szelvenyek_szama()} db')
if volt_dontetlen_mentes_fordulo():
    print('3.4 feladat: Volt döntetlen mentes forduló.')
else:
    print('3.4 feladat: Nem volt döntetlen mentes forduló')