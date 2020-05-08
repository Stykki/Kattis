
inp = 1
inp = int(input())

while inp >= 0:
    prev_time = 0
    distance = 0
    for i in range(0, inp):
        speed, time = input().split()
        realtime = int(time) - prev_time
        prev_time = int(time)
        distance += realtime * int(speed)
    print(distance, "miles")
    inp = int(input())