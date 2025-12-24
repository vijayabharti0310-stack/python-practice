#1. Get second item from list of dictionary.
items=[{"fruit":"apple","color":"red"},
       {"vegetables":"peas","color":'green'},
       {"grains":"wheat","color":"yellow"}]
print(items[1])

#2. Get first item from list of dictionary.
print(items[0])

#3. Get third item from tuple.
students = [("Navin", 80), ("shivam", 22), ("rahul", 34)]

for name, age in students:
    print(students[2])



#4. Api for - All crud apis for  Menu
    
#1. Get 2nd item from 2nd tuple.

tuples_list= [("g", "k"), ("l", "m"), ("n", "o")]
#for item in tuples_list:
print(tuples_list[1][1])
    

#2. Get last item from last tuple.
print(tuples_list[2][1])
#[("g", "k"), ("l", "m"), ("n", "o")]

#1. Get 3rd item from 3rd dictionary

i = 0
dicts_list=[{"name" : "gau", "age" : 20},
            {"name" : "pau", "age" : 20,"gender":"male"},
            {"name" : "hau", "age" : 20,"gender":"female"}]
d = dicts_list[2]
for item in d.items():  
    i += 1
    if i == 3:           
        print(item)

#2. Get name from 2nd dictionary

print(dicts_list[1]['name'])

#3. Get age from 3rd )dictionary

print(dicts_list[2]['age'])
#[{"name" : "gau", "age" : 20}, {"name" : "pau", "age" : 20, "gender" : "male"}, {"name" : "hau", "age" : 20, "gender" : "female"}]


#22/11/25
#l2 = [[3,4,5], [6,7,8]]
# 1.check if first list from l2  has 6 => 

l2 = [[3, 4, 5], [6, 7, 8]] # l2 is a list which has two lists inside it.
for i, x in enumerate(l2[0]): #for loop with enumerate function to get index and value of elements of first list inside l2.
    print(i, x)      # print index and value of list 1 inside l2.
    if x == 6:           # check value which is available in x is equal to 6 or not.
        print("6 is available in list 1") # if it is equal to 6 then it will print 6 is available in list 1.
        break  # this is used to stop searching
else:   # if x=6 is not available then else body execute given statement.
    print("6 is not available in list 1")
  
   

#** 2. check if second list has length of 4

l2 = [[3, 4, 5], [6, 7, 8]]         # l2 is a list of list ,two lists inside it.
count = 0       #count is a variable ,which initilise 0.
for i in range(len(l2[1])):         ##  for loop , i is a variable go through each element, i will print the length of list l2.
    print(i)  
    count += 1     # it will count elements one by one 
if count == 4:      #checks count is equals to 4, if it is 4 then print 2nd list has len 4
    print("Second list has length 4")
else:        # otherwise go to the else statement
    print("second list has not length 4.")      # then print 2nd list has not len 4



# 3. check if first list has 5 elements


l2 = [[3, 4, 5], [6, 7, 8]] # l2 is a list of lisst having integer values
count = 0  # count is a variable , o is initilize in it.
for i, x in enumerate(l2[0]): # for loop ,having two variables i(index) and x(value) 
    print(i,x) # it will print index and value 
    count += 1 # it will count steps one by one
if count == 5: # if is a cheaking condition which will check variable count is equals to 5 or not
    print("Yes, first list has 5 elements") # if count is equals to 5 then it will print...
else: #otherwise it will print given statement.
    print("No, first list does not have 5 elements")



# 4. Get 2nd element from 2nd list of l2

l2 = [[3, 4, 5], [6, 7, 8]] # tow list inside list l2,values are integers.
for i in range(len(l2[1])):   # loop through 2nd list len gives the llength of l2[1] which is 3 and range gives number like 0,1,2 means indexes
    if i == 1:                # will check the value of i is equals to 1
        print(l2[1][i]) #it will print l2's 2nd list's i which is 7
        break # thenn it will break


# 5.Get last element from 1st list of l2

l2 = [[3, 4, 5], [6, 7, 8]] # l2 is a lis of lists ,having integer values.
for i, x in enumerate(l2[0]): #for loop, i is a variable which is used to show index and x=values of 1st list of l2
    if i == len(l2[0]) - 1: # It checks whether the loop has reached the last index of the first list.
        print("Last element of first list is:", x) # then it will print element which is available at last index of 1st list
        break


#6. Add a new element in first list (1)

l2=[[3,4,5],[6,7,8]]
l2[0].append(1)
print(l2)

##or 
l2 = [[3, 4, 5], [6, 7, 8]]
for i in range(len(l2[0])): 
    print(l2[0])
    l2[0].append(1)  
    break          
print(l2)



# i have a list l2 with 2 lists inside it. in 2nd line i'm using append function to add new element 1 in list 1.
# in 3rd line printing the updated list l2, output will be [[3, 4, 5, 1], [6, 7, 8]].

#7. Add 3 in each element of 2nd list#

l2 = [[3, 4, 5], [6, 7, 8]]
for i in range(len(l2[1])):
    l2[1][i] += 3
print(l2)

#explanation: i have a list l2 with 2 lists . in 2nd line there is a for loop with range function which will iterate 
# over the length of 2nd list. in 3rd line each iteration 3 will be added to each elements of 2nd list.
#We mostly use range function inside loops when we want to repeat something a certain number of times.
#in last line printing the updated list l2.

#25/11/2025

#l1 = [[2,34], "saurav"] Aapko change third letter of data in l1 which datatype is String to k.


l1 = [[2, 34], "saurav"]
for i, value in enumerate(l1):  # accessing each element of l1 without using index
    print("What is inside list l1", l1)
    if type(value) == list:  # check the type of value - is it a list?
        for j, val in enumerate(value):  # will give index with value
            print(j, val)
    if type(value) == str:  # If the current item is a string then process the word
        word = value
        print("Datatype:", type(word))

        count_letters = 0   # Count letters
        for ch in word:# it will store each letter of word one by one in ch variable.
            count_letters += 1
        print("Total letters:", count_letters)

        third = '' # Print 3rd letter
        for k, ch in enumerate(word):
            if k == 2:
                third = ch
        print("Third letter is:", third)

        new_word = ""
        for k, ch in enumerate(word):
            if k == 2:
                new_word += "k"
            else:
                new_word += ch

        l1[i] = new_word
        print("New word:", new_word)


#28/11/25
#l2 = [10, 20, ["banana", 50]]  Change the 2nd letter of "banana" to 'u'.


l2 = [10, 20, ["banana", 50]]
for i, value in enumerate(l2):
    if type(value) == list:                  # find inner list If true then excute next loop
        for j, val in enumerate(value):
            if type(val) == str:             # find string "banana"
                count = 0                 ## count letters in string
                for ch in val:
                    count += 1
                pos = 0                 # find the 2nd letter using loop , variable pos means position initilized with 0
                for ch in val:
                    if pos == 1:             # 2nd letter is position 1
                        #old_letter = ch
                        pos += 1
                        
                new_word = ""           # build new string
                pos = 0
                for ch in val:
                    if pos == 1:
                        new_word += "u"      # replace 2nd letter
                    else:
                        new_word += ch
                    pos += 1
                    value[j] = new_word         # update inside list
print(l2)


##7. Add 3 in each element of 2nd list#
'''l2 = [[3, 4, 5], [6, 7, 8]]
for i in range(len(l2[1])):
    l2[1][i] += 3
print(l2)
Phir se banaye => 
1. without using range 
2. for loop use karna hai
3. Without index hardcoded value.  l2[1] shouldn't be used.'''


l2 = [[3, 4, 5], [6, 7, 8]]
for i ,value in enumerate(l2):
    print('values inside l2',i,value) 
    if i==1:
        print(i)
        for j, val in enumerate(value):
            print('index and value of 2nd list of l2',j,val)
            value[j]=val+3
print(l2)
    


#Ek funtion banana hai to add contact in list. Input will be dictionary and output will be list of dictionary.
'''Storage datatype will be list of dictionary.
Dictionary ka key name and  phone no rakhna hai..'''


contact_list=[] #It will store contacts , each contact should be a dictioary
def add_contact(contact_dictionary): # function with argument contact dictionary, it will store name and phone number 
    new_contact={} #
    #print(add_contact)
    for key in contact_dictionary:  #each key of contact dictionary
        new_contact[key] = contact_dictionary[key]  #
    contact_list.append(new_contact)
    return contact_list
contact =[{"name": "Vijaya", "phone_no": "8507976383"},
        #  {"name": "Saurav", "phone_no": "8787976383"},
         # {"name": "rita", "phone_no": "9907976383"},
          #{"name": "jaya", "phone_no": "9999976383"},
          #{"name": "sita", "phone_no": "8888876383"}
          ]
result = add_contact(contact)
print(result) 

##make a function to addd students details ,details should be a dictionary.
#one student
student_details = []

def add_student(student_dictionary):
    new_student = {}

    for key in student_dictionary:      # Copy each key-value properly
        new_student[key] = student_dictionary[key]
    
    student_details.append(new_student)  # Append after copying
    return student_details

student = {"Name": "Shivam", "Class": 8, "roll": 5, "Address": "Sitamarhi"}  # FIXED (removed list)

result = add_student(student_details)
print(result)


#add multiple students.

student_details = []

def add_student(student_dictionary):
    new_student = {}

    for key in student_dictionary:
        new_student[key] = student_dictionary[key]

    student_details.append(new_student)
    return student_details

#student ={"Name": "Shivam", "Class": 8, "roll": 5, "Address": "Sitamarhi"}

#result = add_student(student)
#print(result)
add_student({"Name": "Shivam", "Class": 8, "roll": 5, "Address": "Sitamarhi"})
add_student({"Name": "Ravi", "Class": 9, "roll": 11, "Address": "Patna"})
add_student({"Name": "Sita", "Class": 7, "roll": 2, "Address": "Delhi"})

print(student_details)

#01/12/2025

'''students = [
    ["Vijaya", 22, ["Python", "SQL", "Excel"]],
    ["Ravi", 23, ["Java", "HTML"]],
    ["Sita", 21, ["C++", "ML", "Python"]]
]
1.Har student ka naam print karo  
2.Har student ke skills count karo
3.Agar kisi student ke 2nd skill ko "AI" karna ho to kaise karoge?'''

students = [
    ["Vijaya", 22, ["Python", "SQL", "Excel"]],
    ["Ravi", 23, ["Java", "HTML"]],
    ["Sita", 21, ["C++", "ML", "Python"]]
]

for student in students:
    print("Name:", student[0])

    skills = student[2]
    print("Skills Count:", len(skills))
    if len(skills) > 1:
        skills[1] = "AI"

print("Updated List:", students)

''' Qsn: 2  Loop ka use karke sabhi students ke total skills count nikaalo. Matlab:Vijaya ke 3 skills,Ravi ke 2,Sita ke 3
Total = 8 skills,Tumhe loop se ye count nikalna hai.'''
students = [
    ["Vijaya", 22, ["Python", "SQL", "Excel"]],
    ["Ravi", 23, ["Java", "HTML"]],
    ["Sita", 21, ["C++", "ML", "Python"]]
]
for stud in students:
    #print(stud[2])
    print(len(stud[2]))
    print('Name : ',stud[0],len(stud[2]), 'skill :',stud[2])

'''Qsn.3:  Python ko "PYTHON-ADV" se replace karna hai ,  Sirf loop ka use karke.'''

students = [
    ["Vijaya", 22, ["Python", "SQL", "Excel"]],
    ["Ravi", 23, ["Java", "HTML"]],
    ["Sita", 21, ["C++", "ML", "Python"]]
]

for stud in students:
    skills = stud[2]
    for i in range(len(skills)):
        if skills[i].lower() == "python":   
            skills[i] = "PYTHON_ADV"

print(students)

#Date:08/12/2025
#Question1:-
'''Create a function to store grocery info. input is dict and output is list of dictionary.
Material:
Unit:
Price:'''

grocery_list=[]
def grocery_info(Material:str,Unit:int,Price:float) -> list:
    dict1={}
    dict1["Material"] = Material
    dict1["Unit"]=Unit
    dict1["Price"]=Price
    grocery_list.append(dict1)
    return dict1
    print(dict1)
grocery_info("biscuit",2,50)
grocery_info("chocolate",1,40)
grocery_info("paneer",5,280)
print(grocery_list)


#Question 2:-
'''Create a function to score a cricket player. 
Logic - 
on hitting six - no of six * 2
On hitting four - no of fours * 1
On being out -  -3
Input me match me Bande ne Kitna 4 maara, Kitna 6 maara and out hua ki nahi wo ayega.
Output me score dena hai..'''

def cricket_score(fours:int, sixes:int, out_status:bool) -> int:
    score = (fours * 1) + (sixes * 2)
    if out_status:
        score -= 3
    return score
player1_score = cricket_score(4, 3, True)
print("Player 1 Score:", player1_score)
player2_score = cricket_score(5, 2, False)
print("Player 2 Score:", player2_score)

#Date: 10/12/2025
'''✅ Question 1:Create a function to store student information.
Input: a dictionary containing "name", "age", "marks".
Output: append it into a list of students and return the list.'''

student=[]
def stud_info(dictionary:dict) -> list:
    student.append(dictionary)
    return student
    print(dictionary)
stud_info({"name":"Vijaya","age":22,"marks":85})
stud_info({"name":"Ravi","age":23,"marks":90})
print(student)

'''✅ Question 2
Create a function that accepts a list of student dictionaries and returns the student
with highest marks.:'''

def highest_marks(students:list) -> dict:
    top = students[0]     

    for s in students:    
        if s["marks"] > top["marks"]:
            top = s       
    return top            
students_list = [
    {"name": "Vijaya", "marks": 85},
    {"name": "Ravi",   "marks": 90},
    {"name": "Sita",   "marks": 78}
]
top_student = highest_marks(students_list)
print("Top Student:", top_student)


'''✅ Question 3 Create a function that takes a dictionary: {"name": "Vijaya", "math": 80, 
"science": 75, "english": 90},Calculate total = sum of marks,
Add it inside the dictionary as "total",Return the updated dictionary.'''

'''def calc_marks(name,maths,science,english) -> dict:
    dict={}
    dict[name]='vijaya'
    dict['math']=90
    dict['science']=75
    dict['english']=80
    total=maths+science+english
    dict[total]=total
    print('Total marks:',total)
    return dict
result=calc_marks('vijaya',90,75,80)
print(result)'''

def calc_marks(student: dict) -> dict:
    total = student["math"] + student["science"] + student["english"]
    student["total"] = total
    return student
data = {"name": "Vijaya", "math": 80, "science": 75, "english": 90}
data1={"name": "Ravi", "math": 85, "science": 80, "english": 88}
data2={"name":"Sita","math":78,"science":82,"english":79}

print(calc_marks(data))
print(calc_marks(data1))
print(calc_marks(data2))


'''✅ Question 4
Create a function that stores attendance details of students.
Input dictionary contains "name" and "days_present".
Add it to a list and return the full attendance list.'''

attendance_list=[]
def attendace_details(atten_dict:dict)->list:
    attendance_list.append(atten_dict)
    return attendance_list
    


'''✅ Question 5
Create a function that accepts a list of student dictionaries and returns:
number of students,average marks,list of all names Output should be a dictionary like:
{
  "count": 5,
  "avg_marks": 78.5,
  "names": ["Vijaya", "Ravi", "Sita", ...]
}'''



#date:- 15/12/2025
'''1.Given a list of numbers,[10, 15, 20, 25, 30, 35] 
use a for loop to count how many numbers are even and how many are odd.'''

numbers=[10, 15, 20, 25, 30, 35,3, 99]
even=[]
odd=[]
for val in numbers:
    if val%2==0:
        #print("even number",val)
        even.append(val)
        #print(even)
        #print(len(even),'Even numbers are there.')
    else:
        #print('odd numbers',val)
        odd.append(val)
        #print(odd)
        #print(len(odd),'Odd numbers are there')
print('Even in numbers list',even)
print(len(even))
print('odd in numbers list',odd)
print(len(odd))
    
'''2.Using a for loop, find the largest number in a list without using max().
[45, 12, 78, 34, 89, 23]'''

num=[45, 12, 78, 34, 89, 23]
larg=num[0]
for val in num:
    #print(val)
    if val>larg:
        #print(larg)
        larg=val
print('Largest number :',larg)


'''3. Using a for loop, create a new list that contains 
the square of each number from the given list. [2, 3, 4, 5]'''

number_list=[2,3,4,5]
square_list=[]
for i in number_list:
    square_list.append(i**2)
print("square of each number inside list is",square_list)


#4.Using a for loop, count how many vowels are present in a given string.'''
city='Manikarnika'
count_vowel=0
for i in city:
    if i in 'aeiouAEIOU':
        count_vowel += 1
print('Vowels count:', count_vowel)


#5.Using a for loop, print the multiplication table of a given number up to 10.'''

num=7
for i in range(1,11):
    print(num,'*',i,'=',i*num)


#Date:- 16/12/2025
#1.Given a list of numbers, use a for loop to count how many numbers are:Positive,Negative,Zero
#[10, -5, 0, 7, -2, 0, 8]

numbers=[10,-5,0,7,-2,0,8]
positive=0
negative=0
zero=0
for i in numbers:
    if i>0:
        positive=positive+1
        print(positive)
    elif i<0:
        negative=negative+1
        print(negative)
    else:
        zero=zero+1
        print(zero)
print('positive numbers=',positive)
print('Negative numbers=',negative)
print('Zero',zero)

#2.Reverse a given list using a for loop (do not use reverse() or slicing).[1,2,3,4]
number=[1,2,3,4]
reverse_list=[]
for i in range(len(number)-1,-1,-1):
    reverse_list.append(number[i])
print(reverse_list)

#3.Given a number, use a for loop to find the sum of its digits. number = 123
number=1,2,3,7
sum=0
for i in number:    #To repeat the same action (adding) for every value.
    sum=sum+i
print(sum)

#**4.Using a for loop, find and print the duplicate elements in a list. [1, 2, 3, 2, 4, 5, 1]
number=[1, 2, 3, 2, 4, 5, 1]
duplicate=[]
for i in number:
    number[i]==number
    number[i].append(duplicate)
print(duplicate)

    
#5.Using a for loop, count how many times each element appears in a list.['a', 'b', 'a', 'c', 'b', 'a']
'''a : 3 , b : 2, c : 1'''

elements = ['a', 'b', 'a', 'c', 'b', 'a'] #Creates a list of letters
counted = [] #it is a blank list , it will contain only repeated values.
for i in elements: #loop will check elements one by one
    if i not in counted: #Checks if the current element i is already counted
        print(f"{i} : {elements.count(i)}") # elements.count(i) → counts how many times i appears,
        counted.append(i) #Adds the current element i to the counted list


#Date:-17/12/2025
#1️.Write a program to check whether a given number is prime or not using a for loop.

num = int(input("enter number"))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1

if count == 2:
    print("Number is Prime")
else:
    print("Number is Not Prime")

#2.Factorial of a Number Write a program to find the factorial of a number entered by the user using a for loop.
#Example: 5 → 120
num=4
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

#3️.Reverse a Number Write a program to reverse a number using a for loop. 1234 → 4321

num=1234
temp = num       # Save original number
reversed_num = 0
num_digits = len(str(num))          # Count number of digits first
for i in range(num_digits):
    last_digit = temp % 10            # Step 1: Get last digit
    reversed_num = reversed_num * 10 + last_digit  # Step 2: Build reversed number
    temp = temp // 10                  # Step 3: Remove last digit
print("Reversed number is:", reversed_num)

#4.Pattern Printing Write a program to print the following pattern using a for loop:
''' *                   
    * *
    * * *
    * * * *
    * * * * *'''

st='*'
for i in range(1,6):
    print(i*st)

#5.Write a program to count how many digits are present in a number using a for loop.
#METHOD 1.

num=12345
num_count=len(str(num))
print(num_count)

#METHOD 2.

num=12345
count=0
for i in range(len(str(num))):
    count=count+1
print('total digits count : ',count)

#METHOD 3.
num=1234
count=0
for i in str(num):
    count= count+1
print(count)

#METHOD 4.
count = len(str(num))
print("Number of digits:", count)

 #6.Add 10 to each element in a list.
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] + 10
print(numbers)

#Date:- 18/12/2025
#1. name='vijaya' ----find duplicate character, at what index, and what is the count of that pparticular letter.


name = "vijaya"
for i in name:
    if name.count(i) > 1:
        print("Duplicate character:", i)
        print("Count:", name.count(i))
        
        print("Indexes:", end=" ")
        for j in range(len(name)):
            if name[j] == i:
                print(j, end=" ")
        break


name = "vijaya"
count = 0
indexes = []
for i in range(len(name)):
    if name[i] == 'a':   # checking manually for duplicate
        count = count + 1
        indexes.append(i)
if count > 1:
    print("Duplicate character: a")
    print("Count:", count)
    print("Indexes:", indexes)


#date :- 21/12/2025
#1. Armstrong Number Write a program to check whether a number is an Armstrong number using a for loop.
# Example: 153 → 1³ + 5³ + 3³ = 153
# solved by chatgpt
#number=153
num = int(input("Enter number: "))
temp = num            # keep original number safe
digits = 0
# Step 1: count digits
t = num
while t > 0:
    digits += 1
    t //= 10

# Step 2: calculate Armstrong sum
sum_val = 0
t = num
while t > 0:
    digit = t % 10
    sum_val += digit ** digits
    t //= 10

# Step 3: compare
if sum_val == temp:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


    
#2.Perfect Number:-Write a program to check whether a number is a perfect number using a for loop.
#Example: 6 → 1 + 2 + 3 =6

num=int(input("Enter number : "))
sum=0
for i in range(1,num):
    if num % i==0:
        sum=sum+i
if sum==num:
    print('number is perfect')
else:
    print('number is not perfect')    

#3.Second Largest Number:-Given a list of numbers, find the second largest number using a for loop (without using sort()).

num = [100, 40, 12, 200]
largest = num[0]
second_largest = num[0]
for i in range(len(num)):
    if num[i] > largest:
        second_largest = largest
        largest = num[i]
    elif num[i] > second_largest and num[i] != largest:
        second_largest = num[i]
print("2nd largest number is:", second_largest)

#4.Prime Numbers in a Range: Write a program to print all prime numbers between 1 and N using nested for loops.

n=int(input("Enter range"))
for num in range(2,n+1):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print(num)


#5.Frequency of Digits: Write a program to count the frequency of each digit in a given number using a for loop.
#Example: 112233 → {1:2, 2:2, 3:2}

num = input("Enter a number: ")

check = ""

for digit in num:
    if digit not in check:
        count = 0
        for d in num:
            if d == digit:
                count = count + 1
        print(digit, ":", count)
        check = check + digit




#6.Largest Number:-Given a list of numbers, find the largest number using a for loop (without using sort()).

num=[1,2,3,4]
larg=num[0]
for i in range(len(num)):
    if num[i]>larg:
        larg=num[i]
print('largest number is ',larg)

#Date:- 22/12/2025
#interview related questions from list.
#1. Program to find sum of elements in a list.
a=[1,2,3,4]
sum=0
for i in a:
    sum=sum+i
print('Sum of elements of list a :',sum)

#2. Program to find maximum and minimum element without using max()/min().
a=[5,10,1,20]
minimum=a[0]
maximum=a[0]
for i in range(len(a)):
   if a[i]>maximum:
       maximum=a[i]
   elif a[i]<minimum:
       minimum=a[i]
print(minimum)
print(maximum)
    

#3. Program to count total elements in a list.
a=[10,20,30]
count=0
for i in a:
    count=count+1
print(count)


#4. Program to reverse a list without using reverse() or slicing.

a=[10,4,12,20]
for i in range(len(a)-1,-1,-1):
    print(a[i])


"""2nd method
a=[10,4,12,20] 
rev=[] 
for i in range(len(a)-1,-1,-1): 
    rev=a[i] 
    print(rev)
"""

#5. Program to check whether a list is empty.

a=[]
count=0
for i in a:
    count=count+1
if count==0:
    print('List is empty')
else:
    print('List is not empty')
    
#2nd method
a=[]
if not a:
    print("list is empty")
else:
    print("list is not empty")

#3rd method
a=[]
if len(a)==0:
    print('list is empty')
else:
    print('list is not empty')


#Date:23/12/25

#write a program to find 2nd element of a string.
name='umbrella'
a=1
for i in name:
    if a%3==0:
        print(i)
    a+=1

#2nd method
name = "vijaya"
for i in range(len(name)):
    if (i + 1) % 2 == 0:   
        print(name[i])

#3rd method

name = "vijaya singh"
count = 0
for i in name:
    count = count + 1
    if count % 2 == 0:
        print(i)

#6. Program to search an element in a list without using 'in'.
a=[12,11,13]
for i in a:
    if i==18:
        print(i,'available in list')
        break
    else:
        print(i,'not available in list')

#2nd method
a = [12, 11, 13]
count = 0
for i in a:
    if i == 12:
        print(i, 'available in list')
        count += 1
        break
if count == 0:
    print('not available in list')

#third method
a = [12, 11, 13]
found = False
for i in a:
    if i == 18:
        found = True
        break
if found:
    print("Element found")
else:
    print("Element not found")



#7. Program to print list elements using index.
fruits=['mango','orange','apple','grapes']
for i,j in enumerate(fruits):
    print(i,j)

##2nd example:-
num=[9,2,10,20,33,50]
for index,value in enumerate(num):
    print(index,value)

#3rd method
fruits=['mango','orange','apple','grapes']
for i in range(len(fruits)):
    print(i, fruits[i])


#8. Program to copy one list into another manually.
a = [1, 2, 3, 4, 5]
b = []
for i in a:
    b.append(i)
print(b)


#2nd method
a=[1,2,3,4,5]
b=[]
for i in a:
    b=a.copy()
print(b)

#9. Program to find average of list elements.
lst=[1,2,3]
sum=0
avg=0
for i in lst:
    print(i)
    sum=sum+i
print('sum of value inside list is :',sum)
avg=sum/len(lst)
print(avg)


#10. Program to separate even and odd numbers
num=[2,3,4,1,6,5]
for i in num:
    if i%2==0:
        print(i,'Even number')
    else:
        print(i,'Odd Number')

#2nd method:-
even=[]
odd=[]
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

