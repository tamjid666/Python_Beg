a = [x for x in range(10)]
print(a)
a.sort(reverse = True)
print(a)

def myfunc(n) :
    return abs(n-3)
#Sort the list based on how close the number is to 3:
a.sort(key = myfunc)
print(a)

b = ["Banana","Apple","aunt","banana"]
# b.sort()
b.sort(key = str.lower)
print(b)

c = b.copy()
d = b[:]
print(c)
print(d)