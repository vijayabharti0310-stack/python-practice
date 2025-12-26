#Operator:-----
#What is operator?
#An operator is a symbol used to perfom an operation.
#There are 7 main types of operators:-

'''1.Arithmetic - used for math operations.
eg: +,-,*,/,%,//(floor division),**(power)
2. Comparision - used to compare values.
eg: ==,!=,>,<,>=,<=
3. Assignment - used to assign values
eg: =,+=,-=,*=,/=
4.Logical - used for condition
Logical operator are used to combine conditions and make decisions in programs.
eg: and-both True, or-anyone True, not-reverse result
5.Membership - check pesence
in - present, not in-not present.
6.Identify operators- check same object.
eg: is- same object, is not- not same
7.Bitwise operators:- work on binary numbers.
eg: &-AND, ^-XOR, ~-NOT, <<-left shift, >>-right shift.
''' 

#5.Membership operator - check is this value present or not??
#python has two membership operators:-
 
#1.in operator:-checks whether a value exists.
#2.not in operator:- 
text="python"
print("p" in text)

greet='morning'
'g' in greet #output---True
'z' in greet #output---False

#membership operator in list
numbers=[10,20,30,40]
20 in numbers               #output -- True
60 in numbers               #output -- False

##membership operator in tuple
t=(1,2,3,4,5)
7 in t          #False
2 in t          #True
12 not in t     #True

## membership operator in dictionary
#In dictionary 'in' checks keys only, not values.
student={"Name":"Vijaya","Age":22}
print("Name" in student)                #output : True
print("Class" in student)               #output : False
print("Name" not in student)            #output : False



#6.Identify operators- check same object.:-1.is - same object 2. is not-not same
#is :-Checks identity → memory location is same or not. instead of ==
a = 10
b = 10
print(a is b)   #  True         'is used on =='

#is not :-Checks not same object.
x = 1000
y = 1000
print(x is not y)   # True

#
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True (same values)
print(a is b)   # False (different boxes)






