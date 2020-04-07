"""
Name: Akinlua, Olorunfemi Praise
Date Created: April 07, 2020
About: English Dictionary
Version: 1.0
Python Version: 3.6
"""

#load JSON Library
import json
from difflib import (SequenceMatcher, get_close_matches)

#load the JSON Data into a varibale
#type dict
dictData = json.load(open("/Users/Hp/Documents/GitHub/LearnPython/projects/dictionary/data.json"))

def dictionary(word):
    #lowers the case of the individual alphabets that make up the word inputted by the user
    word = word.lower()
    #checks for whether the word requested is embedded in our data.json file
    if word in dictData:
        return dictData[word]
    elif word.title() in dictData:
        return dictData[word.title()]
    elif word.upper() in dictData:
        return dictData[word.upper()]
    else:
        allWords = dictData.keys()
        closeMatch = get_close_matches(word, allWords, 1)
        if (len(closeMatch) > 0):
            iPrompt = input(closeMatch[0] + " might be the word you are looking for. \nEnter Yes to check the word %s, and No if this isn't it: " %closeMatch[0])
            if iPrompt.lower() == "yes":
                return dictData[closeMatch[0]]
            elif iPrompt.lower() == "no":
                return "Check for your word again."
            else:
                return "Wrong Entry."
        else:
            return "The word doesn't exist. Please do double check your word input."

#program requests for the word that the users wants to check for the definition
wordInput = input("Enter the word: ")


definition = dictionary(wordInput)

if type(definition) == list:
    for item in range(len(definition)):
        print(str(item + 1) + " " + definition[item])
else:
    print(definition)
