with open("input.txt", "r") as f:
    data = f.readlines()

score = 0

for line in data:
    value = 0.5
    is_winning = False
    card_data = line.split(":")[1].strip().split("|")
    win = list(map(int,map(str.strip,card_data[0].strip().split())))
    draw_nums = list(map(int,map(str.strip,card_data[1].strip().split())))
    for num in draw_nums:
        if num in win:
            value *= 2
            is_winning = True
    if is_winning:
        score += int(value)

print(score)