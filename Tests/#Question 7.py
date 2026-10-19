divider ='___________________'

def nine_marks_evaluation(questions):
    score=0
    for question in questions:
        print(question[0])
        user_input = input(f"{divider}\nEnter your answer: ").strip().lower()

        benefits = any(word in user_input for word in question[1])
        drawbacks = any(word in user_input for word in question[2])
        conclusion = any(word in user_input for word in question[3])

        full_marks_1 = all(word in user_input for word in question[1])
        full_marks_2 = all(word in user_input for word in question[2])
        full_marks_3 = all(word in user_input for word in question[3])

        score_count = sum([benefits, drawbacks, conclusion])

        full_marks = sum([full_marks_1, full_marks_2, full_marks_3])

        FULL_SCORE = sum([score_count, full_marks])
        
     

        #Some marks
        if FULL_SCORE == 1:
            print('Unfortutunately, this is one mark!!')
            score+=1
        elif FULL_SCORE == 2:
            print('Almost, you got 2 marks')
            score+=2
        elif FULL_SCORE == 3:
            print('Almost, you got 3 marks')
            score+=3
        elif  FULL_SCORE == 4:
            print('Good, you got 6 marks')
            score+=6
        #Full marks
        elif FULL_SCORE == 5:
            print('Good, you got 7 marks')
            score+=7
        elif FULL_SCORE == 6:
            print('Great, you got full marks.')
            score+=9
        else:
            score=0
    
    return score

#Question 7
print('7. A company needs to develop a new program.')
print('This program needs to be developed as quickly as possible, and the company has')
print('identified some components that can be reused from another project.')

question_7 = [('Evaluate the effectiveness of top down design when developing this program.(9 marks)',
                   ['always broken down into smaller units', 'the designer can define the requirements of what the program needs to do',
                    'subunits gets less complex as you progress',
                    'tasks and code can be reused again',
                    'saves time','units can be updatable'],
                    ['inflexible decisions','time consuming','testing stubs','testing requires stubs',
                      'modules are very specific','existing components','existing components cannot be used again',
                      'dependent on the bigger picture'],
                    ['breaking down the bigger picture into smaller problems','time consuming and inflexible decisions can slow down progress','use of studs can make the process more complex', 
                       'better team coordination', 'easy reusable code','team can reuse components'])]

q = nine_marks_evaluation(question_7)

scores = q

print(scores)