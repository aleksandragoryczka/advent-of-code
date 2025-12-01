with open('2025/inputs/day01/input.txt') as f:
    lines = f.readlines()

dial = 50
zero_counter = 0

for line in lines:
    rotation_number = int(line[1:])

    if line.startswith("R"):
        dial += rotation_number
    if line.startswith("L"):
        dial -= rotation_number
    if dial >= 100 or dial <= 0:
        rotations_counter = rotation_number // 100
        dial = dial % 100
        if rotations_counter > 0:
            zero_counter += rotations_counter
        else:
            zero_counter += 1

print(zero_counter)

