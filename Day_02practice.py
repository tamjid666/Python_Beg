"""
a = 10 
b = 20
print("Complex form of ",b," is : ",complex(b))
#string manupulation
a,b,c = 10,20,30
print(b)
def myfunc():
    b = 40
    print(b)
myfunc()
print(b)
""""""
# name = my name , abdullah al , tamjid 
# print(len(name))
import sys
import random

# print(sys.version)
# print(random.randrange(1,50))
val = random.randrange(1,10)
f = True
cnt = 0 
while(f):
    a = print("Enter Your Value : ",end = '')
    a = int(input())
    if a == val :
        print("Correct !")
        f = False
    else :
        cnt += 1
        if a > val :
            print("value is less than your value")
        else:
            print("Value is greater than your value")
print("You're Point is " ,cnt)
"""

a = "There are to many types of people"
b = "tamjid"
print("many" in a)
print("tamjid" not in a)
if b in a : 
    print("Yes")
else:
    print("NO")