output = 0

for contestant in range(0, 5):
    usr_inp = input()
    usr_list = usr_inp.split()
    usr_output = 0
    for number in usr_list:
        usr_output = usr_output + int(number)
    if usr_output > output:
        output = usr_output
        cont_ant = contestant + 1

print("{} {}".format(cont_ant, output))

