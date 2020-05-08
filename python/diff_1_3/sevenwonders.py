usr_str = input()
T_count = 0
C_count = 0
G_count = 0


for letter in usr_str:
    if letter == "T":
        T_count +=  1
    elif letter == "C":
        C_count +=  1 
    else:
        G_count += 1

def get_lowest(g,t,c):
    if t >= g <= c:
        return g
    elif g >= t <= c:
        return t
    elif t >= c <= g:
        return c
    else:
        return 0

lowest = get_lowest(G_count, T_count, C_count)
output = (T_count ** 2) + (G_count ** 2) + (C_count ** 2) + 7 * lowest
print(output)