def main():
    path = "/Users/Stanisław/PycharmProjects/AdventOfCode/2018/2_1/input.txt"
    check_letter = set()
    letters = {}
    x = 0
    y = 0
    checksum = 0
    for line in open(path):
        line = line.replace("\n", "")
        for letter in line:
            if letter not in check_letter:
                letters[letter] = 1
                check_letter.add(letter)
            else:
                letters[letter] += 1
        for letter in line:
            if letters[letter] == 2:
                x += 1
                break
        for letter in line:
            if letters[letter] == 3:
                y += 1
                break
        letters.clear()
        check_letter.clear()
    checksum = x * y
    print(checksum)


if __name__ == "__main__":
    main()