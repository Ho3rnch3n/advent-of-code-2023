with open("input.txt","r") as f:
    data = f.readlines()

sum_ids = 0

bag = {"red": 12, "green": 13, "blue": 14}

for line in data:
    possible = True
    line = line.split(":")
    game_id = int(line[0].split(" ")[1].strip())
    game_rolls = line[1].strip().split(";")

    for roll in game_rolls:
        roll_dict = {"red": 0, "green": 0, "blue": 0}
        
        roll_cubes = roll.strip().split(",")
        for cube in roll_cubes:
            cube = cube.strip().split(" ")
            cube_color = cube[1].strip()
            cube_amount = int(cube[0].strip())
            roll_dict[cube_color] += cube_amount
        
        for roll_color, roll_amount in roll_dict.items():
            if bag[roll_color] < roll_amount:
                possible = False
    
    if possible:
        sum_ids += game_id

print(sum_ids)