a = ["apple","Banana"]

# for x in a : 
#     print(x)
# for i in range(len(a)) : 
#     print(a[i])
# i = 0 
# while i<len(a) :
#     print(a[i])
#     i+=1 
# [print(x) for x in a]

"""
list comparison
b = []
for x in a :
    if "pp" in x :
        b.append(x)
print(b)
b = [x for x in a if "pp" in x] #Syntex --> 
    #newlist = [expression for item in iterable if condition == True]
print(b)
c = [x for x in a if "pp" not in x]
d = [x for x in a if "pp" != x]
print(c)
print(d)
"""

# b = [x for x in range(5)]
# print(b)
# c = [x for x in range(10) if x%2==0]
# print(c)

# d = [x.capitalize() for x in a]
# print(d)
# b = ["hello" for x in a ]
# print(b)
b = [x if x != "apple" else "Orange" for x in a]
# "Return the item if it is not banana, if it is banana return orange".
print(b)