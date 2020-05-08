n_of_times = int(input())
inp_list = []
output = 0

for _ in range(1, n_of_times + 1):
    inp_str = input()
    inp_list.append(inp_str.split())
for i in inp_list:
    output += float(i[0]) * float(i[1])
print("{0:.3f}".format(output))