usr_input = input()
usr_list = usr_input.split()
fizz_numb = int(usr_list[0])
buzz_numb = int(usr_list[1])
count = int(usr_list[2])



def print_check(num):
    print_str = ""
    if not num % fizz_numb:
        print_str += "Fizz"
    if not num % buzz_numb:
        print_str += "Buzz"
    if not print_str:
        print_str = num
    return print_str

for i in range(1, count + 1):
    str_to_print = print_check(i)
    print(str_to_print)