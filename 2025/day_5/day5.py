def get_file_contents() -> str:
    with open("input.txt", "r") as file:
        return file.read()


contents: str = get_file_contents()


def get_check_fresh_function(ranges: list[tuple]) -> callable:
    def func(id: int) -> bool:
        for r in ranges:
            if r[0] <= id <= r[1]:
                return True
        return False

    return func


lines = contents.splitlines()
lines.reverse()

ranges_lines = []
while True:
    line = lines.pop()
    if line == "":
        break
    parts = line.split("-")
    ranges_lines.append((int(parts[0]), int(parts[1])))

# check_fresh = get_check_fresh_function(ranges_lines) # part 1

# print(sum(1 for line in lines if check_fresh(int(line)))) # part 1

# part 2

ranges_lines.sort()

# stitch ranges
stitched_ranges = []
for i in range(len(ranges_lines)):
    if i == 0:
        stitched_ranges.append(ranges_lines[i])
    else:
        last_range = stitched_ranges[-1]
        current_range = ranges_lines[i]
        if current_range[0] <= last_range[1]:
            # overlap
            new_range = (last_range[0], max(last_range[1], current_range[1]))
            stitched_ranges[-1] = new_range
        else:
            stitched_ranges.append(current_range)

range_count = 0
for r in stitched_ranges:
    range_count += r[1] - r[0] + 1

print(range_count)
