import math
usr_inp = input()
usr_inp_lst = usr_inp.split()
pythagoras = math.sqrt(int(usr_inp_lst[1]) ** 2 + int(usr_inp_lst[2]) ** 2)
for _ in range(0, int(usr_inp_lst[0])):
    lengt = int(input())
    if lengt <= pythagoras:
        print("DA")
    else:
        print("NE")
    