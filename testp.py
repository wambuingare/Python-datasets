l = [None] * 10
print(len(l))

aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)

n = [None] * 20
print(len(n))

resList = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
print(resList)

resList = [y+x for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
print(resList)

aList = [1, 2, 3, 4, 5, 6, 7]
pow2 =  [2 * x for x in aList]
print(pow2)

sampleList = [10, 20, 30, 40]
del sampleList[0:6]
print(sampleList)

my_list = ["Hello", "Python"]
print("-".join(my_list))

sampleList = [10, 20, 30, 40, 50]
sampleList.append(60)
print(sampleList)

sampleList.append(60)
print(sampleList)

aList = [5, 10, 15, 25]
print(aList[::-2])

sampleList = [10, 20, 30, 40, 50]
sampleList.pop()
print(sampleList)

sampleList.pop(2)
print(sampleList)

aList = ["PYnative", [4, 8, 12, 16]]
print(aList[0][1])    
print(aList[1][3])

aList = [10, 20, 30, 40, 50, 60, 70, 80]
print(aList[2:5])
print(aList[:4])
print(aList[3:])

list1 = ['xyz', 'zara', 'PYnative']
print (max(list1))

aList = ['a', 'b', 'c', 'd']

sampleList = [10, 20, 30, 40, 50]
print(sampleList[-2])
print(sampleList[-4:-1])

listOne  =  ['a', 'b', 'c', 'd']
listTwo =  ['e', 'f', 'g']

aList = [4, 8, 12, 16 ,20,24,28]
h=aList[-6:-2] 
print(h)

l=[1,2,3,4]
x=l.pop()
print(x)
















