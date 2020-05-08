import math

n_of_times = int(input())

for _ in range(0, n_of_times):
    inp_str = input()
    fact = math.factorial(int(inp_str))
    print(str(fact)[-1])
