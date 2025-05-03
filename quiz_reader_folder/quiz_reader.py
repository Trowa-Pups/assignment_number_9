#Import or make a program that reads the files that "quiz_creator.py" created
import os #Still using os for I am more familiar in it
import colorama #Importing it because i seen it in my yt feed and i thought i could use it to satisfy the "astig" factor
import random #Importing it because i need it to randomize the questions 
from colorama import Fore #Importing Fore to change text color
import time #Importing it to make a delay in the terminal to make the flow more natural

#Ask the user to input what quiz number they want to read
#Importing this section from my quiz creator
quiz_number = str(input("Please input what quiz you are going to edit or create Ex.(quiz_#_1.txt): "))

downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads") 

file_path = os.path.join(downloads_folder, quiz_number) 

#Make the user answer the quiz
if os.path.exists(file_path): #To check if the file is there or not
    print(Fore.BLUE + "Reading file...")
    time.sleep(1)
    with open(file_path, "r") as file: #Opens the files and reads it with "r"
        file_lines = file.readlines()

right_answer_list = [] #To store the right/correct answers in the quiz
question_list = [] #To store the questions to randomize later
temporary_storage = "" #To temporary store the entire question

#To seperate the lines in the file into seperate lines
for line in file_lines: 
    line = line.strip() 

    if line.startswith("Question"): #To check if the line is the question
        temporary_storage += line + "\n" #To store the line in the temporary storage
    
    elif line.startswith("A:") or line.startswith("B:") or line.startswith("C:") or line.startswith("D:"): #To check if the line are the answers
        temporary_storage += line + "\n" #To store the line in the temporary storage

    elif line.startswith("Right Answer"): #To check if the line is the correct answer in the current question
        line = line.replace("Right Answer: ", "") #Removes the "Right Answer: " to make the answer remain 
        right_answer_list.append(line) #To store the answer in the list
        question_list.append(temporary_storage) #To store the question in the list
        temporary_storage = "" #To reset the temporary
        

quiz_data = list(zip(question_list, right_answer_list)) #Using list(zip()) to correctly pair the question and answer and put it on a lis
random.shuffle(quiz_data)

print(Fore.GREEN + "🚀  Welcome to " + quiz_number + "! 🚀 \n Answer the quiz by inputting letters like (A, B, C, and D):") 
time.sleep(2) #Made a 2 second delay to make sure the user sees the title

user_score = 0 #The score of the user

for question_number, (question, correct_answer) in enumerate(quiz_data): #Using enumerate to get the question number and get the question and correct answer from quiz_data
    print(Fore.WHITE + f"Question no.({question_number + 1}):") #To print the question to the terminal
    print(Fore.WHITE + question) 
    
    user_answer = input(Fore.WHITE + "Please input your answer(Ex: A): ").lower() #Ask the user to answer the question and use lower() to make it the same case as the correct answers

#Evaluate the user's answers and give a score
    if user_answer == correct_answer: #To check
        print(Fore.GREEN + "\nYou are correct! ✅")
        user_score += 1 #To add one point in the user's score
        time.sleep(1) #To make it more natural
    
    else:
        print(Fore.RED + "\nYou are wrong! ❌")
        time.sleep(1) #To make it more natural

if user_score == len(quiz_data): #Using len() to count the amount of things in the list(quiz_data) and seeing if user_score is equal to it
    print(Fore.YELLOW + "\nYou got a perfect score! 💯 Congratulations!" , user_score , "/" , len(quiz_data))

elif user_score >= len(quiz_data)// 2: #To see if score is equal or greater than half of the quiz
    print(Fore.YELLOW + "\nNice try! ❤ Better luck next time! 🍀" , user_score , "/" , len(quiz_data))

else: #If the score is less than half
    print(Fore.YELLOW + "\nYou tried your best! Keep studying! 📖", user_score , "/" , len(quiz_data))