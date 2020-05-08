inp = input()
inp_list = inp.split()

num1 = inp_list[0]
num2 = inp_list[1]

num1_flipped = int(num1[::-1])
num2_flipped = int(num2[::-1])

if num1_flipped > num2_flipped:
    print(num1_flipped)
else:
    print(num2_flipped)