import math

inp_num = input()
inp_list = inp_num.split()
m = int(inp_list[0])
pepsi = int(inp_list[1])

outp = m / math.sin(math.radians(pepsi))

outp = math.ceil(outp)
print(outp)