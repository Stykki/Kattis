inp = input()

new_list = input().split()
new2_list = []

for item in new_list:
    if int(item) == -1:
        pass
    else:
        new2_list.append(int(item))

output = 0
for item in new2_list:
    output += item

output = output / len(new2_list)
print(output)