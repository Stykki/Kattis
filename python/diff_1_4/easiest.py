n = input()

while n != "0":
    sum_of_n = 0
    sum_lst = []
    for i in n:
        sum_of_n += int(i)
    for x in range(11, 1000000):
        xn = int(n) * x
        sum_of_xn = 0
        for ligma in str(xn):
            sum_of_xn += int(ligma)
        if sum_of_xn == sum_of_n:
            sum_lst.append(x)
            break
    print(sum_lst[0])
    n = input()
    