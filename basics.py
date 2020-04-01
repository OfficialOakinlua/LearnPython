#Name: Akinlua, Olorunfemi Praise
#Date Created: April 01, 2020
#About: Learn Python (Basics)
#Version; 1.0
#Python Version: 3.6

#---------------------
###variables###

print("David is a great fighter")
 #if I would love to write the above
 #statement over and over again within my python program
 #I would use a variable, a variable is simply a box that contains certain things
 #this things could be strings, numbers, boolean and objects

 #Now let's put line 3 string in a variable named Sentence

Sentence = "David is a great fighter"
print(Sentence)

#line 10 and Line 16 would output the same things

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

###Inputing Data
#Before we go on, I would love to introduce something that I believe would be great
#to know now at the begining
#You can accept data (strings, number) from the user of your program via a simple
#function called input(). A simple illustration is below

age_input = input("Enter your Age:")
print(age_input)
#the result of line 46 and 47 would be depending on what the program user inputs
#for example, if Linda uses the program and she types 17, her output would be 17
#Now if Jacob writes 23, the program would output 23
#As you can see, we are slwoing building a dynamic program bit by bit
