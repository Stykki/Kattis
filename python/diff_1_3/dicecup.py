inp = input().split()
die_1 = int(inp[0])
die_2 = int(inp[1])

if die_1 >= die_2:
    biggest = die_1
else:
    biggest = die_2

sides1_list = [i for i in range(1, die_1 + 1)]
sides2_list = [i for i in range(1, die_2 + 1)]

every_pos = []

for i in sides1_list:
    for x in sides2_list:
        tuttla = i, x
        every_pos.append(tuttla)

sum_lst = []

for i in every_pos:
    sum_lst.append(sum(i))
    sum_lst.sort()

counter = 0
prev_count = 0
print_lst = []
for i in range(1, biggest * 2 + 1):
    counter = sum_lst.count(i)
    if counter > prev_count:
        print_lst = [i]
        prev_count = counter
    elif counter == prev_count:
        print_lst.append(i)
        prev_count = counter



for i in print_lst:
    print(i)