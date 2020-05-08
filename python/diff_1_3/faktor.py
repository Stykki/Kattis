import math

usr_inp = input()
usr_list = usr_inp.split()
articl = int(usr_list[0])
imp_fact = int(usr_list[1])
x = 1

while True:
    if (math.ceil(x/articl)) == imp_fact:
        print(x)
        break
    else:
        x += 1