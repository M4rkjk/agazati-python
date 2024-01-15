szoveg = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui nam magni eaque voluptas iste quasi voluptatem praesentium id exercitationem dolorum nemo veniam ab delectus alias nulla, atque ipsam consequuntur labore minus enim necessitatibus quaerat eius perferendis. Fugiat officia iusto libero eos, recusandae reprehenderit consectetur optio fugit quidem unde quis quaerat asperiores id eligendi labore dolorem ut voluptas enim. Facere in eaque reprehenderit explicabo modi possimus alias veritatis, excepturi aspernatur nostrum magni et tempora recusandae id ipsa illo repellendus, quod cumque veniam. Voluptates numquam illum ratione doloribus! Illo, voluptates ut! Eveniet, illum incidunt! Animi, tempora ipsa ipsam tempore error molestiae totam velit iste aliquam hic magnam incidunt minima amet minus labore eius voluptatem necessitatibus mollitia illum corrupti voluptate impedit expedita? Quis eveniet eligendi quas, voluptatum et nostrum doloremque iste optio laudantium nulla rem beatae quasi esse labore? Aliquid assumenda minus impedit ullam! Ab error culpa tempora reiciendis itaque sequi et asperiores neque officia voluptate omnis possimus, similique, corrupti perferendis facere natus, enim quisquam. Facere distinctio tempore unde reprehenderit laboriosam magni natus accusamus voluptas labore laudantium, eaque ratione error, sunt, amet officia rem voluptatum iste quo architecto quasi officiis! Quidem nisi consequuntur nulla, aspernatur error officia debitis. Minima, doloribus! Qui, dolor praesentium!'

szavak = szoveg.split(' ')

print(szavak)

# # melyik szó hányszor fordul elő a szövegben?
# {'Lorem': 1, 
#  'ipsum': 2,
#  'dolor': 1}

stat = {}

for szo in szavak:
    if szo not in stat.keys():
        stat[szo] = 1
    else:
        stat[szo] += 1

# print(stat)


# Melyik szavak fordulnak elő egynél többször?
for key, value in stat.items():
    if value > 1:
        print(f'{key} - {value} darab')


# Melyik szó fordul elő a legtöbbször?
legtobb_value = -1
legtobb_key = ''
for key, value in stat.items():
    if value > legtobb_value:
        legtobb_value = value
        legtobb_key = key
# print(f'Legtöbbször a {legtobb_key} szó fordul elő ({legtobb_value} darab)')

#Lehet, hogy több maximum van...
print('Legtöbbször előforduló szavak: ')
for key, value in stat.items():
    if value == legtobb_value:
        print(f'\t{key}')
