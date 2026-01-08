#Simple- only for basic understanding.

def calculator(a,b):
    print('Sum=',a+b)
    print('Sub=',a-b)
    print('multiply=',a*b)
    print('Div=',a/b)
calculator(100,20)

#2nd method.
def calculator(x,y):
    return x+y,x-y,x*y,x/y
calculator(10,5)

#3rd method
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    if y==0:
        return 'cannot divide by 0. '
    return x/y

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4):"))
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if choice == 1:
    print("Result:", add(x,y))
elif choice == 2:
    print("Result:", sub(x,y))
elif choice == 3:
    print("Result:", mult(x,y))
elif choice == 4:
    print("Result:", div(x,y))
else:
    print("Invalid choice")


    