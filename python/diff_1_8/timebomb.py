

def get_lines():
    line_list = []
    for i in range(5):
        line = input()

        count = 0
        ret_str = ""
        for i in range(len(line)):
            count += 1
            if count >= 0:
                ret_str += str(line[i])
            if count % 3 == 0 and count != 0:
                line_list.append(ret_str)
                ret_str = ""
                count = -1


    return line_list

lines = get_lines()
for i in lines:
    print(i)