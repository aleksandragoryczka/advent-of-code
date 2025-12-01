with open('2025/inputs/day01/input.txt') as f:
    lines = f.readlines()

dial = 50
zero_counter = 0

for line in lines:
    if line.startswith("R"):
        dial += int(line[1:])
    if line.startswith("L"):
        dial -= int(line[1:])
    if dial >= 100 or dial < 0:
        dial = dial % 100
    if dial == 0:
        zero_counter += 1

print(zero_counter)