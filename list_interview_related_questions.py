#SECTION 2: BASIC PROGRAMMING QUESTIONS - interview based.

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


#Date:- 27/12/2025
#SECTION 3: INTERMEDIATE LOGIC QUESTIONS
#11. Program to remove duplicate elements without using set.

nums=[1, 2, 3, 2, 4, 1, 5]
dup=[]
for i in range(len(nums)):
    #print(i)
    found=False
    for j in range(len(dup)):
        if nums[i]==dup[j]:
            found=True
            break
    if found==False:
        dup.append(nums[i])
print(dup)

#or 

nums = [1, 2, 3, 2, 4, 1, 5]
unique = []
for i in nums:
    if i not in unique:
        unique.append(i)
print(unique)


#remove repeated name
fruits=['apple','mango','orange','apple','banana','mango']
dup_fruits=[]
for i in range(len(fruits)):
    found=False
    for j in range(len(dup_fruits)):
        if fruits[i]==dup_fruits[j]:
            found=True
    if found==False:
        dup_fruits.append(fruits[i])
print(dup_fruits)

#12. Program to find duplicate elements in a list.

my_list = [1, 1, 2, 3, 4, 3, 5, 6, 5]
duplicate_items = []
for i in range(len(my_list)):
    count = 0
    for j in range(len(my_list)):
        if my_list[i] == my_list[j]:
            count += 1
    if count > 1:
        if my_list[i] not in duplicate_items:
            duplicate_items.append(my_list[i])
print(duplicate_items)  #output:-[1, 3, 5]

#13. Program to count frequency of each element.
nums = [1, 2, 3, 2, 4, 1, 5,8,9,8,8,9,1,1,1]
#frequency=[]
for i in range(len(nums)):
    count=0
    for j in range(len(nums)):
        if nums[i]==nums[j]:
            count=count+1
    
    already_printed = False
    for k in range(i):
        if nums[i] == nums[k]:
            already_printed = True
            break
    if already_printed == False:
        print(nums[i], ":", count)
#output:-
'''1 : 5,
2 : 2
3 : 1
4 : 1
5 : 1
8 : 3
9 : 2'''

#14. Program to find largest element without sorting.
num=[1,2,4,5,3]
large=num[0]
for i in range(len(num)):
    #print(i)
    if num[i]>large:
        large=num[i]
print(large)    #output:- 5


#15. Program to merge two lists alternately.
list1=[1,2,3,4]
list2=[5,6,7,8,9,10]
merge=[]
for i in range(len(list1)):
    merge.append(list1[i])
    if i < len(list2):
        merge.append(list2[i])
for i in range(len(list1),len(list2)):
    merge.append(list2[i])
print(merge)  #output:-[1, 5, 2, 6, 3, 7, 4, 8, 9, 10]

#Date:-28/12/2025
#16. Program to find common elements between two lists.

a=[1,2,3,5,6,8,10]
b=[6,5,3,4,1,7,10,12,60]
common=[]
for i in range(len(a)):
    #print(i)
    for j in range(len(b)):
        #print(j)
        if a[i]==b[j]:
            common.append(a[i])
print(common)

#17. Program to find missing number from a list.

my_list=[1,2,4,6,9,10]
missing=[]
my_list.sort()
for i in range(len(my_list)):
    current=my_list[i]
    next=my_list[i+1]
    if (next-current>1):
        for num in range(current+1,next):
            missing.append(num)
print(missing)
    
#18. Program to rotate list elements to the left.

my_list=[1,2,3,4,5,6]
rotate_left=my_list[0]
for i in range(len(my_list)-1):
    my_list[i] = my_list[i + 1]
my_list[len(my_list) - 1] =rotate_left
print(my_list)

#19. Program to rotate list elements to the right.
my_list=[1,2,3,4,5,6]
rotate_right=my_list[-1]
for i in range(len(my_list)-1,0,-1):
    my_list[i]=my_list[i-1]
my_list[0]=rotate_right
print(my_list)

#20. Program to split a list into two halves

a=[1,2,4,3,6,8]
middle=len(a)//2
first_half=[]
second_half=[]
for i in range(middle):
    first_half.append(a[i])
for i in range(middle,len(a)):
    second_half.append(a[i])
print("First half = ",first_half)
print("Second half = ",second_half)

#21.Program to split a list into two halves and count how many elements are there in each half.

a=[1,4,3,2,6,7,8,9,10,11,21]
middle=len(a)//2
first_half=[]
second_half=[]
for i in range(middle):
    first_half.append(a[i])
for i in range(middle,len(a)):
    second_half.append(a[i])
print('First half = ',first_half)
print(len(first_half))

print('Second half = ',second_half)
print(len(second_half))

#21. Program to find second largest element without sorting.
num = [1, 2, 4, 5, 3]
largest = num[0]
second_largest = num[0]
for i in num:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print("2nd largest:", second_largest)


#Date:- 29/12/2025

#22. Program to check whether a list is palindrome without slicing.
#23. Program to flatten a nested list.

nested_list = [1, [2, 3], [4, 5, 6], 7]
flat_list = []
for element in nested_list:
    if type(element) == list:   # check if it is a list
        for item in element:    # loop through inner list
            flat_list.append(item)#append items in flat_list
    else:
        flat_list.append(element)  # if not a list, append directly
print(flat_list)

#24. Program to sort a list without using sort() or sorted().

my_list=[6,1,5,2,4,3]
s_ort=[]
my_list.sort
s_ort=my_list
print(s_ort)

#Date:-29/12/2025
#25. Program to move all zeros to the end of the list.

my_list=[1,2,0,3,4,0,5]
no_zero=[]
for i in range(len(my_list)):
    if my_list[i]>0:
        no_zero.append(my_list[i])
print(no_zero)
for i in range(len(my_list) - len(no_zero)):
    no_zero.append(0)
print(no_zero)

#26. Program to find intersection of two lists without using set.
l1=[2,1,3,4,6]
l2=[4,5,1,6,7]
l3=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            l3.append(l1[i])
print(l3)

#27***. Program to remove all occurrences of a given element.
num = [1, 2, 1, 3, 4, 5, 4, 7, 6, 7]
element_to_remove = 1 # element you want to remove
new_list = []
for i in range(len(num)):
    if num[i] != element_to_remove:
        new_list.append(num[i])
print(new_list)

#28. Program to find pair of elements with given sum.
num=[1,2,3,4,5]
target_sum=7
for i in range(len(num)):
    for j in range(i+1, len(num)):  # check elements after i
        if num[i] + num[j] == target_sum:
            print((num[i], num[j]))

#Date:- 03/01/2026     
#29. Program to replace negative numbers into other list.
num=[9,8,-1,7,-3,0]
negative=[]
for i in range(len(num)):
    if num[i]<0:
        negative.append(num[i])
print(negative)



#30. Program to replace negative numbers with zero.

num = [9, 8, -1, 7, -3, 0]
for i in range(len(num)):
    if num[i] < 0:
        num[i] = 0
print(num)


#31. Program to find longest consecutive sequence in a list.

nums = [100, 4, 200, 1, 3, 2]
nums.sort()
longest = 1
current = 1
for i in range(1, len(nums)):
    if nums[i] == nums[i-1] + 1:
        current += 1
    else:
        current = 1
    if current > longest:
        longest = current
print(longest)

#32. Program to split list based on a condition.even-odd.

num=[1,2,3,5,6,8,7,9]
even=[]
odd=[]
for i in range(len(num)):
    if num[i]%2==0:
        even.append(num[i])
    else:
        odd.append(num[i])
print('Even numbers : ',even)
print('Odd numbers : ',odd)