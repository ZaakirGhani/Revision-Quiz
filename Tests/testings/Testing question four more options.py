#Testing question four more options

bold_divider = '______________________'
divider = '------------------------'

#4 MARK question FUNCTION with 2 options
def four_marks_more_options(questions,Label1, label2):
    score=0

    for question in questions:
        print(question[0])
        user_input1 = input(f"{divider}\n{Label1} ").strip().lower()
        user_input2 = input(f"\n{label2} ").strip().lower()
        
        users_inputs = [user_input1, user_input2]  # Store both responses

        score_count = sum(
            any(word in user_response for word in question[i])
            for user_response in users_inputs
            for i in range(1, 5)  # Check against all four answer lists
        )

    #4 marks
        if score_count == 4:
            print(f"{bold_divider}\nCorrect\n")
            score+=4
    #3 marks
        elif score_count == 3:
            print(f"{divider}Good job, 3 marks\n")
            score+=3
    #2 marks    
        elif score_count == 2:
            print(f"{divider}\nGood job, 2 marks\n")
            score+=2
    #1 mark
        elif score_count == 1:
            print(f"{divider}\nAlmost, you got 1 mark\n")
            score+=1
        else:
            print(f"{divider}\nIncorrect\n")
            score+=0
    return score

 #question 10d
print('Personal information about users will be held in this system.\n')

question_10d = [('10d. Explain two ways that the company can ensure that it meets the requirements of\ndata protection laws. (4 marks)',
                     ['adequate security measures are in place','audit data stored'],
                     ['such as encryption','such as firewalls','ensure only essential data is kept'],
                     ['appoint a data protection officer','appoint a data controller','train employees'],
                     ['monitor compliance with laws','correct working practices are adhered to'])]

question_10d_score = four_marks_more_options(question_10d,'1.','2.')
