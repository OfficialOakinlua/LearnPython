#Name: Akinlua, Olorunfemi Praise
#Date Created: April 04, 2020
#About: Learn Python (Conditionals); Based of the Udemy Python Mega Course
#Version: 1.0
#Python Version: 3.6
<<<<<<< Updated upstream
=======


#--------------
#Conditionals
#there are more like control sructures put in place to let a system to a particular when A happens and do
#another thing when B happens and do another when C happens and so on

#If statement
#Very simple. If a condition is fulfilled, do this
x = 4
if (x > 0):
    print("Greater than 0")

#the  above code would print Greater than 0 because the condition in bracket - x > 0 was fulfilled

if (x > 5):
    print("Greater than 5")

#the above code would not output anything has the conditon wasn't fulfilled 4 is less than 5

#If Else statement
#your code becomes a little bit interesting and encompassing when you add an else statement
#ooh, i forgot, a statement is a piece of code to be executed by the intepreter
#so if a condition is fulfilled, do this but if that same condition isn't fulfilled do another thing

if (x > 5):
    print("Greater than 5")
else:
    print("Less than 5")

#the above code would output Less than 5 because 4 is less than 5 and it didn't fulfil the condition set


#If Elif ELse statement
#You can have more than one condition and corresponding output to deal with in your code and
#in order to deal with that, you can simply use the elif statement

if (x > 5):
    print("Greater than 5")
elif (x == 4):
    print("Equals 4")
elif (x == 3):
    print("Equals 3")
else:
    print("Less than 3")

#the above code would print Equals 4
#once a condition is fulfilled, the intepreter would skip the remaining elifs or conditions and more to the
#next block of code

#now you would notice that in the first and second elif, double equal signs were used (==). the reason is because (=) is an assignment operator
#and (==) is an equal to sign
# (!==) -> Not equal to
# (>==) -> Greater than or equal to
# (<==) -> Less than or equal to

#Nested If statement
#You can have an if statement embeded into another if statement

age = 15
country = "NGR"

if (age >= 18):
    if(country == "NGR"):
        print("You are eligible for a full-cost Scholarship. Go to the main Scholarship portal")
    else:
        print("You are ineligible")
else:
    if(country == "NGR"):
        print("Go to the Under-Age Nigerian Scholarship Site.")
    elif (country == "UK"):
        print("Go to the Under-Age United Kingdom Scholarship Site.")
    else:
        print("You are regarded as an International Student. Therefore, go to the International Student Site.")

#the above code would print "Go to the Under-Age Nigerian Scholarship Site." because it didn't fulfil the first conditon but fulfilled
#the NGR condition.
#if the value of the variables were different say country = "UK" and age = 18, it would output "You are ineligible" because it fulfilled the first condition
#and falls under the main if block but doesn't fulfil the second conditon, therefore falling under the else block.


#You can also use user input, functions, and nested conditions to make a little advanced python code
#we can replicate the Scholarship python code using the above features and a little bit of relatability


#--------------------------
#Start of the Advanced Scholarship Code
#functions declaration
def warning():
    print("Do make sure that whatever information you input are true and accurate.")
    print("The Federal Government of Nigeria can prosecute you for any falsified information you input.\nThink carefully before you input your data. Thank You.")

def age(year):
    current_year = 2020
    age = current_year - year
    return age


warning()

#Data Collection
userName = input("Enter Your Full Name: ")
userYear = int(input("Enter Your Birth Year: ")) #converted the inputed data to integer to avoid TypeError messages
userCountry = input("Enter Country Name: ")

age = age(userYear)

#in order to avoid whitespaces, use strip function
userCountry = userCountry.strip()

#Analysis
if (age >= 18):
    if(userCountry == "Nigeria"):
        print("You are eligible for a full-cost Scholarship. Go to the main Scholarship portal")
    else:
        print("You are ineligible")
        print("Or you have wrongly spelt the name of your Country")
else:
    if(userCountry == "Nigeria"):
        print("Go to the Under-Age Nigerian Scholarship Site.")
    elif (userCountry == "United Kingdom"):
        print("Go to the Under-Age United Kingdom Scholarship Site.")
    else:
        print("You are regarded as an International Student. Therefore, go to the International Student Site.")
        print("Or you have wrongly spelt the name of your Country")

#the output of this program can be seen in 13.png or try it yourself
#Do Know that this program isn't fullproof because we have not dealt with all the errors that could pop up for example wrongly inputted data etc.
#this will be treated in try, catch topics
#Though you catch catch the errors by using if statement and type function, you can do that
>>>>>>> Stashed changes
