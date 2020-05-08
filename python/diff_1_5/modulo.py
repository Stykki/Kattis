

the_set = set()
for _ in range(10):
    x = int(input())
    the_set.add(x%42)


print(len(the_set))