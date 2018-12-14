def main():
    path = "/Users/Stanisław/PycharmProjects/AdventOfCode/2018/2_1/input.txt"
    input_line = {}
    index = 0
    i = 0
    y = 1
    diff = 0
    similarity = ""

    for line in open(path):
        line = line.replace("\n", "")
        input_line[index] = str(line)
        index += 1
    for x in range(250):
        for y in range(250):
            while i < 26:
                if input_line[x][i] == input_line[y][i]:
                    similarity += input_line[x][i]
                    if i == 25:
                        if diff == 1:
                            print(similarity)
                            break
                    i += 1
                    continue
                else:
                    diff += 1
                    if diff >= 2:
                        break
                i += 1
            similarity = ""
            y += 1
            i = 0
            diff = 0
            if y >= 250:
                break
        x += 1
        y = 0
        if x >= 250:
            break


if __name__ == "__main__":
    main()