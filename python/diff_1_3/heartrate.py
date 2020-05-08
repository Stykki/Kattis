n_of_times = int(input())

for _ in range(0, n_of_times):
    b_inp = input().split()
    beats = int(b_inp[0])
    sec = float(b_inp[1])
    abpm = 60/sec
    bpm = (60*beats) / sec
    lower = bpm - abpm
    higher = bpm + abpm
    print("{:.4f} {:.4f} {:.4f}".format(lower, bpm, higher))