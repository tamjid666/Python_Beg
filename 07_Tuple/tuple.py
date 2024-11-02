#A tuple is a collection which is ordered and unchangeable
#unchangeable mean no append or pop
#you can add two tupple
#allow duplicate values

mytuple = ("Apple","banana","cherry")
print(mytuple)

a = ("tamjid",)#one item tupel,remember the comma
print(type(a))
a = ("tamjid")
print(type(a))

thistuple = tuple(("apple","banana","cherry"))#note the double round -brackets
print(type(thistuple))
#value add this tupple
y = list(thistuple)
y.append("tamjid")
thistuple = tuple(y)
print(thistuple)

z = ("hey",)
mytuple += z 
print(mytuple)

del thistuple #delete whole tuple

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

    -->List is a collection which is ordered and changeable. Allows duplicate members.
    -->Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    -->Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    -->Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""