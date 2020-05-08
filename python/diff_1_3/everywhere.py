tst_case =int(input())

for _ in range(0, tst_case):
    tripz = int(input())
    place_list = []
    for _ in range(0, tripz):
        place_list.append(input())
        place_sort = set(place_list)
    print(len(place_sort))