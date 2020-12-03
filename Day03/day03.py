grid = [input.strip() for input in open("input.txt").readlines() if input.strip()]

def part1(rowIncrease, columnIncrease):
    treeCount, row, column = 0, 0, 0
    while row < len(grid):
        currentCoordinate = grid[row][column % len(grid[row])]
        if currentCoordinate == "#":
            treeCount += 1
        row += rowIncrease
        column += columnIncrease
    return treeCount

print(part1(1, 3))

print(part1(1, 3) * part1(1, 1) * part1(1, 5) * part1(1, 7) * part1(2, 1))