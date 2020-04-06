#Name: Akinlua, Olorunfemi Praise
#Date Created: April 06, 2020
#About: Learn Python (Modules and Libraries); Based of the Udemy Python Mega Course
#Version: 1.0
#Python Version: 3.6

#Modules
#A module is a piece of software in this case which ends with a .py extension that has a specific functionality

#To access different Modules you have to import them, now you can only import moudles that are on your local computer
#to access thirdparty modules, you need to download them from their servers and then install them within your python environment
#some modules, packages and libraries come default with python and therefore you don't need to download them
#One is OS module which provides a way of using operating system dependent functionality i.e functionality based on maybe Windows or Linux or macOS (unix based)
#to use the OS module, we have to import it

import os #this is the import statement. After this you canuse whatever functions, objects and capabilities are within the OS module

#one of the capabilities is to list the files that are within the same directory as the py file itself using a embedded function called listdir()
os.listdir() #list all the files in a list
os.getcwd() #list the current working directory
dir(os) #to know the different functionality of the particular module. This process is called introspection.
#os.__file___ #to identify where the module file is

#Libraries
#A library is just a collection of python files that can execute a particular capability or capabilities (it is just a wider module par se)
#the way you import module is same way you import libraries as well

import tkinter #tkinter has been imported
import csv#csv library has been imported and via this library you can manipulate excel files (*.csv)
#packages
#packages are just third-party modules and libraries such as matplotlib (mathematics), BeautifulSoup (web scraping), Numpy (Scientific Computation)

#to get thirdparty modules (packages), you can use the following code in your cmd
#pip install numpy #to install numpy. You can check 23.png for images of installation and also the upgrade of pip


#Let's Learn how to create a documentation to how py files
#lets do one for this modules.py File
""" This PY file explains a lot about modules, libraries and packages """


#Working with date and time
#to print time or dates, you can use the datetime module
import datetime
print(datetime.datetime.now()) #would provide a result as seen in 24.png or function-like result if used directly on the python console (25.png)


#You can perform some operations with the datetime module like substracting
now = datetime.datetime.now()
yesterday = datetime.datetime(2020, 4, 5, 10, 49, 34, 0)
time_difference = now - yesterday #datetime.timedelta(1, 32887, 330964) if in python interpreter but if you print it, the output would be something like 1 day, 9:08:07.330964
print(time_difference.days) #would output 1
print(time_difference.total_seconds()) #would output 119287.330964


#you can add a specific amount of days or seconds
after = now + datetime.timedelta(days = 3)
after_sec = now + datetime.timedelta(seconds = 214244)


#let's try another module to import called time
import time
listDateTime = [] #create empty list
for i in listDateTime:
    listDateTime.append(datetime.datetime.now())
    time.sleep(2) #this delays the code for 2 seconds 

#lets create a txt file with a name based on time
filename = datetime.datetime.now()

def createFile():
    """ Creates a TXT file with time-based name """
    with open(filename.strftime("%Y-%m-%d-%H") + ".txt", "w") as file:
        file.write("")

createFile()
#result of the code can be seen in 26.jpg
