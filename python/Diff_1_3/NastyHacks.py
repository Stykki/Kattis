n_of_times = int(input())

for _ in range(1, n_of_times + 1):
    inp_str = input()
    inp_list = inp_str.split()
    r = int(inp_list[0])
    e = int(inp_list[1])
    c = int(inp_list[2])
    if (r + c) == e:
        print("does not matter")
    elif (r + c) < e:
        print("advertise")
    else:
        print("do not advertise")