#A set is a collection which is unordered, unchangeable*, and unindexed.
#Duplicate not*** allowed [n.b. except ture,false,0,1]
thisset = {"apple","banan"}
print(type(thisset))

thisset.add("Hi")
print(thisset)

name = {"tamjid","sanjid"}

thisset.update(name)
print(thisset)

#add any type of value 
mylist = ["hurreh ","value"]

thisset.update(mylist)
print(thisset)

thisset.remove("tamjid")#if "tamjid" not exist it's throw error
thisset.discard("banan")
thisset.pop()
print(thisset)
thisset.clear()
print(thisset)
del thisset