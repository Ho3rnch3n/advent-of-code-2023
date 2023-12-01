with open("input.txt","r") as f:
    input = f.readlines()

sol = 0

for line in input:
    numbers = "".join(x for x in line if x.isdigit())
    sol += int(numbers[0] + numbers[-1])

print(sol)