inp = input()
inp2 = input().split()
amt = 0

for i in inp2:
    if int(i) < 0:
        amt += 1

print(amt)