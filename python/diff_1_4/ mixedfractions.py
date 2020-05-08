

inp = input()
while inp != "0 0":
    first_num, second_num = inp.split()
    x = int(first_num) // int(second_num)
    y = int(first_num) % int(second_num)
    print("{} {} / {}".format(x, y, second_num))

    inp = input()