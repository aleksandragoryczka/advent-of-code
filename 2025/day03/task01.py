with open('2025/inputs/day03/input.txt') as f:
    lines = f.read().splitlines()

descending_digits = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']

def find_max_value_in_slice(slice: list[str]) -> int:
    return max([int(x) for x in slice])

total_output_joltage = 0
for line in lines:
    list_line = list(line)[:len(list(line))]
    max_number = 0
    for digit in descending_digits:
        next_slice_start_idx = 0

        for idx, val in enumerate(list_line[:len(list_line)-1]):
            if val == digit:
                next_slice_start_idx = idx + 1
                break
        
        if next_slice_start_idx != 0:
            max_value_in_slice = find_max_value_in_slice(list_line[next_slice_start_idx:])
            current_max_number = 10 * int(digit) + max_value_in_slice
            if current_max_number > max_number:
                max_number = current_max_number

    total_output_joltage += max_number

print(total_output_joltage)
