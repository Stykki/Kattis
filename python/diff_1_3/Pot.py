n_of_times = int(input())


output = 0
for _ in range(1, n_of_times + 1):
    inp_str = input()
    last_char = inp_str[-1]
    inp_str = inp_str[:-1]
    output = output + int(inp_str) ** int(last_char)

print(output)