from time import time, ctime

print("Current time is " + ctime())
print("Current time in floating is " + str(time()))
x = time() + 20
print("Time after 20 sec is " + ctime(x))