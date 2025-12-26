#Logical operator :- Logical operators are used to combine conditions and make decisions in program.
#There are 3 logical operators in Python: 1.and   2.or   3.not
#1. and operator:- Both conditions must be True
'''
| A     | B     | A and B | A or B |
| ----- | ----- | ------- | ------ |
| True  | True  | True    | True   |
| True  | False | False   | True   |
| False | True  | False   | True   |
| False | False | False   | False  |'''

a = 10
print(a > 5 and a < 20)   # True
print(a > 5 and a > 20)  # False

#2. or operator:- At least one condition must be True 

a = 10
print(a > 5 or a > 20)   # True
print(a < 5 or a > 20)  # False

#3. not operator:- Reverses the result

a = 10
print(not(a > 5))   # False
print(not(a < 5))   # True

#Write a program to check - a number is between 10 and 50 (inclusive).

a=20 #int(input("Enter number : "))
print(a>10 and a<50)

#Write a program to check a number is less than 0 OR greater than 100.
a=20#int(input("Enter number : "))
print(a<0 or a>100)

#Write a program to check age is eligible to vote (age ≥ 18 and citizen is "india").

age=int(input("Enter your age : "))
citizen=input("Enter your citizenship : ").lower()
print(age>=18 and citizen=='India')


