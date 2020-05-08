l = input()
d = input()
x = int(input())

output_list = []


for i in range(int(l), int(d)+1):
    sum_of_i = 0
    for lettr in str(i):
        sum_of_i += int(lettr)

    if sum_of_i == x:
        output_list.append(i) 
print("{}\n{}".format(output_list[0], output_list[-1]))
