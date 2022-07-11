#!/usr/bin/env python
# coding: utf-8

# # Exercise 9

# ###  Check if the number is an Armstrong number or not.

# In[41]:


n = int(input("Enter a number : "))
sum = 0
temp = n
while temp>0:
    dig = temp % 10
    sum += dig **3
    temp //= 10
if sum == n:
    print("The given number is an Armstrong number")
else:
    print("The given number is not an Armstrong number")


# # Exercise 11

# ### Write a function called show stars(rows). If rows are 5, it should print the following.

# In[42]:


n=int(input("Enter a number of rows : "))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()


# # Exercise 12

# ### Write a program to remove characters from a string starting from zero up to n and return a new string.

# In[47]:


str_1 = str(input("Enter the string values : "))
print ("The original string : " + str_1)
n = int(input("Enter the position of the string to remove : "))
new_str = str_1[:(n-1)] + str_1[n:]
print ("The string after removing the i'th character : " + new_str)


# # Exercise 13

# ### Iterate the given list of numbers and print only those numbers which are divisible by 5

# In[51]:


x = []
n_1 = int(input("Enter no. of list elements"))
for i in range(n_1):
    x_1 = int(input())
    x.append(x_1)
x_2 = []
def div_5(x):
    print("Given list",x)
    for i in x:
        if i%5 == 0:
            x_2.append(i)
div_5(x)
print("The list is",x_2)


# # Exercise 15

# ### Print the number pattern.

# In[52]:


n=int(input("Enter the number of rows : "))
for i in range(0,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()


# # Exercise 16

# ### Write a program to check if the given number is a palindrome number.

# In[3]:


a=int(input("Enter a number : "))
a1=str(a)
a2=a1[::-1]
if a1==a2:
    print("The given is a Palindrome")
else:
    print("The given number is not a Palindrome")


# # List

# ### Python program to interchange first and last elements in a list

# In[8]:


def swapList(newList):
    size = len(newList)
    temp_1 = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp_1
    return newList
n_4 = int(input("Enter the number of elements :"))
newList = []
for i in range(n_4):
    c = int(input())
    newList.append(c)
print(swapList(newList))


# ### Python program to swap two elements in a list

# In[9]:


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
List = []
n_5 = int(input("Enter the number of array elements :"))
for i in range(n_5):
    n_6 = int(input())
    List.append(n_6)
pos1, pos2 = 1, 3
print(swapPositions(List, pos1-1, pos2-1))


# ### To find length of a list

# In[12]:


List = []
n_5 = int(input("Enter the number of elements :"))
for i in range(n_5):
    n_6 = int(input())
    List.append(n_6)
print("The length of the list given :",len(List))


# ### Maximum of two numbers.

# In[14]:


a=[]
n=int(input("Enter the number of elements : "))
for i in range(1,n+1):
    b=int(input("Enter the element :"))
    a.append(b)
a.sort()
print("First largest element :",a[n-1])
print("Second largest element :",a[n-2])


# ### Minimum of two numbers.

# In[15]:


a=[]
n=int(input("Enter the number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter the element:"))
    a.append(b)
a.sort()
print("First smallest element :",a[n-(n-1)])
print("Second smallest element :",a[n-(n-2)])


# # String Exercises.

# ### Program to check whether the string is Symmetrical or Palindrome

# In[54]:


string = str(input("Enter a word : "))
half = int(len(string) / 2)
if len(string) % 2 == 0:
    first_str = string[:half]
    second_str = string[half:]
else:
    first_str = string[:half]
    second_str = string[half+1:]
if first_str == second_str:
    print(string, 'string is symmertical')
else:
    print(string, 'string is not symmertical')
if first_str == second_str[::-1]:
    print(string, 'string is palindrome')
else:
    print(string, 'string is not palindrome')


# ### Reverse words in a given String in Python

# In[55]:


string = str(input("Enter a sentence to reverse :"))
s = string.split()[::-1]
l = []
for i in s:
    l.append(i)
print(" ".join(l))


# ### Ways to remove i’th character from string in Python

# In[57]:


test_str = str(input("Enter a word : "))
print ("The original string is : " + test_str)
z = str(input("Which character you want to remove ? : "))
new_str = test_str.replace(z, '', 1)
print ("The word after removal of i'th character(works) : " + new_str)


# # Tuples 

# ### Python program to Find the size of a Tuple

# In[58]:


tup1= ("karthi","parvathi", 5, 11)
tup2= ("Learn", "Python")
tup3= ((25,"Program"), (34, "Python"), (123, "Coding"))
print("Size of tuple1 : ", tup1.__sizeof__(), "bytes")
print("Size of tuple2 : ", tup2.__sizeof__(), "bytes")
print("Size of tuple3 : ", tup3.__sizeof__(), "bytes")


# ### Python – Maximum and Minimum K elements in Tuple

# In[21]:


my_tuple = (17, 255, 396, 90, 60, 88)
print("The tuple is : ")
print(my_tuple)
K = 2
print("The value of K has been initialized to ")
print(K)
my_result = []
my_tuple = list(my_tuple)
temp = sorted(my_tuple)
for idx, val in enumerate(temp):
    if idx < K or idx >= len(temp) - K:
        my_result.append(val)
my_result = tuple(my_result)
print("The result is : " )
print(my_result)


# # Dictionary Exercises

# ### Dictionary with keys having multiple inputs.

# In[36]:


def books(car_name,year):
    print("CAR DETAILS : " , car_name + ' , ' + year)
books("Toyota Innova" , "2004")
books("Renault Duster" , "2010")
books("Maruti-Suzuki" , "2000")


# # Function Exercises

# ### Get list of parameters name from a function in Python.

# In[38]:


def fun(x, y, z):
    return a**b**c
import inspect
print(inspect.signature(fun))


# # Matrix Exercises

# ### Assigning Subsequent Rows to Matrix first row elements.

# In[39]:


my_list=[[5,10,15],[3,6,9],[4,8,12],[7,14,21]]
print("my list :"+str(my_list))
result={my_list[0][val] : my_list[val+1] for val in range(len(my_list)-1)}
print("The matrix : " +str(result))


# ### Adding and Subtracting matrices.

# In[ ]:


import numpy as np
A = np.array([[10,5],[9,9]])
B = np.array([[4,4],[5,6]])
print("elments in A")
print(A)
print("elments in B")
print(B)
print("addition of two matrix")
print(np.add(A,B))
print("subtraction of two matrics")
print(np.subtract(A,B))

