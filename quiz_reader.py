#Import or make a program that reads the files that "quiz_creator.py" created
import os #Still using os for I am more familiar in it
import colorama #Importing it because i seen it in my yt feed and i thought i could use it to satisfy the "astig" factor
import random #Importing it because i need it to randomize the questions 

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

right_answer_list = [] #To store the right/correct answers in the quiz
question_list = [] #To store the questions to randomize later
temporary = "" #To temporary store the entire question

#To seperate the lines in the file into seperate lines
for line in file_lines: 
    line = line.strip() 

    if line.startswith("Question"): #To check if the line is the question
        temporary += line + "\n" #To store the line in the temporary storage
    
    elif line.startswith("A:") or line.startswith("B:") or line.startswith("C:") or line.startswith("D:"): #To check if the line are the answers
        temporary += line + "\n" #To store the line in the temporary storage

    elif line.startswith("Right Answer"): #To check if the line is the correct answer in the current question
        line = line.replace("Right Answer: ", "") #Removes the "Right Answer: " to make the answer remain 
        right_answer_list.append(line) #To store the answer in the list
        question_list.append(temporary) #To store the question in the list
        temporary = "" #To reset the temporary
        

quiz_data = list(zip(question_list, right_answer_list)) #Using list(zip()) to correctly pair the question and answer and put it on a lis
random.shuffle(quiz_data)

for question_number, (question, correct_answer) in enumerate(quiz_data): #Using enumerate to get the question number and get the question and correct answer from quiz_data
    print(f"Question no.({question_number + 1}):") #To test
    print(question) #To test
    print(correct_answer) #To test
#Evaluate the user's answers and give a score