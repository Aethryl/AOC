def get_file_contents() -> str:
    with open("input.txt", "r") as file:
        return file.read()


contents: str = get_file_contents()

total_joltage = 0
# transform the data per line
for line in contents.splitlines():
    numbers = list(map(int, line))
    highest = numbers[0]
    highest_index = 0
    for i in range(1, len(numbers) - 12):  # 12 -> 1 for part 1
        if numbers[i] > highest:
            highest = numbers[i]
            highest_index = i

    # part 1
    # # print(f"Highest: {highest} at index {highest_index}")
    # num2 = max(numbers[highest_index + 1 :])
    # # print(f"Second highest: {num2}")

    # total_joltage += int(str(highest) + str(num2))
    # # print(f"Current total joltage: {total_joltage}")
    #
    # part 2

    # print(f"Highest: {highest} at index {highest_index}")
    remaining = numbers[highest_index + 1 :]
    remaining.reverse()
    # print(f"Remaining: {remaining}")

    stack = [highest]

    while remaining:
        print(f"Stack: {stack}, Remaining: {remaining}")
        next = remaining.pop()
        if not remaining:
            if len(stack) < 11:
                stack.append(next)
                break
        while len(stack) + len(remaining) > 11 and next > stack[-1]:
            print(f"Stack before pop: {stack}")
            stack.pop()
        if len(stack) < 12:
            stack.append(next)

    found_str = "".join(map(str, stack))
    print("-------------------")
    print(f"Found string: {found_str}")
    print("-------------------")
    assert len(found_str) == 12, f"Found string length is not 12: {len(found_str)}"
    total_joltage += int(found_str)

print(total_joltage)
