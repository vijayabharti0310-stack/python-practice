#String methods:-
#1.replace:- change one value to another
#syntax:-string.replace(old,new)  old-what you want to change, new-what you want to put in place of old
text="I like JAVA"
text.replace('JAVA','PYTHON')

#replace multiple items (repeating letters).
text='aeroplane'
text.replace('a','A')



# 2. del:-means delete /remove -deleting variables,list items,dict items,slices.
greeting='Good Morning'
print(greeting)
del greeting

greeting #after del if you want to run then it will give NameError: name 'greeting' is not defined



# 3.string concatination:- join two strings using '+' operator.
#eg:-1
str1='Vijaya '
str2='Bharti'
print(str1+str2)  #output-Vijaya Bharti

#eg:-2
name='Ravi'
marks=85
print(f"Name is {name} and marks {marks}")

#eg:-3
my_list=[1,2,3,4,5]
my_list[3]=6 #in this method you can update the value of that particualr number which is inside rectangular brackets.
print(my_list) #output will be [1, 2, 3, 6, 5]

#eg:-4
my_list+[7] #concatinate list with list ,here i value addded in my_list after 5.



#4. partition:-It is a string method used to split a string into 3 parts.(It splits the string only once.)

greeting='hello everyone I am Vijaya'
greeting.partition('I') #output:-('hello everyone ', 'I', ' am Vijaya')

#eg2:
greet="Hello everyone I am Vijaya Singh ,how can I help you."
greet.partition('Vijaya Singh')
#output:-('Hello everyone I am ', 'Vijaya Singh', ' ,how can I help you.')



#5.strip():- It is used to remove extra spaces from astring.It removes from start,end,but not from middle.
str="  vijaya  "
str.strip() #output: "vijaya" - here strip() remove extra spaces from both sides.

#eg2.
id="   @@@###12345  @@###"
id.strip() #output:-'@@@###12345  @@###'  :-here strip remove both sides step but not from middle.

#eg3.
id="@@@###12345@@###"
id.strip('@#') #remove both sides matching value :-'12345'

#eg4.
id="@@@###??/@#@#??&"
id.strip('@#') #output- '??/@#@#??&'


#6.count()- used to show how many times a particular character is epeated in a word.
#eg:
name='vijaya'
name.count('a') #output:- 2


#7. .upper():- used for capital letters.
name.upper()



#8. .lower():-used for small letters.
name.lower()


#9.split()-> It seperate by each word.
#note: we cannot convert string into integer directly but using '' and "" any numberis inside these wuotes then it will give an output.
greeting='hello everyone I am Vijaya'
greeting.split()#output- ['hello', 'everyone', 'I', 'am', 'Vijaya']

#eg.2:- split using , comma.
intro="I come from Sitamarhi, birth place of Sita"
intro.split(',') #it will split sentence where comma is given.
#output:-['I come from Sitamarhi', ' birth place of Sita']


#10.startswith();-checks whether  astring starts with a given value.(it returns True or False)
name='vijaya'
name.startswith('v')  #True
name.startswith('a')  #False


#11.endswith() :- checks whether a string ends with a given value.Returns True and False.
name.endswith('a')  #True
name.endswith('v')  #False


#12.format():- It is used to insert values into a string.It makes strings clean and readable.
# eg1.
x=10
y=20
z=25
#"cost of three pens {},{},{}".format(x,y,z)
print("cost of three pens {},{},{}".format(x,y,z))

#eg2. using f''
name='vijaya'
age=22
print(f"my name is {name}, I am {age} years old.")



#13.typecasting:- means changing one data type into another.
a=1
b='abc'
print(a)

float(a)#1.0
bool(a) #True
int(a)#1
str(a) #TypeError: 'str' object is not callable


#14.indexing:- means accessing one element from a sequence using its position number.Python uses 0-based indexing.
#indexing works ---string, list, tuple.
text="PYTHON"
text[0]     #P
text[1]     #Y
text[4]     #O
text[5]     #N
text[6]     #IndexError: string index out of range
text[-1]    #N
text[-4:-1] #THO
