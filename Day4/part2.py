with open("input.txt", "r") as f:
    data = f.readlines()

copy_tracker = [1] * len(data)

score = 0

for card_num, line in enumerate(data):
    next_cards_won = 0
    card_data = line.split(":")[1].strip().split("|")
    win = list(map(int,map(str.strip,card_data[0].strip().split())))
    draw_nums = list(map(int,map(str.strip,card_data[1].strip().split())))
    for num in draw_nums:
        if num in win:
            next_cards_won += 1
    for i in range(next_cards_won):
        copy_tracker[card_num + i + 1] += copy_tracker[card_num] # i starts with 0

print(sum(copy_tracker))