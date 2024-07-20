#While Loop

i=1
txt=int(input("enter a number for table: "))
n=txt
while i<=10:
    tab=i*n
    print("table of",n,"is",":",n,"*",i,"=",tab)
    i=i+1
    
   

#Single statement while block

#i= 0
#while (i==0): print("Hello World!")

#for in Loop

#Example 1
# Iterating over a list
print("List Iteration")
l = ["red", "blue", "green"] 
for i in l:
    print(i)
   
#Example 2
# Iterating over a tuple (immutable) 
print("Tuple Iteration")
t = ("geeks", "for", "geeks") 
for i in t:
    print(i)

#Example 3
# Iterating over a String 
print("String Iteration") 
s = "Hello!"
for i in s:
    print(i)

#Iterating by index of sequences
# Iterating by index
list = ["geeks", "for", "geeks"] 
for index in range(len(list)):
    print (list[index])

# Loop Control Statements

# Continue Statement
l="ILovePakistan"
for i in l:
    if i=='P' or i=='s':
        continue
    print("current letter is",i)
#Break Statement
l="Pakistan"
for i in l:
    if i=='P' or i=='s':
        break
print("current letter is",i)

#Python Functions

#Example
def my_function():
    print('Hello from a function')

my_function()

# Example
def my_function(fname):
    print(fname)
my_function("Ahmad")
my_function("Ali")

#Example
def my_function(country = "Pakistan"): 
    print("I am from " + country)
my_function("India") 
my_function() 
my_function("Brazil")

#Example
def my_function(n):
    for i in n: 
        print(i)
nmb = [1, 2, 3] 
my_function(nmb)

#Example
n=int(input('enter nmbr:'))
def my_function(x): 
    return n * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#Example
def sum(a,b):
    c=a+b
    return c    
print(sum(5,6))  

#Python Classes/Objects

#Example
class Car:
    color="blue"
    brand="mercedes"
c1=Car()
print(c1.color)
print(c1.brand)   

#The init () Function 

#Object Methods

class Car:
    def __init__(self,color,brand):
        self.color=color
        self.brand=brand
    def get_color(self):
        return self.color
    def get_brand(self):
        return self.brand
c1=Car("Ali",87)
print(c1.get_color(), " " ,end="")
print(c1.get_brand())  

print("Lab 2 end")    