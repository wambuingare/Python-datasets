
mydict={"name":"Mary","age":26,"city":"New York"}
print(mydict)

mydict2=dict(name="Jane",age=23,city="Mexico")
print(mydict2)

value=mydict["name"]
print(mydict)

value=mydict2["name"]
print(mydict2)


def product ():
    product=[10,15,3,2]
    p=1
    for b in product:   
        p*=b
        print(p)

def numbers ():
    w=range(1,50)
    for num in w:
        if num %7==0:
         print(num)

         
def product ():
    q=[20,25,4,2]
    product=1
    for i in q:
        product*=i
        print(product)

def count ():   
        n=input("pythonlobby")
        count=0
        for i in range(len(n)):
             count=count + 1
        print(count)

num=[23,24,54,34]
for i in range(len(num)):
     print(num[i],end=" ")

number=[23,34,'hello',32,56]
count=0
for i in range(len(number)):
    count+=1
    print(len(number))

def rev(q):
        q.reverse()
        return q

num=[23,34,'hello',32,56]
print(rev(num))

num=[1,2,3,4,5]
for i in range(len(num)):
 y=num[i]*num[i]
print(y,end='')

num=["Hello",34,45,"""""",40]
while(40 in num):
    num.remove(40)
    print(num)

