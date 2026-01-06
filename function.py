#Date:- 06/01/2026

#function:- Function is a block of code that does a specific task and can be used again and again.
#Instead of writing the same code many times,we write it once in a function and call it whenever needed.
#why do we use function? 
#Code becomes short, Code becomes easy to understand, Code can be reused, Easy to fix errors.
#Types of funcion:- 1. Built in function- already provided by python. print(), len(), type(), input.
#2. User-defined function:- created by programmers. 3. Ananomous function- lambda, filter,map.

#Syntax:-
'''def function_name():
    statement.....'''

#eg:-simple

def greet():
    print("Hello! Good Morning Everyone ")
greet() #function call

#eg:-Function with parameters.

def greet(name):
    print('Hello ',name)
greet('Vijaya')
greet('Shweta')

#eg:-function with return value.

def add(a,b):
    return a+b
result=add(10,20)
print(result)

#eg:- function with default value.

def country(name,nation='India'):
    print(name,nation)
country('Vijaya')
country('John','USA')

#eg:- Function calling another function.

def add(a,b):
    return a+b
def multiply(x,y):
    return x*y
print(add(2,3))
print(multiply(4,5))

#recursion:- function call itself.

def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
fact(5)

#1.Find Square of a Number
def square(x):
    print('Square ' ,x*x)
square(5)
#or
def square(x):
    return x*x
square(5)

#2.Check Even or Odd
def even_odd(x):
    if x%2==0:
        return 'even'
    return 'odd'
even_odd(2)

#3.Find Maximum of Two Numbers

def max(x,y):
    if x>y:
        return 'X is greater'
    return 'Y is greater'
max(200,100)

#4.Find Length of String (without len)
def len_str(s):
    count=0
    for i in s:
        count+=1
    return count
len_str('vijaya')

#5.Factorial using Function
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
factorial(5)

#6.Check Prime Number

def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
prime_num(22)

#7.Sum of Digits
def sum_digits(n):
    sum=0
    for i in str(n):
        sum=sum+int(i)
    return sum
sum_digits(123509)

#8.Fibonacci Series (Nth term)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
fibonacci(12)

#9.count vowels in a string.

def count_vowels(s):
    count = 0
    for i in s.lower():
        if i in 'aeiou':
            count += 1
    return count
count_vowels('VIJAYA')

#10.Count digits using function
def count_dgt(n):
    count=0
    for i in range(len(str(n))):
        count=count+1
    return count
count_dgt(12345)
    
#11.Reverse number.
def reverse_number(n):
    rev=0
    for i in range(len(str(n))):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
reverse_number(123)


