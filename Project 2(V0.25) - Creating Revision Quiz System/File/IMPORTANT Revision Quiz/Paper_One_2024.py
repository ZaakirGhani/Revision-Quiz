#This is PAPER ONE 2024 |DESIGN AND DIGITAL PRODUCTION|
#The first section displays functions that help mark the grade
#The second section displays all the questions and defines the mark schemes with the help of the first section

#Modules
import time
import nltk
from nltk.corpus import wordnet
import csv
import matplotlib.pyplot as plt



#Display Universal Splitter
divider =('-------------------------------')
bold_divider = ('_____________________________________')

#|THE FIRST SECTION - THE FUNCTIONS THAT MARKS USERS INPUT|
#Flowchart FUNCTION
def flowchart(questions):
    flowchart = []
    print('(START)')
    signal = True

    while signal:
        user_input = input('Enter flowchart: ').lower().strip()
        if user_input in ['decision', 'diamond','dia']:
            decision = input('DECISION: ').lower().strip()
            if_yes = input('IF YES: ').lower().strip()
            if_no = input('IF NO: ').lower().strip()
            
            flowchart.append(decision)
            flowchart.append(if_yes)
            flowchart.append(if_no)
            signal = True

        elif user_input in ['process', 'rectangle','rec']:
            process = input('PROCESS: ').lower().strip()
            flowchart.append(process)
            signal = True

        elif user_input in ['input','output','parelleogram','par']:
            input_output = input('INPUT/OUTPUT: ')
            flowchart.append(input_output)
            signal = True

        elif user_input in ['end']:
            print('(END)')
            signal = False
        else:
            print('Retry')
            signal = True
    
    score=0
    for question in questions:
        answer1_match = any(word in flowchart for word in question[1])
        answer2_match = any(word in flowchart for word in question[2])
        answer3_match = any(word in flowchart for word in question[3])
        answer4_match = any(word in flowchart for word in question[4])
        answer5_match = any(word in flowchart for word in question[5])
            

        #Adding all the point by point answers together
        score_count = sum([answer1_match, answer2_match, answer3_match, answer4_match, answer5_match])

    
        #6 marks
        if score_count == 5:
            print(f"{bold_divider}\nCorrect\n")
            score+=6
        #5 marks
        elif score_count == 4:
            print(f"{divider}\nGreat job 5 marks\n")
            score+=5
        #4 marks
        elif score_count == 3:
            print(f"{divider}Good job, 4 marks\n")
            score+=4
        #3 marks    
        elif score_count == 2:
            print(f"{divider}\nGood job, 3 marks\n")
            score+=3
        #2 mark
        elif score_count == 1:
            print(f"{divider}\nAlmost, you got 2 mark\n")
            score+=2
        else:
            print(f"{divider}\nIncorrect\n")
            score+=0
    return score


#Pseudocode FUNCTION
def pseudocode(questions):
    #User input is stored in a list
    pseudocode = []
    print('\nEnter Pseudocode:')

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
            print(f"{bold_divider}\nCorrect\n")
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


#1 MARK questions FUNCTION
def one_marks(questions):
    score=0
 
     #Outputing question and checking if answer is correct within a loop.
    for Question,Answers in questions:
        print(f"{Question}")
        #Entering Answer
        user_input = input(f"{divider}\nEnter your answer: ").strip().lower()
        if user_input in Answers:
            print(f"{bold_divider}\nCorrect\n")
            score+=1
        else:
            print(f"{divider}\nIncorrect\nAnswer: {Answers[0]}\n")
    return score


#2 MARK question FUNCTION
def two_marks(questions):
   
    score=0
    for question in questions:
        print(question[0])
        user_input = input(f"{divider}\nEnter your answer: ").strip().lower()
        answer1_match = any(word in user_input for word in question[1])
        answer2_match = any(word in user_input for word in question[2])

        score_count = sum([answer1_match, answer2_match])
    #3 marks
        if score_count == 2:
            print(f"{bold_divider}\nCorrect\n")
            score+=2
    #2 marks    
        elif score_count == 1:
            print(f"{divider}\nGood job, 1 mark\n")
            score+=1
        else:
            print(f'{divider}\nIncorrect\n')
    return score


#3 MARK question FUNCTION
def three_marks(questions):
    score=0

    for question in questions:
        print(question[0])
        user_input = input(f"{divider}\nEnter your answer: ").strip().lower()
        answer1_match = any(word in user_input for word in question[1])
        answer2_match = any(word in user_input for word in question[2])
        answer3_match = any(word in user_input for word in question[3])

        score_count = sum([answer1_match, answer2_match, answer3_match])

    #3 marks
        if score_count == 3:
            print(f"{bold_divider}\nCorrect\n")
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


#4 MARK question FUNCTION
def four_marks(questions):
    score=0

    for question in questions:
        print(question[0])
        user_input = input(f"{divider}\nEnter your answer: ").strip().lower()
        answer1_match = any(word in user_input for word in question[1])
        answer2_match = any(word in user_input for word in question[2])
        answer3_match = any(word in user_input for word in question[3])
        answer4_match = any(word in user_input for word in question[4])

        score_count = sum([answer1_match, answer2_match, answer3_match, answer4_match])

    #4 marks
        if score_count == 4:
            print(f"{bold_divider}\nCorrect\n")
            score+=4
    #3 marks
        elif score_count == 3:
            print(f"{divider}\nGood job, 3 marks\n")
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


#6 MARK question FUNCTION
def six_marks(questions):
    score=0

    for question in questions:
        print(question[0])
        user_input = input(f"{divider}\nEnter your answer: ").strip().lower()
        answer1_match = any(word in user_input for word in question[1])
        answer2_match = any(word in user_input for word in question[2])
        answer3_match = any(word in user_input for word in question[3])
        answer4_match = any(word in user_input for word in question[4])
        answer5_match = any(word in user_input for word in question[5])
        answer6_match = any(word in user_input for word in question[6])

        score_count = sum([answer1_match, answer2_match, answer3_match, answer4_match, answer5_match, answer6_match])

    #6 marks
        if score_count  == 6:
            print(f"{bold_divider}\nCorrect\n")
            score+=6
    #5 marks
        elif score_count == 5:
            print(f"{divider}\nGreat job, 5 marks!\n")
            score+=5
    #4 marks
        elif score_count == 4:
            print(f"{divider}\nGood job, 4 marks\n")
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



#Nine marks for the evaluation
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
            print(f'{divider}\nUnfortutunately, this is one mark!!\n')
            score+=1
        elif FULL_SCORE == 2:
            print(f'{divider}\nAlmost, you got 2 marks\n')
            score+=2
        elif FULL_SCORE == 3:
            print(f'{divider}\nAlmost, you got 3 marks\n')
            score+=3
        elif  FULL_SCORE == 4:
            print(f'{divider}\nGood, you got 6 marks\n')
            score+=6
        #Full marks
        elif FULL_SCORE == 5:
            print(f'{divider}\nGood, you got 7 marks\n')
            score+=7
        elif FULL_SCORE == 6:
            print(f'{bold_divider}\nGreat, you got full marks.\n')
            score+=9
        else:
            score=0
            print(f'{divider}\nIncorrect\n')
    
    return score


#twelve marks variation one: Marks two benefits and drawbacks 
def twelve_marker_evaluation_variation_one(questions):
    score=0
    for question in questions:
        print(question[0])
        user_input = input(f"{divider}\nEnter your answer: ").strip().lower()

        benefits = any(word in user_input for word in question[1])
        benefits2 = any(word in user_input for word in question[2])
        drawbacks = any(word in user_input for word in question[3])
        drawbacks2 = any(word in user_input for word in question[4])
        conclusion = any(word in user_input for word in question[5])

        full_marks_1 = all(word in user_input for word in question[1])
        full_marks_2 = all(word in user_input for word in question[2])
        full_marks_3 = all(word in user_input for word in question[3])
        full_marks_4 = all(word in user_input for word in question[4])
        full_marks_5 = all(word in user_input for word in question[5])

        score_count = sum([benefits, benefits2, drawbacks, drawbacks2, conclusion])

        full_marks = sum([full_marks_1, full_marks_2, full_marks_3, full_marks_4, full_marks_5])

        FULL_SCORE = sum([score_count, full_marks])
        
        #Some marks
        if FULL_SCORE == 1:
            print(f'{divider}\nUnfortutunately, this is one mark!!\n')
            score+=1
        elif FULL_SCORE == 2:
            print(f'{divider}\nAlmost, you got 2 marks\n')
            score+=2
        elif FULL_SCORE == 3:
            print(f'\n{divider}Almost, you got 3 marks\n')
            score+=3
        elif  FULL_SCORE == 4:
            print(f'\n{divider}Good, you got 4 marks\n')
            score+=4
        elif FULL_SCORE == 5:
            print(f'\n{divider}Good, you got 5 marks\n')
            score+=5
        #Full marks
        elif FULL_SCORE == 6:
            print(f'{divider}\nGood, 8 marks.\n')
            score+=8
        elif FULL_SCORE == 7:
            print(f'{divider}\nGreat, 9 marks\n')
            score+=9
        elif FULL_SCORE == 8:
            print(f'{divider}\nGreat, 10 marks\n')
            score+=10
        elif FULL_SCORE == 9:
            print(f'{divider}\nExcellent, 11 marks\n')
            score+=11
        elif FULL_SCORE == 10:
            print(f'{bold_divider}\nCorrect, Full marks\n')
            score+=12
        else:
            score=0
            print(f'\nIncorrect!!!\n')
    return score
#/END OF FIRST SECTION\



#|THE SECOND SECTION - DISPLAYS AND USES THE FIRST SECTION FUNCTIONS TO CALCULATE THE MARKS AS WELL AS DISPLAY QUESTIONS AND SET THE MARK SCHEME PATTERNS|
#Paper 1 function
def paper_1_2024():
    print("_______________\nPaper 1 2024")

    #Marks
    marks = 0
     
    #Display first Question
    print(f'\nFigure 1\n{bold_divider}')
    print("1 ENTRY_COST = 12.50")
    print("2")
    print("3 NumofTickets = input(''How many tickets do you wish to buy?'')")
    print("4 NumofTickets = int(NumofTickets)")
    print("5")
    print("6 CostofTickets = NumofTickets * ENTRY_COST")
    print("7")
    print("8 (''Total cost is'', CostofTickets)\n______________________________")
   
    #Question 1a and 1b
    questions_1a_and_1b = [
    ("1a. Identify one constant used in the program shown in Figure 1. (1 Mark)",['ENTRY_COST','entry_cost','entry cost']),
    ("1b. Identify one variable used in the program shown in Figure 1. (1 Mark)",['numoftickets','costoftickets'])
    ]
    
    question_1a_1b_score = one_marks(questions_1a_and_1b)
            
    #Question 1c and 1d: NEEDS MORE WORK SUCH AS NLTK
    question_1c_and_1d = [
    ("1c. Describe how accepted style conventions have been used to make the code in \nFigure 1 more readable. (3 Marks)",
     ['sensible naming styles', 'sensible naming style', 'pep 8','pep8','conventions'],
     ['camelcase', 'snakecase', 'pascalcase','camel case','snake case','pascal case','meaningful identifiers','spacing'],
     ['convey the purpose of each variable', 'variable', 'clarify code structure',' start and end of words','function']),
    
    ("1d. Explain why line 4 in Figure 1 is needed. (3 Marks)",
      ['input is a string','input','string'],
      ['converted into an integer','changed into an int','integer','int'],
      ['used in calculations','avoid runtime errors','avoid errors']
    )
]
    #Outputing and intiating mark system
    question_1c_1d_score = three_marks(question_1c_and_1d)
        
    #Question 2
    question_2 = ("\n2. State two professional organisations that provide guidance on accessibility and \nquality in IT systems. (2 Marks)")        
    print(question_2)
    
    #Enter Answer
    print("______________\nName two:")
    Enter_1 = input("1: ")
    
    question_2_answer = ['ISO','W3C','IETF','BCS','IEEE','NTSE']
    
    if any(word in Enter_1 for word in question_2_answer):
        marks+=1
        print("Correct")
    else:
        print("Incorrect")
    
    Enter_2 = input("2: ")
    
    if any(word in Enter_2 for word in question_2_answer) and Enter_2 != Enter_1:
        marks+=1
        print("Correct")
    elif Enter_1 == Enter_2:
        print("Thats two answer so only one mark!")
    else:
        print("Incorrect!!")
    
    #question 3
    question_3 = [("\n3. Describe how company culture can be established. (3 Marks)", ['define company values','company values'],
    ['communicate these values to employees','communicate values','talk about values','introduce values to employees'],
    ['employ people that fit with these values','train employees','train employees to the culture',  'training staff','train staff','fit with these values'])]
    
    question_3_score = three_marks(question_3)

    #Question 4
    print(f'4. An application is being written for a decorating company. Some Python code from\nthe application is shown in Figure 2.\nThe code does not work as intended.\n\nFigure 2\n{bold_divider}')
    print('1 Area = 0.0\n2')
    print('3 Length = input("Enter length of wall")')
    print('4 Height = input("Enter height of wall")\n5')
    print('6 if Area > 100.0:')
    print('7    print("This job will take more than one day")\n8')
    print('9 Area = float(Length) * float(Height)\n10\n')
    
    #Question 4a and 4b
    question_4_a_and_b =[
        ('4a. Describe how a mathematical operator has been used in the code shown\nin Figure 2 (3 marks).',['multiplication operator'],
         ['length and height','length','height'],
         ['calculate the area','area']),

        ('4b. Explain why the code written in Figure 2 will not work as intended. (3 marks)', 
         ['sequence wrong','sequence','area will always be zero entering the decision','area','zero'],
         ['as the area is calculated after the decision','because area calculated after decision','area calculated after'],
         ['so the program will never state if the job will take more than one day','condition will never be true','conditon','never true','say if the job will take more','one day'])
    ]

    #Question score
    question_4_score = three_marks(question_4_a_and_b)
    

    #Question 5
    print(f'5. An application is being written for a camp site. One function is shown in Figure 3.\n\nfigure 3\n{bold_divider}')
    print('1 def calc_cost(NumofNights, Month):')
    print('2    if Month > 4 and Month < 9:')
    print('3        NightlyCost = 30')
    print('4    else:')
    print('5        NightlyCost = 28')
    print('6    TotalCost = NumofNights * NightlyCost')
    print('7    return TotalCost\n')

    #Question 5a
    question_5a = [('5a. Write a line of code that will store the total cost of a 6 night stay in month 12. (4 marks)',['declaring a variable (e.g. cost_of_stay = )','declaring a variable'],
                    ['calling function correctly'],
                    ['passing numofnights parameter correctly'],
                    ['passing month parameter correctly'])]
    
    question_5a_score = four_marks(question_5a)

    #Question 5b
    question_5b = [('5b. Describe how the developer has used relational operators in the code. (2 marks)',['greater than 4', 'less than 9'],
                    ['checking if month in range','to allocate correct price'])]

    question_5b_score = two_marks(question_5b)

    #Question 6
    print('6. A program is needed that will calculate the difference between two whole\npositive numbers.\n')
    print('For example if the numbers 2 and 6 are entered then the difference is 4, if the\nnumbers 10 and 8 are entered the difference is 2.\n\nThe program must:\n\n')
    print('a. Allow the user to enter the first number\nb. Check that the number input is a whole positive number\nc. Allow the user to enter the second number\nd. Check that the number input is a whole positive number')
    print(f'e. Calculate the difference\nf. Output the difference\n\nDraw a flowchart that meets the rules of the program.\nUse the space provided on the next page (6 marks)\n{divider}\nTO END THE FLOWCHART, TYPE: "end"\n\nTO INTIATE FLOWCHART SHAPES, TYPE:')
    print("- DECISION SHAPES: 'decision', 'diamond','dia'\n- PROCESS SHAPES: 'process', 'rectangle','rec'\n- INPUT/OUTPUT SHAPES: 'input','output','parelleogram','par'\n")

    
    question_6 = [('\nDraw a flowchart that meets the rules of the program.\nUse the space provided on the next page (6 marks)',
                         ['number1','number2','number 1','number 2','enter number1','enter number2'],
                         ['number1>0','number2>0','number1>-1','number1>-1','number1 > 0','number2 > 0','number1 > -1','number2 > -1'],
                         ['number1>number2','number1 > number2','number 1 > number 2','number2<number1','number2 < number1','number 2 < number 1'],
                         ['difference=number1-number2','difference=number1-number2'],
                         ['display difference','output difference'])]

    question_6_score = flowchart(question_6)

    #Question 7
    print('7. A company needs to develop a new program.\n')
    print('This program needs to be developed as quickly as possible, and the company has')
    print('identified some components that can be reused from another project.')

    question_7 = [('\nEvaluate the effectiveness of top down design when developing this program. (9 marks)',
                   ['always broken down into smaller units', 'the designer can define the requirements of what the program needs to do',
                    'subunits gets less complex as you progress',
                    'tasks and code can be reused again',
                    'saves time','units can be updatable'],
                    ['inflexible decisions','time consuming','testing stubs','testing requires stubs',
                      'modules are very specific','existing components','existing components cannot be used again',
                      'dependent on the bigger picture'],
                    ['breaking down the bigger picture into smaller problems','time consuming and inflexible decisions can slow down progress','use of studs can make the process more complex', 
                       'better team coordination', 'easy reusable code','team can reuse components'])]
    
    question_7_score = nine_marks_evaluation(question_7)

    #SECTION A MARKS
    #Adding the total marks
    calculated_section_A_marks = question_4_score + question_3_score + question_1c_1d_score + question_1a_1b_score + question_5a_score + question_5b_score + question_6_score + question_7_score + marks 

    print(f"\n#########################################\nCongrats on your SECTION A you got: {calculated_section_A_marks}/40\n#########################################")

    #SECTION B
    print('SECTION B\n')

    #Question 8a
    print('8.  A company is developing a smartphone-based fitness app. This app will work with\nwearable technology to track user activities such as cycling, walking and running.')
    print('\n(a) The app will calculate how hard a user has trained during an activity and assign\nthe activity a training level.\nThe app will use this logic to determine the training levels:')
    print('\n• Low level - A duration of less than 30 minutes.\n• High level - A duration of more than 30 minutes and an average heart rate of\nmore than 150 beats per minute.')
    print('• All other activities are considered medium.\n\nThe app will:\n\n• receive the start time, end time and average heart rate\n• calculate the duration of the activity\n• calculate the training level of the activity')
    print(f'• output the training level of the activity.\n{divider}\nDevelop a section of code that will calculate and output the training level\nof an activity. (6 marks)')
    print(f"{divider}\nTO END THE PSEUDOCODE, TYPE: 'endcode','finish','end code' or 'fin'")

    question_8a =  [('Develop a section of code that will calculate and output the training level\nof an activity. (6 marks)',
                     ['avg_heart_rate','start_time','end_time','receive start_time from device','receive end_time from device','receive avg_heart_rate from device','starttime','endtime'],
                     ['set duration to 0', 'duration=end_time - start_time'],
                     ['if duration<30 then\nlevel="low"',"if duration<30 then\nlevel='low'",'if duration < 30 then\nlevel = "low"',"if duration < 30 then\nlevel='low'",'if duration < 30 then\nlevel = "low"',"if duration < 30 then\nlevel='low'"],
                     ['elseif duration>30 and avg_heart_rate > 150 then\nlevel="high"', "elseif duration>30 and avg_heart_rate > 150 then\nlevel='high'","elseif duration > 30 and avg_heart_rate > 150 then\nlevel='high'"],
                     ['else\nlevel="medium"',"else\nlevel='medium'","else\nlevel = 'medium'",'else\nlevel = "medium"'],
                     ['send level to display','display level','output level'])]
    
    question_8a_score = pseudocode(question_8a)
    
    #Question 8b
    question_8b = [('8b. Describe two ways that the developer could use abstraction when developing\nthe app. (4 marks)',
                          ['decide on the needed inputs','needed inputs'],
                          ['formulate key actions in the program','make key actions in the program'],
                          ['identify necessary data','filter out unnecessary detail','identify data needs','data needs'],
                          ['deciding on the inputs to the system','decide on the inputs','deciding on what will vary'])]
    
    question_8b_score = four_marks_more_options(question_8b,'1.','2.')

    #Question 8c
    question_8c = [('8c. Discuss the moral and ethical issues of using wearable technology to track user\nactivities through a fitness app. (6 marks)',
                    ['changes behaviour of individuals','finite resources to manufacture these devices','such as home/work locations and health data','encourage more physical activity such as walking & cycling'],
                    ['desire to have increasing fitness scores','fear that data gathered by wearable devices could be misused if not adequately protected','could be extracted from the data','inaccurate health indicators'],
                    ['cause users to push themselves past safe activity levels','example health insurance companies','this could raise privacy concerns/legal issues'],
                    ['endangering their health','endangering their health(safety in relation to running and cycling)','location data','unequal access to wearable technologies'],
                    ['environmental issues','used for targeted marketing','due to cost or connectivity issues'],
                    ['due to consumption of energy','potentially sensitive information','result in some people gaining an unfair advantage when preparing for events','unfair advantage'])]

    question_8c_score = six_marks(question_8c)

    #question 9a
    print('9. A company is developing new software to train student nurses.')

    question_9a = [('(a) Explain two ways that an acceptable use policy will govern staff conduct when\ndeveloping the software. (4 marks)',
                    ['list prohibited activities','stipulate working practices'],
                    ['penalties for not adhering to these rules','avoid confusion to new employees'],
                    ['list permitted activities','stipulate etiquette rules'],
                    ['internal and external communication','will aid data security'])]

    question_9a_score = four_marks_more_options(question_9a,'1.','2.')

    #question 9b
    question_9b = [('9b. Explain two ways that a developer may express an algorithm. (4 marks)',
                    ['uses existing code','flowcharts'],
                    ['express concepts using diagrams','pseudocode'],
                    ['uses coding concepts','written description'],
                    ['explained as a narrative','annotated code'])]

    question_9b_score = four_marks_more_options(question_9b,'1.','2.')

    #question 9c
    print('The training software will be integrated with Augmented Reality (AR) and\nVirtual Reality (VR).\n')

    question_9c = [('9c. Evaluate the use of AR and VR to train nurses. (9 marks)',
                    ['immersive lesson','created that transport learners outside the classroom','this would give them the opportunity to','virtually visit a hospital', 'to walk around a care home', 'ar can be used in lectures',
                     'superimpose internal organs on to the body','other pupils so learners','better appreciate anatomy','may increase leaner engagement','improve focus and knowledge retention','simulate a training environment','allows nurses to practice without risk to human life'],
                    ['technologies are still developing','environment portrayed such as internal organ','operating theatres may not appear realistic',
                     'health issues','motion sickness','eyestrain','could affect learning duration','no awareness of the real world','cause accidents to users','inaccessible to some learners with eyesight problems'],
                    ['nurses have a greater understanding','further research must be conducted'])]
    
    question_9c_score = nine_marks_evaluation(question_9c)

    #question 10a
    print("\n10. An online game is being developed. One module being developed will be used to\nprocess users' details.\n\n(a) New users will be able to select a suitable username (e.g. Wizard82) and the\n\namount of credit they wish to add to their account (e.g. 7.89).\n\n")

    question_10a = [('Explain the most appropriate data type for each variable. (4 marks)',
                     ['string'],
                     ['username could contain a mixture of characters','username could contain more than one character'],
                     ['real','float'],
                     ['user could add values containing','pound','pence','decimal number','allow the credit','added to existing credit'])]

    question_10a_score = four_marks_more_options(question_10a,'Username:','Credit_Added:')

    #question 10b
    print('The user must also enter their mobile phone number.\n\nOne suitable validation technique to check the data entered would be a\npresence check.\n')

    question_10b = [('10b. Describe two other suitable validation techniques that could be used for\nthis data. (4 marks)',
                     ['length check'],
                     ['contains acceptable number of characters'],
                     ['format check'],
                     ['no invalid characters','entered string starts with 0 or +','check string starts with 0 or +','check string starts with 0 or add','entered string starts with 0 or add'])]

    question_10b_score = four_marks_more_options(question_10b,'1.','2.')

    #question 10c
    question_10c = [('10c. Describe how the developer would prepare automated test tools when unit\ntesting this module. (3 marks)',
                     ['test file is created'],
                     ['inserting test data'],
                     ['expected results'])]
    
    question_10c_score = three_marks(question_10c)

    #question 10d
    print('Personal information about users will be held in this system.\n')

    question_10d = [('10d. Explain two ways that the company can ensure that it meets the requirements of\ndata protection laws. (4 marks)',
                     ['adequate security measures are in place','audit data stored'],
                     ['such as encryption','such as firewalls','ensure only essential data is kept'],
                     ['appoint a data protection officer','appoint a data controller','train employees'],
                     ['monitor compliance with laws','correct working practices are adhered to'])]

    question_10d_score = four_marks_more_options(question_10d,'1.','2.')

    #question 10e
    print('10e. A developer is writing a module that allows users to log on to the online game.\nOne function of this module will be to search through a list of registered\nusernames to find the user details.')
    print('\nEvaluate the suitability of using linear and binary search algorithms to search\nthrough the user list for a specific username.\n\nYour evaluation should include:')

    print('\n• the benefits and drawbacks of each search algorithm')

    question_10e = [('• a supported conclusion as to which algorithm the developer should choose. (12 marks)',
                     ['easy to understand','and develop','list of users','not need to be sorted before searched'],
                     ['very ineffecient','take a long time to complete','some users','could be waiting a long time before their details were retrieved','search increases greatly','o(n),',
                      'could hinder the growth of the number of users accessing the game'],
                     ['efficient','users would be able to access the game with little delay','search time does not grow rapidly','o(log^2n)'],
                     ['more complex algorithm to understand and develop','data must be in order for the algorithm to work'],
                     ['efficent','complexity','should choose binary search if the list is sorted','if unsorted','choose linear search','linear search offers flexibility','linear time complexity'])]
    
    question_10e_score = twelve_marker_evaluation_variation_one(question_10e)

    calcualated_section_B_marks = marks + question_8a_score + question_8b_score + question_8c_score + question_9a_score + question_9b_score + question_9c_score + question_10a_score + question_10b_score + question_10c_score + question_10d_score + question_10e_score

    print(f'\n#############################################\nSection B: {calcualated_section_B_marks}/60\n{bold_divider}')

    #Calculates the full marks (Section A Marks + Section B Marks)
    PAPER_ONE_MARKS = calculated_section_A_marks + calcualated_section_B_marks
    #Display's full marks
    print(f'\nYour marks: {PAPER_ONE_MARKS}/100')
#/END OF SECOND SECTION\