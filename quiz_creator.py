#Import or make a program that creates or edit a file or something that checks a file
import os #using import os to check files in the computer

#Ask the user to input what quiz number they want to create or edit
quiz_number = str(input("Please input what quiz you are going to edit or create Ex.(quiz_#_1.txt): "))

downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads") #Using expanduser("~") to make it search home directory and put "Downloads" to find the downlaods folder, and using os.path.join to combines all the paths taken to make it one path

file_path = os.path.join(downloads_folder, quiz_number) #Joining both of them to make the full file path

if os.path.exists(file_path): #To check if the file is there or not
    print(f"{quiz_number}" + " will be opened")
    with open(file_path, "a") as file: #Opens the file and it uses 'a' for it doesn't remove previous texts in the file
        number = 0 

        right_answers_list = [] #To store the right answers

        while True: #To make it a loop so that the user can put how much questions they want in the file
            question = str(input(f"Please input the new question, if done, type 'exit': ")) #Ask the user to input their question 

            if question.lower() == "exit": #If the user inputs "exit", make the program break and update the file with the new inputs of the user
                file.write(f"List of right answers: {right_answers_list}") #To write the list after the user exits
                print("Exiting...")
                break

            #Ask the user to input four options, and input the correct answer
            option_a = input("Input option A of the question: ")
            option_b = input("Input option B of the question: ")
            option_c = input("Input option C of the question: ")
            option_d = input("Input option D of the question: ")

            if option_a == option_b or option_a == option_c or option_a == option_d or option_b == option_c or option_b == option_d or option_c == option_d:
                same_answer_detector = str(input("Same answer detected! Do you want to continue? Yes/No: "))
                if same_answer_detector.lower() == "no":
                    file.write(f"List of right answers: {right_answers_list}") #To write the list after the user exits
                    print("Exiting...")
                    break
                
            right_answer = input("Input the right answer Ex.(A): ").lower() #Used lower() to make sure that the letter is always the same
            right_answers_list.append(right_answer) #To store to the list

            file.write(f"Question {number + 1}: {question} \n") #Print the input of the user in the text file
            file.write(f"A: {option_a}\nB: {option_b}\nC: {option_c}\nD: {option_d}\n")
            file.write(f"\n \n Right Answer: {right_answer} \n")

            number += 1 #To change the question number

else:
    print(f"{quiz_number}" + " does not exist")
    print("creating the file...")
    with open(file_path, "w") as file: #Opens the file and using "w", it is the 'write' mode to put texts in the txt file
        
        number = 0 

        right_answers_list = [] #To store the right answers

        while True: #To make it a loop so that the user can put how much questions they want in the file
            question = str(input(f"Please input the Question no.{number + 1}, if done, type 'exit': ")) #Ask the user to input their question 

            if question.lower() == "exit": #If the user inputs "exit", make the program break and update the file with the new inputs of the user
                file.write(f"List of right answers: {right_answers_list}") #To write the list after the user exits
                print("Exiting...")
                break

            #Ask the user to input four options, and input the correct answer
            option_a = input("Input option A of the question: ")
            option_b = input("Input option B of the question: ")
            option_c = input("Input option C of the question: ")
            option_d = input("Input option D of the question: ")

            if option_a == option_b or option_a == option_c or option_a == option_d or option_b == option_c or option_b == option_d or option_c == option_d:
                same_answer_detector = str(input("Same answer detected! Do you want to continue? Yes/No: "))
                if same_answer_detector.lower() == "no":
                    file.write(f"List of right answers: {right_answers_list}") #To write the list after the user exits
                    print("Exiting...")
                    break
                
            right_answer = input("Input the right answer Ex.(A): ").lower() #Used lower() to make sure that the letter is always the same
            right_answers_list.append(right_answer) #To store to the list

            file.write(f"Question {number + 1}: {question} \n") #Print the input of the user in the text file
            file.write(f"A: {option_a}\nB: {option_b}\nC: {option_c}\nD: {option_d}\n")
            file.write(f"\n \n Right Answer: {right_answer} \n")

            number += 1 #To change the question number