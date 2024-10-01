a = "tamjid"
b = "abdullah"
c = b + " " + a 
print(c)

age = 36
#wrong : txt = "My name is Jogn , I am " + age
#correct : txt = "My name is Jogn , I am " + str(age) 
txt = f"My name is John,I am {age}" #calld f-string
print (txt)

price = 50
txt = f"the price is {price:.2f}"
print(txt)

a , b = 20 , 30
print(f"ther price of {a*b:.2f}") 

d = 1
print(d,"\t")