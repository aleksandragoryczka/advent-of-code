def check_if_invalid(value: str) -> int:
    value_list = list(value)
    for i in range(0, int(len(value_list)/2) + 1):
        first_slice = value_list[:i]
        if len(first_slice) > 0:
            no_slices = len(value_list) / len(first_slice)
            if int(no_slices) == no_slices:
                if first_slice * int(no_slices) == value_list:
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

