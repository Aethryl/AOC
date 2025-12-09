from math import ceil, log10


def get_file_contents() -> str:
    with open("input.txt", "r") as file:
        return file.read()


contents: str = get_file_contents()

ranges_strings = contents.split(",")


# bruteforce some numbers
duplicati = 0

for ranges_string in ranges_strings:
    range_parts = ranges_string.split("-")
    start = int(range_parts[0])
    end = int(range_parts[1])
    number = start
    while number < end + 1:
        string_number = str(number)
        # debug
        # print(f"Checking number: {number}")
        if len(string_number) % 2 != 0:
            if string_number[len(string_number) // 2] == "0":
                number += 1
                continue
        base10 = log10(number)
        half_base10 = base10 / 2
        half_base10 = ceil(half_base10)

        first_half_number = number % (10**half_base10)

        n = first_half_number * (10**half_base10)
        if number == n + first_half_number:
            duplicati += number
            # print(f"!!!!!!!!!!!!!Found duplicati: {number}")
            number += 1
            continue

        # part 2
        matcher = ""
        for i in range(len(string_number) // 2 + 1):
            matcher = matcher + string_number[i]
            # debug
            # print(f"matcher at {i}: {matcher}")
            matches = string_number.count(matcher)
            if matches > 1 and len(matcher * matches) == len(string_number):
                duplicati += number
                # print(f"!!!!!!!!!!!!!Found duplicati: {number}")
                break
        number += 1

print(duplicati)
