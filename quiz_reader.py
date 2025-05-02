#Import or make a program that reads the files that "quiz_creator.py" created
import os #Still using os for I am more familiar in it
import colorama #Importing it because i seen it in my yt feed and i thought i could use it to satisfy the "astig" factor

#Ask the user to input what quiz number they want to read
#Importing this section from my quiz creator
quiz_number = str(input("Please input what quiz you are going to edit or create Ex.(quiz_#_1.txt): "))

downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads") 

file_path = os.path.join(downloads_folder, quiz_number) 

#Make the user answer the quiz
if os.path.exists(file_path): #To check if the file is there or not
    print("Reading file...")
    with open(file_path, "r") as file: #Opens the files and reads it with "r"
        file_lines = file.readlines()


#Evaluate the user's answers and give a score