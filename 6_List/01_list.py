# food = ["apple",True,50,5+3j]
# print(food[-1])
# print(food[1:3])
# print(type(food))
# print(len(food))

# food[1:3] = [False,"Baaa"]
# print(food)
# food.append("House")#like vector.push_back()
# print(food)
# food.insert(1,"Orange")
# print(food)

# name = ["abdullah","al","tamjid"]
# food.extend(name)
# print(food)


# for x in food :
#     print(x)

# # list constructor
# thislist = list(("hey",2,3+1j))

# print(thislist)

# if "apple" in food : 
#     print("YES")

food = ["Orange","Apple"]
f2 = ("Banana")
f3 = ["Banana"]
food.extend(f2)
food.extend(f3)
print(food)
print(f2)

food.remove("B")
print(food)
food.pop(3)
food.pop()
print(food)

del food[0]
print(food)

# del food
# print(food)

food.clear()
print(food)