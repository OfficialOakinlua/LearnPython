#Name: Akinlua, Olorunfemi Praise
#Date Created: April 03, 2020
#About: Learn Python (Errors); Based of the Udemy Python Mega Course
#Version: 1.0
#Python Version: 3.6
#DISCLAIMER: this particular py file contains a lot of errors

#errors
#There are different types of errors that one could fall under in Python during the
#course of coding. It is important and paramount to understanding the process of python coding

#-----------------------------
#Syntax errors
#these are errors due to wrong python syntax used in executing a code
print 3 #would give a syntax error becaue of missing paranthesis
#check 04.png, 05.png or try it yourself
#the red arrow I drew points to this ^ icon
# ^ shows you where the error is. In this case, the error is around 3 (no paranthesis)
# let's try another wrong syntax
print 345 # ^ is shown at the end of 345 indicating missing paranthesis


#------------------------------
#Logical errors
#these are errors cause the program to behave incorrectly, but they do not usually crash the program
#so they completely run to the end and wouldn't cause any prompt from python but would be not give you
#what you want

a = 2
b = 4
ans = a + b / 2
print(ans) #the output would be 4 instead of 3 if you want to carry out the average of the two numbers
#this because of the BODMAS rule, division would be carried out by the console before the addition
#so for a correct average of two numbers code
ans = (a + b) / 2
print(ans) #this is the correct code

#runtime errors
# these errors occur when you ask Python to run the application, and it finds an error when its parsing through
#the entire code before compiling it
a = 1
b = 2
print(int(2.5)
print(a + b)

#the above code would give a syntax error on line 44 (even though the Syntax is correct on that line)
#check 06.png for the image of the error or try it yourself
#this makes it a little bit hard to identify where the error is
#so it is often better to look before and after the ^ icon
#in this case, the error was before the ^


#Name error
#using the previous code, let's make any error
print(c) #this would ouput a NameError because c isn't defined or doesn;t exist
#check 07.png

#Type Error
print(1 + "2")# this would give an error named TypeError: unsupported operand type
#this is because string can't be addded to integers
#check 08.png

#Zero division error
print(a/0)
#python can't process this specific division

#now not all the kind or type of errors are treated here, over this course of this project
#more errors would be made and explained
#AND if you need help with any error or problem, you can search the particular error or ask a good question
#on exchange platforms showing your code and what you intended to achieve
