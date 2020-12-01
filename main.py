def part1():
    result = [int(i) for i in open("input.txt").read().splitlines()]
    for i in range(len(result)):
        for j in range(len(result)):
            if result[i] + result[j] == 2020:
                print(result[i] * result[j])

def part2():
    result = [int(i) for i in open("input.txt").read().splitlines()]
    for i in range(len(result)):
        for j in range(len(result)):
            for k in range(len(result)):
                if result[i] + result[j] + result[k] == 2020:
                    print(result[i] * result[j] * result[k])
part2()