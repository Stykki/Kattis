

flag = 0
for i in range(0, 5):
    inp = input()
    if 'FBI' in inp:
        print(i + 1)
        flag = 1

if flag == 0:
    print("HE GOT AWAY!")