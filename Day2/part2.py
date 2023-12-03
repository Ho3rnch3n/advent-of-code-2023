with open("input.txt","r") as f:
    data = f.readlines()

sum_powers = 0

for line in data:
    game_power = 1
    game_dict = {"red": 0, "green": 0, "blue": 0}
    line = line.split(":")
    game_id = int(line[0].split(" ")[1].strip())
    game_rolls = line[1].strip().split(";")

    for roll in game_rolls:        
        roll_cubes = roll.strip().split(",")
        for cube in roll_cubes:
            cube = cube.strip().split(" ")
            cube_color = cube[1].strip()
            cube_amount = int(cube[0].strip())
            if game_dict[cube_color] < cube_amount:
                game_dict[cube_color] = cube_amount
    
    for roll_amount in game_dict.values():
        game_power *= roll_amount
    sum_powers += game_power

print(sum_powers)