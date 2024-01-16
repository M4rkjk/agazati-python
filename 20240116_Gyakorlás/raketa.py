
ora = int(input('Hány órás visszaszámlálást tervezünk? '))
szamlalo = 5
for i in range(ora,0, -1):
    print(f'Visszaszámlálás: {i}')
    felfuggeszt = input('Fel kell függeszteni a visszaszámlálást? (i/n)')
    if felfuggeszt == 'i':
        szamlalo += 1

print('A rakéta a visszaszámlálást követően ennyi órával indult: ', szamlalo )