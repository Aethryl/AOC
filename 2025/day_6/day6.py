def get_file_contents() -> str:
    with open("input.txt", "r") as file:
        return file.read()


contents: str = get_file_contents()

# part 1
# problem_accumalators = []
# problems_totals = []

# lines = contents.splitlines()
# li = lines.pop()

# part 1

# for p in li.strip(" "):
#     if p == "*":
#         problem_accumalators.append(p)
#         problems_totals.append(1)
#     elif p == "+":
#         problem_accumalators.append(p)
#         problems_totals.append(0)

# while lines:
#     line = lines.pop()
#     numbers = line.split(" ")
#     numbers = list(filter(lambda x: x != "", numbers))
#     for i, n in enumerate(numbers):
#         if problem_accumalators[i] == "*":
#             problems_totals[i] *= int(n)
#         else:
#             problems_totals[i] += int(n)

# print(sum(problems_totals))

# part 2
lines = contents.splitlines()
biggust_line_length = max(len(line) for line in lines)

index = biggust_line_length - 1

problem_line = lines.pop()

number_stack = []

total = 0

while index >= 0:
    number_string = ""
    for line in lines:
        if index < len(line):
            number_string += line[index]
    if number_string.strip():
        number_stack.append(int(number_string))

    if index < len(problem_line):
        operator = problem_line[index]
        if operator == "+":
            total += sum(number_stack)
            number_stack = []
        elif operator == "*":
            multi = 1
            for n in number_stack:
                multi *= n
            total += multi
            number_stack = []
    index -= 1

print(total)
