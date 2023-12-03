with open("input.txt", "r") as f:
    data = f.readlines()

map = []

for line in data:
    map.append(list(line.strip()))

map_y = len(map)
map_x = len(map[0])

gear_ratio_sum = 0

def extract_num(map, x, y):
    while True:
        if x > 0 and map[y][x-1].isdigit():
            x -= 1
        else:
            break
    num = map[y][x]
    while True:
        if x < map_x - 1 and map[y][x+1].isdigit():
            x += 1
            num += map[y][x]
        else:
            break
    return num



for y in range(map_y):
    for x in range(map_x):
        if map[y][x] == "*":
            adj_nums = []
            #check upper row
            if y > 0:
                if map[y-1][x].isdigit():
                    adj_nums.append(extract_num(map,x,y-1))
                else:
                    if x > 0:
                        if map[y-1][x-1].isdigit():
                            adj_nums.append(extract_num(map,x-1,y-1))
                    if x < map_x -1:
                        if map[y-1][x+1].isdigit():
                            adj_nums.append(extract_num(map,x+1,y-1))
            # check left right
            if x > 0:
                if map[y][x-1].isdigit():
                    adj_nums.append(extract_num(map,x-1,y))
            if x < map_x - 1:
                if map[y][x+1].isdigit():
                    adj_nums.append(extract_num(map,x+1,y))
            # check lower row
            if y < map_y - 1:
                if map[y+1][x].isdigit():
                    adj_nums.append(extract_num(map,x,y+1))
                else:
                    if x > 0:
                        if map[y+1][x-1].isdigit():
                            adj_nums.append(extract_num(map,x-1,y+1))
                    if x < map_x -1:
                        if map[y+1][x+1].isdigit():
                            adj_nums.append(extract_num(map,x+1,y+1))

            #print(adj_nums)
            # all adjacent numbers found, check if 2 and calc ratio
            if len(adj_nums) == 2:
                gear_ratio_sum += (int(adj_nums[0]) * int(adj_nums[1]))

print(gear_ratio_sum)