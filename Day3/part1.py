with open("input.txt", "r") as f:
    data = f.readlines()

map = []

for line in data:
    map.append(list(line.strip()))

map_y = len(map)
map_x = len(map[0])

parts_sum = 0

for y in range(map_y):
    current_num = ""
    is_part = False
    for x in range(map_x):
        if map[y][x].isdigit():
            current_num += map[y][x]
        else:
            continue

        # check only if not already a valid part
        if current_num != "" and is_part == False:
            #check upper row
            if y > 0:
                if x > 0:
                    if not map[y-1][x-1].isdigit() and map[y-1][x-1] != ".":
                        is_part = True
                if not map[y-1][x].isdigit() and map[y-1][x] != ".":
                    is_part = True
                if x < map_x - 1:
                    if not map[y-1][x+1].isdigit() and map[y-1][x+1] != ".":
                        is_part = True
            # check left right
            if x > 0:
                if not map[y][x-1].isdigit() and map[y][x-1] != ".":
                    is_part = True
            if x < map_x - 1:
                if not map[y][x+1].isdigit() and map[y][x+1] != ".":
                    is_part = True
            # check lower row
            if y < map_y - 1:
                if x > 0:
                    if not map[y+1][x-1].isdigit() and map[y+1][x-1] != ".":
                        is_part = True
                if not map[y+1][x].isdigit() and map[y+1][x] != ".":
                    is_part = True
                if x < map_x - 1:
                    if not map[y+1][x+1].isdigit() and map[y+1][x+1] != ".":
                        is_part = True

        #print(current_num)
        # full number found add to list.. (or not)
        if (x == map_x - 1 or not map[y][x+1].isdigit()) and current_num != "":
            if is_part == True:
                parts_sum += int(current_num)
                is_part = False
            current_num = ""

print(parts_sum)