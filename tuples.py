from types import CoroutineType

a=(1,2,3,4,5,6,7,8,9,10)

b=a[::-1]
print(b)


my_tuple="Max",28,"Boston"
name,age,City=my_tuple                             
print(name)
print(age)
print(City)

my_tuple=(0,1,2,3,4)

i1 * i2,i3 *my_tuple

print(i1)
print(i3)
print(i2)



coordinates = [(4,5), (6,7), (80,34)]
print(coordinates[2])

prime_numbers = [2,3,5,7,11,13,17]

perfect_squares = (1,4,9,16,25,36)

print("# primes = ", len(prime_numbers))
print("# squares = ", len(perfect_squares))


for p in prime_numbers:
 print("prime: ", p)
for n in perfect_squares:
 print("square: ", n)

print("list methods")
print(dir(prime_numbers))
print(80*"-")
print("Tuple methods")
print(dir(perfect_squares))

import sys

list_eg = [1,2,3, "a", "b", "c", True, 3.14159]
tuple_eg = (1,2,3, "a", "b", "c", True, 3.14159)

print("list size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))


import timeit

list_test = timeit.timeit(stmt="[1,2,3,4,5]",number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)",number=1000000)

print("List time: ", list_test)
print("Tuple time: ", tuple_test)



empty_tuple = ()
test1 = ("a",)
test2 = ("a", "b")
test3 = ("a", "b", "c")

print(empty_tuple)
print(test1)
print(test2)
print(test3)

test1 = 1,
test2 = 1,2
test3 = 1,2,3

print(test1)
print(test2)
print(test3)

print(type(test1))
print(type(test2))
print(type(test3))

(age, country, knows_python)
survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age =", age)
print("Country =", country)
print("Knows Python?", knows_python)

survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2
print("Age =", age)
print("Country =", country)
print("Knows_Python?", knows_python)

country = ("Australia",)
print(country)

