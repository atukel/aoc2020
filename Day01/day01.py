import itertools

result = [int(i) for i in open("input.txt").read().splitlines()]

def naivePart1():
    for i in range(len(result)):
        for j in range(len(result)):
            if result[i] + result[j] == 2020:
                print(result[i] * result[j])

def naivePart2():
    for i in range(len(result)):
        for j in range(len(result)):
            for k in range(len(result)):
                if result[i] + result[j] + result[k] == 2020:
                    print(result[i] * result[j] * result[k])

def decent():
    combTwo = list(itertools.combinations(result, 2))
    print({i * j for (i,j) in combTwo if i + j == 2020})
    combThree = list(itertools.combinations(result, 3))
    print({i * j * k for (i, j, k) in combThree if i + j + k == 2020})

decent()
