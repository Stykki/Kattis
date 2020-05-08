amnt = int(input())

for _ in range(0, amnt):
    inp1 = input()
    inp2 = input()
    output_str = ""
    for i in range(0, len(inp1)):
        if inp1[i] == inp2[i]:
            output_str += "."
        else:
            output_str += "*"
    print(inp1)
    print(inp2)
    print(output_str)
