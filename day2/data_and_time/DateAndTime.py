import time

print(time.localtime())
# print(time.time())


#current local time in readable formate
currenttime = time.asctime(time.localtime())
print()
print(currenttime)

