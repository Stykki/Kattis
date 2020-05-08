import calendar

inp = input().split()
day = int(inp[0])
month = int(inp[1])

dayz = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
day = calendar.weekday(2009, month, day)

print(dayz[day])