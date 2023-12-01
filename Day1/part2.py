with open("input.txt","r") as f:
    input = f.readlines()

sol = 0

for line in input:
    # i did this because some numbers are overlapping for example one of the examples: xtwone3four
    line = line.replace("one","one1one").replace("two","two2two").replace("three","three3three").replace("four","four4four").replace("five","five5five").replace("six","six6six").replace("seven","seven7seven").replace("eight","eight8eight").replace("nine","nine9nine")
    numbers = "".join(x for x in line if x.isdigit())
    sol += int(numbers[0] + numbers[-1])

print(sol)