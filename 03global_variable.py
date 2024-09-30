"""
x = "tamjid" #that is global

def myfunc():
    x = "awsome" #that is local 
    print("Python is " , x )
myfunc()

print(x)
"""
x = 'awsome'
def myfunc():
    global x 
    x = "tamjid"
myfunc()

print("Python is " + x )