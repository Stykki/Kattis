import re
imp = input()

list_of_3s = re.findall('...', imp)
list_of_3s_len = len(imp)

letter_count = 0

for item in list_of_3s:
    if item[0] == 'P':
        letter_count += 1
    if item[1] == "E":
        letter_count += 1
    if item[2] == "R":
        letter_count += 1

print(list_of_3s_len - letter_count)