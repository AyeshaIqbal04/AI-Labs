#program 1:
for el in range(1500,2701):
    if el%7==0 and el%5==0:
        print(el)

#program 2:
def F_to_C(f):
    c=(f-32)/1.8
    return c
def C_to_F(c):
    f=c*1.8 + 32
    return f
f=float(input("Enter temperature in Fahrenheit: "))
c=float(input("Enter temperature in Celcius: "))
c2=F_to_C(f)
f2=C_to_F(c)
print(f"{c}°C is {f2} in Fahrenheit")
print(f"{f}°F is {c2:.1f} in Celsius")

#program 3:
import random
rand_no=random.randint(1,9)
print("random no is:",rand_no)
nmbr=int(input("Enter guess: "))
while rand_no!=nmbr:
    nmbr=int(input("Your guess is wrong, Enter again: "))
else:
    print("Well guessed!")

#program 4:
z=1
for i in range(5):
    for j in range(z):
        print("*",end=" ")
    z=z+1
    print("")
z=z-2
for i in range(4):
    for j in range(z):
        print("*",end=" ")
    z=z-1
    print("")   

#program 5:
word=input("Enter a word: ")
a=len(word)-1
rev=""
for i in range(len(word)):
    rev=rev+word[a]
    a=a-1
print("Reversed word is:",rev)

#program 6:
start=int(input("Enter start of series: "))
end=int(input("Enter end of series: "))
even=0
odd=0
for i in range(start,end+1):
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("No. of even numbers:",even,"No. of odd numbers:",odd)

#program 7:
li=[1,2.3,"w3resource",None,True,1+2j,[1,2,3],{"class":'V',"section":'A'},(0,-1)]
for i in range(len(li)):
    print(li[i], "has datatype", type(li[i]))

 #program 8:
for i in range(7):
    if(i==3 or i==6):
        continue
    print(i,end=" ")
print("") 

#program 9:
x=0
y=1
z=x+y
print(x,y,end=" ")
while z<=50:
    print(z,end=" ")
    x=y
    y=z
    z=x+y
print("")

#program 10:
for i in range(1,51):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)

 #program 11:
row=int(input("Enter Row no:"))
col=int(input("Enter Col no:"))
list=[]
for i in range(row):
    list.append([])
    for j in range(col):
        v=int(input("Enter a number: "))
        list[i].append(v)
print(list)    

#program 12:  
lines=[]
line=input("Enter a line: ")
while line!="":
    lines.append(line)
    line=input("Enter a line: ")
for i in lines:
    print(i.lower())

 #program 13:
binary=input("Enter a series of 4 digit binary numbers with commas: ")
binary=binary.split(',')
li=[]
for i in binary:
    j=int(i,2)
    if j%5==0:
        li.append(i)
print(li)   

#program 14:
string=input("Enter a string: ")
letters=0
digits=0
for i in string:
    if i>='a' and i<='z' or i>='A' and i<='Z':
        letters=letters+1
    elif i>='0' and i<='9':
        digits=digits+1
    else:
        continue
print("Letters:",letters)
print("Digits:",digits)

#program 15:
upper_alphabets=0
lower_alphabets=0
digits=0
special_charac=0
password=input("Enter a password:")
for i in password:
    if i>='a' and i<='z':
        lower_alphabets=lower_alphabets+1
    elif i>='A' and i<='Z':
        upper_alphabets=upper_alphabets+1
    elif i>='0' and i<='9':
        digits=digits+1
    elif i=='$' or i=='#' or i=='@':
        special_charac=special_charac+1
if(len(password)>=6 and len(password)<=16 and lower_alphabets!=0 and upper_alphabets!=0 and digits!=0 and special_charac!=0):
    print("Password is valid.")
else:
    print("Password is invalid.")