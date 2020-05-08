
def get_inp(amt):
    ret_list = []
    for _ in range(amt):
        ret_list.append(input())

    return ret_list


amount = int(input())

numbers_list = get_inp(amount)

for item in numbers_list:
    print(len(item))