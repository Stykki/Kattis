
owned, found, cost = input().split()

cans = int(owned) + int(found)
sodas = 0

while cans >= int(cost):
    sodas += cans // int(cost)

    mep = cans // int(cost)
    mep += cans % int(cost)
    cans = mep


print(sodas)
