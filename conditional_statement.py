#conditional statement :-It is used to make decisions.
# Types of conditional statement:- 4 types
#1.if statement :- used when there is only one conditiion.
#eg1.
age=20
#age=int(input("Enter your age : "))
if age>=18:
    print("You can vote")

#eg.2:-Write a program using only if statements to check: If number is positive, If number is negative, If number is zero

number=int(input("Enter number : "))
if number>0:
    print('Positive number')
if number<0:
    print('Negative number')
if number==0:
    print("Zero")

#eg.3:-Write a program using only if:If number is divisible by 3,If number is divisible by 5,If number is divisible by both 3 and 5

number=15
if number%3==0:
    print('Number is divisible by 3')
if number%5==0:
    print('Number is divisible by 5.')
if number%3==0 and number%5==0:
    print('Number is divisible by 3 and 5 both.')

#eg.4:-Input a single character. Using only if, check:If it is a vowel,If it is a consonant,If it is a digit,If it is a special character

char1 = 'e'
if char1 in 'aeiouAEIOU':
    print('It is a vowel')
if char1.isalpha() and char1 not in 'aeiouAEIOU':
    print('It is a consonant')
if char1.isdigit():
    print('It is a digit')
if not char1.isalnum():
    print('It is a special character')

    '''Note:- isalpha() → check letters
              isdigit() → check numbers
              isalnum() → letters or numbers'''
    
#5. Input three sides a, b, c. Using only if, check:If triangle is possible
#(Rule: sum of any two sides > third side)

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
if (a + b > c) and (b + c > a) and (c + a > b): # Check if triangle is possible
    print("Triangle is possible")
if not ((a + b > c) and (b + c > a) and (c + a > b)): # Check if triangle is not possible
    print("Triangle is not possible")  #output(5,3,4) - Triangle is possible


#2.if-else statement :- used when there are two choices.

#eg.1:- wap to check number is greatest and smallest.
a=6#int(input("Enter number for a :- "))
b=2#int(input("Enter number for b :- "))
if a>b:
    print("a is greatest")
else:
    print("b is smallest")

#eg.2:- 1. ATM Withdrawal (Nested Logic)Write a program that:
#Takes account balance and withdrawal amount
#Allows withdrawal only if:withdrawal amount is less than or equal to balance and
#withdrawal amount is a multiple of 100,Otherwise print proper message using if–else

balance=100000
withdrawl_amount=int(input("Enter amount for withdrawl.."))
if withdrawl_amount <= balance and withdrawl_amount % 100==0:
    print("withdrawl successful")
else:
    print("Insufficient balance")

#eg.2:-2. Electricity Bill (Slab-wise)-Write a program to calculate electricity bill:
#0–100 units → ₹1 per unit,101–200 units → ₹2 per unit,201–300 units → ₹3 per unit
#Above 300 units → ₹5 per unit
units = int(input("Enter units: "))

if units < 0:
    print("Invalid units")

elif units <= 100:
    bill = units * 1
    print(bill)

elif units <= 200:
    bill = (100 * 1) + (units - 100) * 2
    print(bill)

elif units <= 300:
    bill = (100 * 1) + (100 * 2) + (units - 200) * 3
    print(bill)

else:
    bill = (100 * 1) + (100 * 2) + (100 * 3) + (units - 300) * 5
    print(bill)


#3.if-elif-else statement:-Used when there are multiple conditions
#eg.1:- Check number is positive, negative, or zero.
number=int(input("Enter number : "))
if number>0:
    print("number is positive")
elif number<0:
    print("number is negative")
elif number==0:
    print('number is zero')
else:
    print("Thank you")

#eg.2:- 1. Grade System (Strict Rules)
#Write a program to input marks (0–100) and print grade:90–100 → A+ ,80–89 → A,
#70–79 → B, 60–69 → C ,35–59 → Pass, Below 35 → Fail, Any other value → Invalid marks

marks=int(input("Enter your marks"))
if marks>=90 and marks<=100:
    print('A+')
elif marks >=80 and marks<=89:
    print('A')
elif marks>=70 and marks<=79:
    print('B')
elif marks>=60 and marks<=69:
    print('C')
elif marks>=35 and marks<=59:
    print('Pass')
elif marks<35:
    print('Fail')
else:
    print('Invalid marks')

#eg.3:-2. Income Tax Calculator (Slab-wise)-Write a program to calculate income tax:
#Income ≤ 2,50,000 → No tax, 2,50,001–5,00,000 → 5%,5,00,001–10,00,000 → 20%
#Above 10,00,000 → 30%

print("     Income Tax Calculator    ")
income=int(input("Enter your income : "))
net_income=0
if income<=250000:
    print("No tax")
elif income>25000 and income<=500000:
    print(income*0.05)
    print(net_income=income-income*0.05)
elif income>=500001 and income<=1000000:
    print(income*0.020)
elif income>=1000000:
    print(income*0.030)
else:
    print("")



#4.Nested if statement