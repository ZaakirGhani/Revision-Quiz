#This is PAPER ONE 2024 |DESIGN AND DIGITAL PRODUCTION|
#The first section displays functions that help mark the grade
#The second section displays all the questions and defines the mark schemes with the help of the first section


#Display Universal Splitter
divider =('--------------------------------------------------------------')
bold_divider = ('_________________________________________________________')

#|THE FIRST SECTION - THE FUNCTIONS THAT MARKS USERS INPUT|
#Flowchart FUNCTION
def flowchart(questions):
    flowchart = []
    print('(START)')
    

    while True:
        user_input = input('Enter flowchart: ').lower().strip()
        if user_input in ['decision', 'diamond','dia']:
            decision = input('DECISION: ').lower().strip()
            if_yes = input('IF YES: ').lower().strip()
            if_no = input('IF NO: ').lower().strip()
            
            flowchart.append(decision)
            flowchart.append(if_yes)
            flowchart.append(if_no)
            

        elif user_input in ['process', 'rectangle','rec']:
            process = input('PROCESS: ').lower().strip()
            flowchart.append(process)
            

        elif user_input in ['input','output','parelleogram','par']:
            input_output = input('INPUT/OUTPUT: ')
            flowchart.append(input_output)
            

        elif user_input in ['end']:
            print('(END)')
            break
        else:
            print('Retry')
    
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


#2 MARKs with more options
def two_marks_more_options(question): 
    #Enter Answer
    score = 0
    for questions in question:
        print(f'\n{divider}\n{questions[0]}\n')

        print("______________\nName two:")
        
        Enter_1 = input("1: ")

        if any(word in Enter_1 for word in questions[1]):
            score+=1
            print("\nCorrect\n")
        
        
        Enter_2 = input("2: ")
        

        if any(word in Enter_2 for word in questions[1]) and Enter_2 != Enter_1:
            score+=1
            print(f"{bold_divider}\nCorrect\n")
        elif Enter_1 == Enter_2 != '':
            print(f"{divider}\nThats two answer so only one mark!\n")
        else:
            print(f"{divider}\nIncorrect!!\n")
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
            print(f"{divider}\nIncorrect!\n")
            score=0
    
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
            print(f"{divider}\nIncorrect!!!\n")
            score=0
    
    return score
#/END OF FIRST SECTION\





#|THE SECOND SECTION - DISPLAYS AND USES THE FIRST SECTION FUNCTIONS TO CALCULATE THE MARKS AS WELL AS DISPLAY QUESTIONS AND SET THE MARK SCHEME PATTERNS|
#Paper 2 function
def paper_2_2024():
    #Question 1a
    question_1a_and_b = [('1a. State two methods of generating data. (2 marks)',
                   ['human generated','ai','machine learning','machine generated','sensors','sensor','iot','transactional data']),
                   ('1b. State two different types of malware. (2 marks)',
                    ['virus','ransomeware','trojan','worm','spyware','keylogger','adware','fileless malware','botnet'])]
    question_1a_and_1b_score = two_marks_more_options(question_1a_and_b)
    

    question_1c = [('1c. Explain one potential physical vulnerability to a digital system. (2 marks)',
                    ['location of system','cirumstances of use','end user skill level','system robustness','layout'],
                    ['allows easy access to system','cause unforeseen security breach','hardware failure'])]
    
    question_1c_score = two_marks(question_1c)

    #Question 2
    question_2 = [('2. Explain two ways that cloud-based technologies support collaboration. (4 marks)',
                   ['document sharing','documents are updated','sharing'],
                   ['allow multiple users to work together in drafting','communication tool'],
                   ['discuss business issues','file storage'],
                   ['centralised data storage','up to date version'])]

    question_2_score = four_marks_more_options(question_2,'1.','2.')

    #Question 3a
    print('\n3. An animation studio is upgrading the workstations used by animators.\n')
    
    question_3a = [('(a) Explain why the studio would choose liquid cooling for the new workstations. (3 marks)',
                   ['allows better cooling','than air cooled','lower temperature','processors','efficient heat dissipation'],
                   ['as powerful processors','load','processor would be heavier','reducing workload','processor fan'],
                   ['run required software','due to processing required','system quieter','reduces power usage'])]
    
    question_3a_score  =  three_marks(question_3a)

    #Question 3b
    print('An employee needs to use a design package that is incompatible with\nthe new workstations.\n')

    question_3b = [('3b. Describe how the studio could use this package on the new workstations (2 marks)',
                    ['virtualisation','virtual machine'],
                    ['emulate the required environment'])]
    
    question_3b_score = two_marks(question_3b)

    #Question 4
    question_4 = [('4. Explain why a company would want to keep its client list confidential. (3 marks)',
                   ["stop competitors from contacting company's clients","contacting company's clients",'contacting companys clients','contacting company clients','trust of clients','comply with legislation'],
                   ['tempt them with better offers','company reputation is preserved','avoiding legal consequences'],
                   ['avoid loss of profit','avoid loss of business','help with customer retention','result in fines'])]

    question_4_score = three_marks(question_4)

    #Question 5
    question_5 = [('5. Describe one potential technical threat to data when using open Wi-Fi networks. (3 marks)',
                   ['packet sniffer','mobile hotspot'],
                   ['man in the middle attack','intercept man in the middle attack','earsdrop man in the middle attack','perform man in the middle attack','spoof an official wi-fi network'],
                   ['data packet','the wifi router','spread malware','poison data packets','harvest data'])]

    question_5_score = three_marks(question_5)

    #Question 6a
    print("6. A company manufactures children's bicycles.\n")

    question_6a = [('(a) Explain two ways that digital systems can be used to support the company in the\nmarketing of a new bicycle. (4 marks)',
                    ['software to create adverts','online forms','engine optimisation'],
                    ['placed in cycling media','gather opinion','new products','draw attention to website'],
                    ['social media','analyse sale'],
                    ['target parents','more likely to buy the bicycle','drive advertising focus'])]

    question_6a_score = four_marks_more_options(question_6a,'1.','2.')

    #Question 6b
    print('6b. The company wishes to install a new Computer Aided Manufacturing machine.\n')
    question_6b = [('Explain one potential drawback of installing this machine. (3 marks)',
                    ['intial cost of machine','staff might not be familiar with the new machine','maintenance costs','less need for human labour'],
                    ['likely to be high','need training','could be high','redundancies'],
                    ['payback period is likely to be long','productive activities','expensive parts','external staff could be needed','impact staff morale','impact local community'])]

    question_6b_score = three_marks(question_6b)

    #Question 7
    print("7. A new digital system is being developed for a doctor's surgery\n")

    question_7 = [('Explain why it is important to consider cultural awareness and diversity when developing this system. (3 marks)',
                   ['users could be not native speakers','certain icons have an offensive connotation','cultures prefer clear and concise language'],
                   ['might not understand primary ui language ','some cultures','reflecting their direct style'],
                   [' language should be allowed','care should be taken when selecting icons','directness of language should be considered'])]

    question_7_score = three_marks(question_7)

    #Question 8
    question_8 = [('8. Evaluate the effectiveness of Data as a Service (DaaS) to organisations. (9 marks)',
                   [''],
                   [''],
                   [''])]

    question_8_score = nine_marks_evaluation(question_8)

    #Calculate section A
    section_A = (question_1a_and_1b_score + question_1c_score + question_2_score + question_3a_score + question_3b_score + question_4_score + question_5_score + question_6a_score + question_6b_score + question_7_score
                 + question_8_score)

    print(f'#########################################\nCongrats, you got Section A: {section_A}/40\n#########################################')
#/END OF SECOND SECTION\