a = ("hey","hi")
(unpack1,unpack2) = a #no of variable must match with # of tuple
print(unpack1)

(green,*yellow) = a
print(green)
print(yellow)

tuple1 = ('a','b','c')
tuple2 = (1,2,3,1)

tuple3 = tuple1 + tuple2
print(tuple3)

mytup = 2*tuple1
print(mytup)
tupel1 = (1, 2, 3, 1, 4, 1)  # Example tuple
print(tupel1.count(1))  # Counts the number of times '1' appears in 'tupel1'

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found