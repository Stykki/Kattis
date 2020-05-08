n_of_times = int(input())

for _ in range(1, n_of_times + 1):
    num = int(input())
    if num % 2:
        print("{} is odd".format(num))
    else:
        print("{} is even".format(num))