"""
Name: Akinlua, Olorunfemi Praise
Date Created: April 04, 2020
About: Learn Python (Fuctions); Based of the Udemy Python Mega Course
Version: 1.0
Python Version: 3.6
"""


#Functions
#Function is a peice of reuseable code that may or may not have arguments
#that varies their results. They are basically smaller or mini-scripts

def print_2_hello():
    print("hello")
    print("hello")
#this functions doesnt have an argument, and would give the same output evrything
#it is called. The fucntion would print Hello twice

print_2_hello()

def opening_greet(name):
    print("Welcome to LearnPython Tutorial Guide, ", name)
#this fucntion has a single argument, and would output different greet messages
#everytime it is called as long as the argument is different

opening_greet("femi")

#now let's work with variables within a function

def hp_to_watt(hp):
    watt = hp * 0.7068
    return watt
#this function converts horsepower to watt. You should know that watt is a local variable and can't be used
#outside the function.

hp_to_watt(1.8) #should covert 1.8 horsepower to watt
#the only thing is that the above the code wouldn't output anything
#the reason is because you didn't perform any print operation within the function
#and only returned the value
#return is often used with Functions. therefore, if you want to show the results
#you have to use print with the function

print(hp_to_watt(1.8))


#More Fuctions Features
#You can have default argument set in your fucntion. Let's take a look at one
def greetUser(name, company="PROy"):
    print("Welcome to COMM, the next level shopping site. Feel at home, ", name)
    print("Designed by ", company)

greetUser("Femi")
#the output can be seen in 09.png
#PROy has been made a default value assigned to variable company and therefore there is
#no need to specify it has an argument
#though, if you placed the default argument first like
#def greetUser(company="PROy", name):
#it would give you a syntax error as seen in 10.png

greetUser("Femi", "Google")
# so if a value is parsed, it would use the value parsed by you
# In this case, Designed by Google

#def min_to_hours(sec, min):
#    hrs = min / 60 + sec / 3600
#    print(hrs)

#min_to_hours(400, 160) + 10 #this code would give a TypeError because the result of the function
#is a NonType. Error Message can be seen in 11.png

def min_to_hours(sec, min):
    hrs = min / 60 + sec / 3600
    return hrs

print(min_to_hours(400, 160) + 10)

#in order not to have the error message in 11.png, you use return as seen above

#----------------------
#User Input & functions
#Remember the greetUser () function earlier used, we are going to make it a little interactive
#just like when you visit amazon or jumia, you would be probably signup or login, and you name would be asked
#so in how our own little we would create a little interactive session

#let's build our little function
def greetUser(name, company="PROy"):
    return "Welcome to COMM, the next level shopping site. Feel at home, " + name + "\nDesigned by " + company


#let's prompt the user for their name like Amazon and jumia
userName = input("Let PROy know you better, please input your name: ")

#let's show them love
print(greetUser(userName))

#the resulting output can be seen in 12.png
