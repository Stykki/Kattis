cost = float(input())
yards = int(input())

w_l_list = []
output = 0

for _ in range(0, yards):
    w_l = input()
    w_l_list.append(w_l.split())

for i in w_l_list:
    output += float(i[0]) * float(i[1]) * cost

print("{0:.7f}".format(output))