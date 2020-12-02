passwordList = [input.strip() for input in open("input.txt").readlines() if input.strip()]


def part1():
    passwordCount = 0
    for line in passwordList:
        characterCount, key, password = line.split(" ")
        minimum, maximum = [int(i) for i in characterCount.split("-")]
        if password.count(key[0]) in range(minimum, maximum + 1):
            passwordCount += 1
    print(passwordCount)


def part2():
    passwordCount = 0
    for line in passwordList:
        characterCount, key, password = line.split(" ")
        firstPos, SecondPos = [int(i) for i in characterCount.split("-")]
        check = True
        if key[0] == password[firstPos - 1] and key[0] == password[SecondPos - 1]:
            check = False
        elif key[0] == password[SecondPos - 1]:
            check = True
        elif key[0] == password[firstPos - 1]:
            check = True
        else:
            check = False
        if check:
            passwordCount += 1
    print(passwordCount)
