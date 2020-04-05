#Name: Akinlua, Olorunfemi Praise
#Date Created: April 04, 2020
#About: Learn Python (Loops); Based of the Udemy Python Mega Course
#Version: 1.0
#Python Version: 3.6


#Loops
#Loops are used to perform repetitive actions or codes
#In Python, we have different two types of loops namely for and while loop

#For Loop is a control flow statement for specifying iterations over a particular sequence
#which could be a tuple, a dictionary, a set or even a string
#an example for loop is below

shopping_list = ['Milk', 'Bournvita', 'Coffe', 'Condom', 'Bible']

for i in shopping_list:
    print(i)

#the output of the code can be seen in 13.png

#let's make it a little interesting
#let build a mail distribution systems using for loop which only sends
#mail to Gmail accounts

usersMails = ["davidolodo@hotmail.com", "jaycobhari@yahoo.com", "akinluaolorunfemi@gmail.com", "simi@gmail.com"]

for mail in usersMails:
    if "gmail" in mail:
        print("Email sent to " + mail + " successfully.")
    else:
        print("Email not sent. Upgrade to Gmail.")

#output of the code can be seen in 14.png or try it yourself


#Let's improve on our Scholarship Request System with a little of new features based on for loop
#we are going to use for loop to go through a long list of scholarships and check if your are eligible based of
#new inputs such as CGPA, Schools Attended, Number of Recommendation Letters, Current Visa or Passport Status and closing dates
#for above 18


# list of scholarships sourced by the system
schlr01 = {"SchlrShip Name": "Hublot Scholarship", "Schlr Country Origin" : "Nigeria", "Schlr Applicant" : ["All"], "Schlr Status": "Closed", "Schlr GPA" : 3.5, "Recommend Letters" : 0, "Passport": True}
schlr02 = {"SchlrShip Name": "Google Scholarship", "Schlr Country Origin" : "USA", "Schlr Applicant" : ["All"], "Schlr Status": "Open", "Schlr GPA" : 2.0, "Recommend Letters" : 2, "Passport": False}
schlr03 = {"SchlrShip Name": "Tony Elemelu Scholarship", "Schlr Country Origin" : "Nigeria", "Schlr Applicant" : ["Nigeria", "Ghana", "South Africa"], "Schlr Status": "Open", "Schlr GPA" : 2.5, "Recommend Letters" : 0, "Passport": False}
schlr04 = {"SchlrShip Name": "FGN Scholarship", "Schlr Country Origin" : "Nigeria", "Schlr Applicant" : ["Nigeria"], "Schlr Status": "Open", "Schlr GPA" : 0.0, "Recommend Letters" : 2, "Passport": True}
schlr05 = {"SchlrShip Name": "John Holt Scholarship", "Schlr Country Origin" : "USA", "Schlr Applicant" : ["All"], "Schlr Status": "Open", "Schlr GPA" : 2.0, "Recommend Letters" : 0, "Passport": False}


#embeding the above scholarships into a single list
schlrshipList = [schlr01, schlr02, schlr03, schlr04, schlr05]

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
userPassport = input("Do you hold a non-expired Passport? A simple Yes or No will do ")
userPassport = True if userPassport == "Yes" else False
userGPA = float(input("What's is your CGPA? "))
userRecommendLetters = int(input("How many Recommendation Letters do you have? "))


age = age(userYear)

#in order to avoid whitespaces, use strip function
userCountry = userCountry.strip()

#Analysis

ListOfSchlrQualified = []

if (age >= 18):
    for schlr in schlrshipList:
        if ((userCountry in schlr["Schlr Applicant"] or schlr["Schlr Applicant"] == "All") and schlr["Schlr Status"] == "Open" and userRecommendLetters >= schlr["Recommend Letters"] and userGPA >= schlr["Schlr GPA"] ):
            ListOfSchlrQualified.append(schlr["SchlrShip Name"])
else:
    if(userCountry == "Nigeria"):
        print("Go to the Under-Age Nigerian Scholarship Site.")
    elif (userCountry == "United Kingdom"):
        print("Go to the Under-Age United Kingdom Scholarship Site.")
    else:
        print("You are regarded as an International Student. Therefore, go to the International Student Site.")
        print("Or you have wrongly spelt the name of your Country")

if (len(ListOfSchlrQualified) > 0):
    print("The number of scholarships qualified is ", len(ListOfSchlrQualified))
    print("The list can be seen below:\n")
    print(*ListOfSchlrQualified, sep = ", ")
else:
    print("You don't qualify for any scholarships at this time. Do make sure your inputted the right information.")

#We would work on the under-18 part more comprehensively as we progress
