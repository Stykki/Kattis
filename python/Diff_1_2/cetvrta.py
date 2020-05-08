in1 = input()
in2 = input()
in3 = input()
in_list = []
in_list.append(in1.split())
in_list.append(in2.split())
in_list.append(in3.split())
list1 = []
list2 = []

str_to_print = ""

for i in in_list:
    list1.append(i[0])
    list2.append(i[1])

for i in list1:
    counter = list1.count(i)
    if counter == 1:
        str_to_print += i + " "


for i in list2:
    counter = list2.count(i)
    if counter == 1:
        str_to_print += i
print(str_to_print)