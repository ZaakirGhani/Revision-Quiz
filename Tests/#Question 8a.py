divider = '_______________________'

#Pseudocode FUNCTION
def pseudocode(questions):
    #User input is stored in a list
    pseudocode = []
    print('\nEnter Pseudocode\n')

    #Score
    score=0

    #To intiate if statements and end the code in a list for it to be searched
    indenting = ['if','elseif','elif','else']
    ending_pseudocode = ['endcode','finish','end code','fin']
    
    #Looping user input pseudocode
    while True:
        #Inputting pseudocode
        user_input = input("> ").lower().strip()
        
        #Checking if statements variants are typed in to intiate another user input
        if any(word in user_input for word in indenting):
       
            indentation = input(">>    ").lower().strip()
            pseudocode.append(f'{user_input}\n{indentation}')
        #User inputs end to end loop 
        elif any(word in user_input for word in ending_pseudocode):
            break
        #User input is appended into the list
        else:
            pseudocode.append(user_input)
            
    #Marking based on the users inputing their pseudocode
    for question in questions:
        answer1_match = any(word in pseudocode for word in question[1])
        answer2_match = any(word in pseudocode for word in question[2])
        answer3_match = any(word in pseudocode for word in question[3])
        answer4_match = any(word in pseudocode for word in question[4])
        answer5_match = any(word in pseudocode for word in question[5])
        answer6_match = any(word in pseudocode for word in question[6])
            
        #Adding all the point by point answers together
        score_count = sum([answer1_match, answer2_match, answer3_match, answer4_match, answer5_match, answer6_match])
        
        #6 marks
        if score_count == 6:
            print(f"{divider}\nCorrect\n")
            score+=6
        #5 marks
        elif score_count == 5:
            print(f"{divider}\nGreat job 5 marks\n")
            score+=5
        #4 marks
        elif score_count == 4:
            print(f"{divider}Good job, 4 marks\n")
            score+=4
        #3 marks    
        elif score_count == 3:
            print(f"{divider}\nGood job, 3 marks\n")
            score+=3
        #2 marks
        elif score_count == 2:
            print(f"{divider}\nAlmost, you got 2 mark\n")
            score+=2
        #1 marks
        elif score_count == 1:
            print(f"{divider}\nAlmost, you got 1 mark\n")
            score+=1
        #0 marks
        else:
            print(f"{divider}\nIncorrect\n")
            score+=0
    #Returning score when the FUNCTION is called for
    return score



question_8a =  [('Develop a section of code that will calculate and output the training level\nof an activity. (6 marks)',
                     ['avg_heart_rate','start_time','end_time','receive start_time from device','receive end_time from device','receive avg_heart_rate from device'],
                     ['set duration to 0', 'duration=end_time - start_time'],
                     ['if duration<30 then\nlevel="low"',"if duration<30 then\nlevel='low'",'if duration < 30 then\nlevel = "low"',"if duration < 30 then\nlevel='low'",'if duration < 30 then\nlevel = "low"',"if duration < 30 then\nlevel='low'"],
                     ['elseif duration>30 and avg_heart_rate > 150 then\nlevel="high"', "elseif duration>30 and avg_heart_rate > 150 then\nlevel='high'","elseif duration > 30 and avg_heart_rate > 150 then\nlevel='high'"],
                     ['else\nlevel="medium"',"else\nlevel='medium'","else\nlevel = 'medium'",'else\nlevel = "medium"'],
                     ['send level to display','display level','output level'])]

question_8a_score = pseudocode(question_8a)

score =  question_8a_score

print(score)