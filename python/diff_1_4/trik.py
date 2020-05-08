swap = input()

location = 1

for letter in swap:
    if letter == "A":
        if location == 1:
            location += 1
        elif location == 2:
            location -= 1
    if letter == "B":
        if location == 2:
            location += 1
        elif location == 3:
            location -= 1
    if letter == "C":
        if location == 1:
            location += 2
        elif location == 3:
            location -= 2

print(location)