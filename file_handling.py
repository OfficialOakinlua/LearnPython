#Name: Akinlua, Olorunfemi Praise
#Date Created: April 06, 2020
#About: Learn Python (File Handling); Based of the Udemy Python Mega Course
#Version: 1.0
#Python Version: 3.6


#Working with text files (*.txt)
file = open("scholarship.txt", "r") #this python code reads the scholarship txt file (Do know that the python file must be either in the same directory as the txt file or must mention the specific directory and not just the name)
scholarship_content = file.read()
print(scholarship_content)

#the output can be seen in 16.png and can be compared to the image of the text file in 17.png
#now you need to understand that once the read() or readlines() method or function is carried out, if you carry it out again you would an empty []
#because once the txt read, the cursor which is reading the txt file is already at the end and there is nothing at the end.
#to deal with the above, you can aplly a seek method wth an argument so the cursor can go the beginning

file.seek(0)
lined_scholarship_content = file.readlines()
print(lined_scholarship_content)
#readlines() puts all the content in a list after a new line
#as can be seen 18.png

#to remove the \n in the list, you can simply to write the code below
scholarship_content_list = [i.rstrip() for i in lined_scholarship_content] #it's jsut a simplified or one line for loop
print(scholarship_content_list)


#to finish or save any changes or handling of the file, use the close() function
file.close()


#writing a new file
file = open("handler.txt", "w") #creating a new file
file.write("The name of the DSS handler is\nAkinlua Olorunfisayomi") #writing a content into the newly created handler.txt
file.close() #to complete all the above, this operation needs to be done
#output can be seen in 19.png

#you can add a new information to an existing txt files it is basically called appending
#we are going to append a new information to handler.txt
file = open("handler.txt", "a") #preparing the txt file to be appended
file.write("A new handler was discovered, His name is Akinlua, Olorunfunminiyi")
file.close()

#let's add a new feature to the scholarship request system. The new feature is a txt file that shows the list of scholarships you are qualified for

#Updated Advanced Scholarship System
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
        if ((userCountry in schlr["Schlr Applicant"] or schlr["Schlr Applicant"][0] == "All") and (userPassport == True or schlr["Passport"] == False) and schlr["Schlr Status"] == "Open" and userRecommendLetters >= schlr["Recommend Letters"] and userGPA >= schlr["Schlr GPA"] ):
            ListOfSchlrQualified.append(schlr["SchlrShip Name"])

    if (len(ListOfSchlrQualified) > 0):
        print("The number of scholarships you're qualified for is ", len(ListOfSchlrQualified))
        print("The list can be seen below:\n")
        print(*ListOfSchlrQualified, sep = ", ")
    else:
        print("You don't qualify for any scholarships at this time. Do make sure your inputted the right information.")

else:
    if(userCountry == "Nigeria"):
        print("Go to the Under-Age Nigerian Scholarship Site.")
    elif (userCountry == "United Kingdom"):
        print("Go to the Under-Age United Kingdom Scholarship Site.")
    else:
        print("You are regarded as an International Student. Therefore, go to the International Student Site.")
        print("Or you have wrongly spelt the name of your Country")



#the new feature of scholarship txt file
file = open("scholarshipList.txt", "w")

if len(ListOfSchlrQualified) > 0:
    file.write(userName + ", the below are the list of scholarship you qualify for:\n")
    for item in ListOfSchlrQualified:
        file.write(item + "\n")
    file.write("Please do note that there are other requirements for getting the scholarships.")
else:
    file.write("You don't qualify for any scholarship.")

file.close()
#the output can be seen in 20, 21.png

#for other methods, check 22.png


#Additional information
#If you want to work on a file without using the close() function all the time. you can use the with statement
with open("handler", "a+") as text:
    text.seek(0)
    content = text.read()
    file.write("Confidential Information")

#End Of Code
