for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')

print("\n")

amount = int(input("Stars amounts are: \n"))
number = 0
star = 0
"""
while number < amount:
    number += 1
    print("*")
"""
for i in range (star+1,amount):
    for j in range (i):
        print ("*", end='')
    print("\n")