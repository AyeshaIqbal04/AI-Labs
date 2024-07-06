#Print Statement

print("Hello World!")

#Comments in python

x=1 #Initial value of x is 1
print(x)

#Input/Output in python

txt=input("enter a string:")
print(txt)

#Multiple Statements on a Single Line

print("Statement 1"); print("Statement 2")

#Indentation

x=int(input("enter value of x:"))
if x>0:
    print("value of x is",x)
elif x<0:
    print("value of x is",x)
else:
    print("value of x is",x)

#Data types and Type casting

name="ayesha"
age=21
height=5.3
y=None
x=True
z=1+2j
print(type(name))
print(type(age))
print(type(height))
print(type(y))
print(type(x))
print(type(z))
a=2 ; b="3"
c=int(b)
sum=a+c
print("the sum is:",sum)

#Strings

str1="string start and end with double quotes"
print(str1)
str2='string start and end with single quotes'
print(str2)
str3="Number of day's in a week"
print(str3)
str4='There are "seven days" in a week'
print(str4)

#Special characters in strings

print("This is backslash \\ mark")
print("This is tab \t key")
print("These are \'single quotes\'")
print("These are \"double quotes\"")
print("This is a new line  \n NEW LINE")

#String indices

str="Artificial Intelligence"
print(str[3]) ; print(str[-8]) ; print(str[-19])

#Lists

new_list=["red",12,12.4,True]
print(new_list)

#List indices

color_list=["red","green","blue","yellow"]
print(color_list[2])
print(color_list[-4])

#List Slice

li=color_list[:3]
print(li)
l2=color_list[-3:-1]
print(l2)

print("Lab 1 complete")