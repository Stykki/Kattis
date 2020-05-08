all_lines = []

for i in range(4):
    line = input().split()
    xline = [int(i) for i in line]
    all_lines.append(xline)

def eggs(twofour):
    userinp = input()

    if userinp == "0":
        #left
        twofour = left_move(twofour)

    if userinp == "1":
        #right
        twofour = up_move(twofour)

    if userinp == "2":
        twofour = right_move(twofour)

    if userinp == "3":
        twofour = down_move(twofour)
        twofour = down_move(twofour)
        twofour = down_move(twofour)

    print_two_four(twofour)


def print_two_four(lst):
    for sublist in lst:
        x = ""
        for item in sublist:
            x += str(item) + " "
        print(x)
        


def down_move(twofour):
    for x in range(3, 0, -1):
        change = True
        while change:
            change = False
            for z in range(3, -1, -1):
                if twofour[x][z] == twofour[x-1][z] or twofour[x][z] == 0:
                    if not (twofour[x][z] == 0 == twofour[x-1][z]):
                        twofour[x][z] += twofour[x-1][z]
                        twofour[x+-1][z] = 0
                        change += 1
    return twofour


def up_move(twofour):
    for z in range(4):
        change = True
        while change:
            change = False
            for x in range(0, 3):
                if twofour[x][z] == twofour[x+1][z] or twofour[x][z] == 0:
                    if not (twofour[x][z] == 0 == twofour[x+1][z]):
                        twofour[x][z] += twofour[x+1][z]
                        twofour[x+1][z] = 0
                        change += 1
    return twofour



def left_move(twofour):
    #left
    for lines in twofour:
        change = True
        while change:
            change = False
            for x in range(0, 3):
                if lines[x] == lines[x+1] or lines[x] == 0:
                    if not (lines[x] == 0 == lines[x+1]):
                        lines[x] += lines[x+1]
                        lines[x+1] = 0
                        change += 1
    return twofour



def right_move(twofour):
    #left
    for lines in twofour:
        change = True
        while change:
            change = False
            for x in range(2, -1, -1):
                if lines[x] == lines[x+1] or lines[x+1] == 0:
                    if not (lines[x] == 0 == lines[x+1]):
                        lines[x+1] += lines[x]
                        lines[x] = 0
                        change += 1
    return twofour


eggs(all_lines)
