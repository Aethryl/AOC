def get_file_contents() -> str:
    with open("input.txt", "r") as file:
        return file.read()


contents: str = get_file_contents()

grid = [[]]
for i, line in enumerate(contents.splitlines()):
    grid.append([])
    for j, char in enumerate(line):
        grid[i].append(char)

# brute force honestly. should be quick enough
total_free_roll_count = 0
while True:  # part 2
    free_roll_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):  # assume rectangular grid
            # check grid 8 directions
            if grid[i][j] == ".":
                print(".", end="", sep="")
                continue
            dir_count = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[ni]):
                        if grid[ni][nj] == "@":
                            dir_count += 1
            if dir_count < 4:
                free_roll_count += 1
                print("x", end="", sep="")
                grid[i][j] = "."  # part 2
            else:
                print("@", end="", sep="")  # must be @ according to logic

        print("")
    if free_roll_count == 0:
        break
    total_free_roll_count += free_roll_count
    free_roll_count = 0

print(total_free_roll_count)
