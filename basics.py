"""Name: Akinlua, Olorunfemi Praise
Date Created: April 01, 2020
About: Learn Python (Basics); Based of the Udemy Python Mega Course
Version; 1.0
Python Version: 3.6
"""
#---------------------
###variables###

print("David is a great fighter")
 #if I would love to write the above
 #statement over and over again within my python program
 #I would use a variable, a variable is simply a box that contains certain things
 #this things could be strings, numbers, boolean and objects

 #Now let's put line 10 string in a variable named Sentence

Sentence = "David is a great fighter"
print(Sentence)

#line 10 and Line 19 would output the same things

#----------------------
###numbers###

a = 2
b = 5
print(a + b)
#output of the above code is 7
#Numbers are not new concept to us. Though, in programming, there are different
#types of number namely float and integer, a nd b are integers and 4.5 or 6.0 are
#floats (decimals)

a = 2
b = 5.0
print(a + b)
#the resulting output would be a float rather than an integer because a float
#was involved in the addition operation


#--------------------------
###Inputing Data
#Before we go on, I would love to introduce something that I believe would be great
#to know now at the begining
#You can accept data (strings, number) from the user of your program via a simple
#function called input(). A simple illustration is below

age_input = input("Enter your Age:")
print(age_input)
#the result of line 48 and 49 would be depending on what the program user inputs
#for example, if Linda uses the program and she types 17, her output would be 17
#Now if Jacob writes 23, the program would output 23
#As you can see, we are slowing building a dynamic program bit by bit

#--------------------------
#Number Operations
#Just like in mathematics, python can carry out all operations such as addition
#substraction, multiplication and division

num_operation = ((2  * 3) / (2 + 1)) ** 2
print(num_operation)
#the output of the code is 4.0 because python follows the normal BODMAS rule
#Brackets are dealt with first by the compiler then Order (Exponentiation), division
#multiplication, addition, substraction
#division and multiplication are of the same operation level
#same goes to addition and substraction
#one might ask why is the the result is a float. The reason is simply because of the
#division used during the whole process. the result of any division operation would always give
#a float whether all entities involved are integers or floats or both

#-----------------------
#String Operations

firstname = "Olorunfemi"
lastname = "Akinlua"

name = lastname + ", " + firstname
print(name)
#The result of the above code is Akinlua, Olorunfemi
#What occured is an operation called String concatenation
#it involves adding two or more strings together to make a single string
#The above code involves three strings "Olorunfemi", ", " and "Akinlua"
#obviously, string concatenation can only occur between strings. Strings and integers wouldnt work
#Though, a way to add a number to a string is taking the print() functions as a multiple parameters
#We would learn about functions later

print(name + " is ", 19 )

#You can replace a particular character in a string using the replace function. An example code is below
firstname1 = firstname.replace("o", "a")
print(firstname1)
#the output is Olarunfemi. You would be suprised as to why the first letter didn't change to a.
#The reason is simpley because to the python compiler, O is different from o.

#For the same replace() function, you can control the number of letters it changes by another parameter (signifying
#the number of times). Example Code is below
c = "volunteer"
c = c.replace("e", "i", 1) #this will replace e with i once
print(c)
# resulting output is voluntier

#strings in Python are arrays of bytes representing unicode characters.
#String Indexing
word = "Hello World"
word1 = word[2]
print(word1)
#The output of the code is l (the first l)
#python numbers the character from 0 and not 1
#therefore h - 0, e - 1, l - 2, l - 3, o - 4, space - 5, W - 6, o - 7, r - 7, l - 8, d - 9
# a simple maths n =  actual position; p = python position (p = n - 1)
# say word1 = word[2] therefore p = 2 and n = 3 using the normal 1,2,3 l would be the answer

#Another String Indexing Format
#using negative Numbers
word2 = word[-1]
print(word2)
#the resulting output is d (the last character)
word3 = word[-2]
print(word3)
#the resulting output is l (the second to the last character)
#and so on

#Another String Indexing Format
word4 = word[2:5]
print(word4)
#the output of the Code is "llo"
#word2 = word[m:n] the code would output m allthrough to n-1

#length of a string
length_of_lastname = len(lastname)
print(length_of_lastname)
#outputs the number of character in the string stored in lastname including spaces which is 7

#Strip Function
wide_hello = " Hello World! " #strip() is used to remove whitespaces before and after the string
print(wide_hello) #resulting output is "Hello World!" instead of " Hello World! "
#obviously the quotation marks wouldn't be there but i want to put emphasis on the whitespaces


#---------------------------
#Lists
sample_list = ["wow", 1, True, "ILoveYou", 4.56]
#a list can be described as an ordered shopping list that can contain just anything
#a list in python can contain integers, floats, strings, boolean (True or False) (we will talk about this later)
print(sample_list) #output would be ["wow", 1, True, "ILoveYou", 4.56]

#List Operations
#List Indexing
#It's quite similar to string indexing, only this time it's not characters we are Indexing
#but strings, integers, float, boolean
#I will be using the sample_list for different ways to carry out list indexing

sample_list[1]#output is the integer 1
sample_list[2]#output is the boolean True
sample_list[1:3]#output is a list [1, True]
sample_list[-1]#output is the float 4.56
sample_list[-3:-1] # output is a list [True, 'ILoveYou']
sample_list[-1:-3] #outputs [] because -3 is less than -1 and the lesser value is usually first


#Remove () function
sample_list.remove("wow")# would remove the string "wow" from the list making 1 the Oth content of the List
#Append () function
sample_list.append("new")# would add the string "new" to the list making the last content of the List


#---------------------------
#Tuples
sample_tuple = ("wow", 1, "Fame")
#a tuple is similar to a list but the major difference between the two is that Tuple is immuatable
#immutable in the sense that it can't be changed (simply put contains immutable Python objects)
#whatever is the base content remains the content forever

#tuple Indexing
sample_tuple[0] #outputs "wow"

#---------------------------
#Dictionary
#Dictionary is an unordered collection of data values, used to store data values like a map (Data Structures),
#which unlike other Data Types that hold only single value as an element
#Thanks to GeeksforGeeks
#example
author = {"firstname": "Olorunfemi", "lastname": "Akinlua", "School": "OAU", "Book": "LearnPython", "ISBN":"None"}
#basically a dictionary can contain as many key:value pairs ("firstname" - key, "Olorunfemi" - value) as possible
#so instead of using indexing using numbers (0, 1, 2, 3), you can use the key to access the values like a key can access only a particular
#door

#therefore, if we want to access the value "OAU" which is the name of my school (Obafemi Awolowo University) we simply write the code below
author["School"] #in a python interpreter or console, it would output "OAU"

#one thing that is important about dictionary is the feature of its unorderlines
#check 03.png in the img folder and you would notice that the result of printing author (the dictionary)
#gives a the 'lastname' first and so on rather than  the 'firstname' first which was the way we inputed it into our
#python code. it is because of the fact that all of the objects are in an unordered collection

#to verify that the normal indexing doesn't work with dictionaries, try the code below
#author[0] #it would give you an error message KeyError meaning wrong key use to access a value

#lets update the dictionary to have different kind of objects

author = {"firstname": "Olorunfemi", "lastname": "Akinlua", "School": "OAU", "Book": "LearnPython", "ISBN":"None", "Age" : 19, "Hobbies": ("Football", "Watching Series", "Gaming"), "friends": ["Jacob", "Seun", "Timi", "Simi", "Laolu"]}

#now let's access the age value
print(author["Age"]) #outputs 19
print(author["friends"]) #outputs the list ["Jacob", "Seun", "Timi", "Simi", "Laolu"]
#if i would love to print out seun's name who is one of my friends, it would go like this
print(author["friends"][1]) #outputs string "Seun"
print(author["Hobbies"]) #outputs the tuple ("Football", "Watching Series", "Gaming")


#this is the end of the basic.py file
#we move to errors.py
