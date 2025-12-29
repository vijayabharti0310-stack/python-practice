#lambda:-Lambda is a small, one-line function in Python.
# It is used when you need a function for a short time.
#syntax:- lambda arguments:expression

#eg1:- square of 5.

a=5
square=lambda x:x**2
print(square(a))

#eg2:- short a list of string (fruits) based on their lengths.

fruits=['apple','pine apple','banana','cherry','date']
shorted_fruits=sorted(fruits, key=lambda x:len(x))
print(shorted_fruits)

#eg3:-shorted- short a list of string (animal) based on their length.

animals=['ape','buffalo','camel','donkey','elephant','fish']
short_animals=sorted(animals,key=lambda x:len(x))
print(short_animals)

#eg4:-filter- filter elements from a list based on specific condition.
my_list=[1,2,3,4,5,6]
even_numbers=list(filter(lambda x:x%2==0,my_list))
print(even_numbers)

#eg.5:-find odd numbers from a given list.
my_list=[6,7,8,9,10,11,12,13]
odd_numbers=list(filter(lambda x:x%2!=0,my_list))
print(odd_numbers)

#eg.6:-mapping-map() to apply a specific operation to each element of a list.
my_list=[1,2,3,4,5]
double=list(map(lambda x:x*2,my_list)) #here multiplication is going on , you can add, sub,mult,and div also.
print(double)

#eg.7:add 5 to each element of a list.
my_list=[1,2,3,4,5,6]
add=list(map(lambda x:x+5,my_list))
print(add)

#eg.8:-short the list of students based on their names.

students=[
    {'name':'Dlice','age':26},
    {'name':'Bob','age':19},
    {'name':'Charlie','age':21}
]
sorted_students=sorted(students,key=lambda x: x['name'])
print(sorted_students)

#eg.9:-Write a lambda expression to add two numbers.
a=6
b=10
add=lambda x,y:x+y
print(add(a,b))

#eg.10:-Using lambda with filter(), extract all numbers that are divisible by 3 ,but not divisible by 6

nums=[3,6,9,12,15,18,21]
result=list(filter(lambda x:x%3==0 and x%6!=0,nums))
print(result)

#eg.11:-Given a list of tuples, use lambda with sorted() to sort the list
#first by 2nd element (ascending) , #if same, then by 1st element (descending)

data = [(1, 3), (4, 1), (2, 1), (5, 3)]
sort_result = sorted(data, key=lambda x: (x[1], -x[0]))#Use negative value (-x[0]) for descending order
print(sort_result)

#eg.12:-Use lambda with reduce() to find the maximum number from a list.Do not use max()
from functools import reduce
nums = [12, 45, 7, 89, 23,99]
result=maximum = reduce(lambda a, b: a if a > b else b, nums)
print(maximum)

