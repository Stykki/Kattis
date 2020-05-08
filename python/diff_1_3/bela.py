usr = input().split()
suit = usr[1]

score_dom_list = [11, 4, 3, 20, 10, 14, 0, 0]
score_reg_list = [11, 4, 3, 2, 10, 0, 0, 0]
loc_list = ["A", "K", "Q", "J", "T", "9", "8", "7"]

output_score = 0

for _ in range(0, int(usr[0])*4):
    inp = input()
    where = loc_list.index(inp[0])
    if inp[1] == suit:
        output_score += score_dom_list[where]
    else:
        output_score += score_reg_list[where]

print(output_score)