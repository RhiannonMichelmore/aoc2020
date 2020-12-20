monster = '                  # \n#    ##    ##    ###\n #  #  #  #  #  #   '

lines = monster.split('\n')
coords = []
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == '#':
            coords.append((x,y))

print(coords)

