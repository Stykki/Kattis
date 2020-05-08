import math
import datetime

end_point = int(input())

x = 0
b = 1
nuna = datetime.datetime.now()
for i in range(0, end_point+1):
    if i == 0:
        i = 1
    b *= i
    x += 1/b
    
#x = end_point / x

then = datetime.datetime.now()
print(x)
print(then - nuna)