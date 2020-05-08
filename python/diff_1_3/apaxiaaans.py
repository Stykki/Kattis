inp = input()

last_char = ""
output = ""

for i in inp:
    current_char = i
    if current_char != last_char:
        output += i
    last_char = current_char
print(output)

