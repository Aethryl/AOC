def get_file_contents() -> str:
    with open("input.txt", "r") as file:
        return file.read()


contents: str = get_file_contents()
zero_hit = ""
pos = 50
zero_counter = 0
for line in contents.splitlines():
    old_pos = pos  ## part 2
    old_zero_counter = zero_counter  ## part 2 debug
    rotations = int(line[1:])
    if line[0] == "L":
        pos -= rotations
    else:
        pos += rotations
    pos %= 100
    # ## part 1
    if pos == 0:
        zero_counter += 1
        zero_hit = "point at 0"

    ## part 2
    zero_counter += int(rotations / 100)  # whole rotations
    rest_rotations = rotations % 100
    if old_pos != 0 and pos != 0:
        if line[0] == "L":
            if old_pos < (old_pos - rest_rotations) % 100:
                zero_counter += 1
                zero_hit = "during rotation LEFT"
        if line[0] == "R":
            if old_pos > (old_pos + rest_rotations) % 100:
                zero_counter += 1
                zero_hit = "during rotation RIGHT"

    print(
        f"Line: {line}, Old Pos: {old_pos}, New Pos: {pos}, Zero Count: {zero_counter - old_zero_counter}, Zero Hit: {zero_hit}"
    )

print(zero_counter)
