# Kérjük be egy másodfokú egyenlet együtthatóit, (a, b, c)
# és írjuk ki a gyökeit (megoldásait). x1, x2.

from math import sqrt

a = float(input('Adja meg az első számot (a): '))
b = float(input('Adja meg a második számot (b): '))
c = float(input('Adja meg a harmadik számot (c): '))

d = b**2 - 4 * a * c
if d >= 0:
    x1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    print(f'Az x1 megoldása: {x1} ')

    x2 = (+b - sqrt(b**2 - 4 * a * c)) / (2*a)
    print(f'Az x2 megoldása: {x2} ')
else:
    print('Nincs megoldás a valós számok halmazán! ')

