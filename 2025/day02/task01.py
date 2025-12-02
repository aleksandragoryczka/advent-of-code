def check_if_invalid(value: str) -> int:
    if len(value) % 2 == 0:
        value_list = list(value)
        if value_list[:int(len(value_list)/2)] == value_list[int(len(value_list)/2):]:
            return int(value)
    return 0


with open('2025/inputs/day02/input.txt') as f:
    ranges = f.read().split(",")

invalid_ids_sum = 0
for _range in ranges:
    start = int(_range.split("-")[0])
    end = int(_range.split("-")[1])

    for val in range(start, end + 1):
        invalid_ids_sum += check_if_invalid(str(val))
        
print(invalid_ids_sum)

