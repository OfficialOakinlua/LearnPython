"""
Name: Akinlua, Olorunfemi Praise
Date Created: April 07, 2020
About: Learn Python (Pandas); Based of the Udemy Python Mega Course
Version: 1.0
Python Version: 3.6
"""


#Pandas
#High Level library used for data mining activities such as web scraping, loading and analysing excrl files, data visualization
#and also working with cumbersome amount of data
#pandas is based on numpy. To install pandas and numpy

#pip install pandas #on your cmd not your python console. Since pandas is based on numpy during installation, it also installs numpy
#pip install numpy

#lets import Pandas
import pandas

#lets create a dataframe which makes things easier to manipulate
df1 = pandas.DataFrame([[2, 4, 5], [10, 20, 30]])

print(df1)

#lets add column name to the DataFrame
df1 = pandas.DataFrame([[2, 4, 5], [10, 20, 30]], columns = ["Price", "Age", "Value"])

print(df1)
#output of the two codes can be seen in 27.png

#lets pass some index or row Name
df1 = pandas.DataFrame([[2, 4, 5], [10, 20, 30]], columns = ["Price", "Age", "Value"], index = ["First", "Second"])

print(df1)
#check 28.png

#you could also create a dataframe using dictionaries
df2 = pandas.DataFrame([{"Name" : "Femi"},{"Name" : "Fisayomi"}])

#check 29 and 30.png for more options

#lets use one of the many function that we can use on a DataFrame
#check the mean of the different columns

print(df1.mean())
#check 31.png or try it yourself

#and to check the overall mean of the entire dataframe do the following
print(df1.mean().mean()) #means you are doing the mean of the columns mean


#to access a single column
df1.Price

#or

df1["Price"]

#the above is called a Series. A dataframe is made up of many series
#and you can apply the methods that work with dataframes to the Series

df1.Price.mean() #would calculate the mean
df1.Price.max() #would output the biggest value

#obviously the above function can only work with floats and integers. Though, there are methods that work with strings and other datatypes
#to be worked on as we go




#let's talk Jupyter
#Jupyter gives an environment to edit and run the scripts especially when it comes to data analysis or data exploration

#to install Jupyter
#pip install jupyter #obviously on cmd

#to create a new Jupyter Notebook
#jupyter notebook #in the folder where you intend to store your files

#From now, most of our coding would be between our IDE and Jupyter
