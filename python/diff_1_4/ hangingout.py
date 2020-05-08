
firesft, cases = input().split()


terrance_count = 0
reject_count = 0
for _ in range(int(cases)):
    ent_ex, amt = input().split()
    amt = int(amt)

    if ent_ex == "enter":
        if (amt + terrance_count) > int(firesft):
            reject_count +=1
        else:
            terrance_count += amt

    else:
        terrance_count -= amt
print(reject_count)

