def main():
    path = "/Users/Stanisław/PycharmProjects/AdventOfCode/2018/3_1/input.txt"
    write_path = "/Users/Stanisław/PycharmProjects/AdventOfCode/2018/3_1/output.txt"
    file = open(write_path, "w+")
    field = [[0 for w in range(1000)] for h in range(1000)]
    sqr_inches_of_fabric_2_or_more_claims = 0

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
                    sqr_inches_of_fabric_2_or_more_claims += 1
                else:
                    x += 1
                    continue
                x += 1
            x -= width
            y += 1
    print(sqr_inches_of_fabric_2_or_more_claims)

    line = ""
    for h in range(1000):
        for w in range(1000):
            line += str(field[h][w])
        file.write(str(line) + "\n")
        line = ""
    file.close()


if __name__ == "__main__":
    main()