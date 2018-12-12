def main():
    path = "/Users/Stanisław/PycharmProjects/AdventOfCode/3_1/input.txt"
    field = [[0 for w in range(1000)] for h in range(1000)]

    for line in open(path):
        line = line.replace("\n", "")
        line = line.replace(" ", "")
        x = int(line[line.index("@")+1:line.index(",")])
        i = int(line[line.index("@")+1:line.index(",")])
        y = int(line[line.index(",")+1:line.index(":")])
        j = int(line[line.index(",") + 1:line.index(":")])
        width = int(line[line.index(":")+1:line.index("x")])
        height = int(line[line.index("x")+1:])
        while y < j+height:
            while x < i+width:
                if field[x][y] == 0:
                    field[x][y] = 1
                elif field[x][y] == 1:
                    field[x][y] = 2
                else:
                    x += 1
                    continue
                x += 1
            x -= width
            y += 1

    no_overlap = 0

    for line in open(path):
        line = line.replace("\n", "")
        line = line.replace(" ", "")
        x = int(line[line.index("@") + 1:line.index(",")])
        i = int(line[line.index("@") + 1:line.index(",")])
        y = int(line[line.index(",") + 1:line.index(":")])
        j = int(line[line.index(",") + 1:line.index(":")])
        width = int(line[line.index(":") + 1:line.index("x")])
        height = int(line[line.index("x") + 1:])
        while y < j + height:
            while x < i + width:
                if field[x][y] == 1:
                    no_overlap += 1
                    if no_overlap == width*height:
                        print(line)
                        break
                else:
                    no_overlap = 0
                    break
                x += 1
            x -= width
            y += 1


if __name__ == "__main__":
    main()