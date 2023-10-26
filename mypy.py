'''for x in range (2,20,2):
    print(x)
yusuf=5
while yusuf<10:
    print(yusuf)
    yusuf+=1
magic_number=1401
x=0
while x < 1500:
    if (x==magic_number):
        print('magic number founded')
        print(magic_number,"is the magic number")
        break
    else:
        print(x)
        x+=1
for x in range (101):
    if(x%4==0):
        print(x,'is a multiple of 4')
numbers=[2,6,12,14,1,19]
for x in range(21):
    if x in numbers:
        continue
    print(x)
allowed =age_allowed(17)
print(allowed)
def age_allowed(my_age):
    girl_age=my_age/2+7
    return girl_age
for i in range(15,62):
    allowed=age_allowed(i)
    print("@ age",i,"you are allowed to date girl that are",allowed,"and older")
def gender(sex='Unknown'):
    if sex=='m':
        sex='male'
    elif sex=='f':
        sex='female'
    print(sex)
gender('m')
gender('f')
gender()
a=4123
def corn():
    print(a)
def rice():
    print(a)
def flex_arg(*args):
    total=0
    for h in args:
        total+=h
    print(total)
flex_arg(2,4,5,1)
def health(age=0,apple=0,cigrate=0):
    answer=(100-age)+(apple*3.5)-(cigrate*2)
    return answer
print("Enter ur age:")
age=input(("<<<<<"))
print("Enter number of apple eaten")
apple=input(("<<<<<<"))
print("Enter number of cigrates taken")
cigrate=input(("<<<<<"))
print(health(age,apple,cigrate))
def health(age=0,apple=0,cigrate=0):
    answer=(100-age)+(apple*3.5)-(cigrate*2)
    print(answer)
print("Enter age")
age=0-0
age==input(("<<<<<"))
print("Enter apples")
apples=0-0
apples==input(("Enter number  of apples eaten"))
print("Enter number of cigrates smacked")
cigrates=0-0
cigrates==input(("<<<<<<"))
health(age,apples,cigrates)
## Set
groceries={'Rice','Beans','Yam','Plantain','Pie','Porridge','Yam'}
print("Item to be searched...")
item=input(("<<<<<"))
for a in groceries:
    if a== item:
        print("item available")
        break
    else:
        print("Not found in",groceries)
categories={"Yusuf":" A simple guy","Dada":" A small brat","Abdul":" likes plenty babes"}
print(categories)
print(categories["Yusuf"])
for k,v in categories.items():
    print("the value of:",k,"is",v)
import tun
tun.fish()
import random
x = random.randrange(1,7)
for n in range(25):
    x = random.randrange(1,7)
    print(x)'''
## File creation
fw=open('file.txt','w')
fw.write('writing to a file\n')
fw.write('this is the new line\n')
fw.close()
fr=open('file.txt','r')
text=fr.read()
fr.close()
print(text)