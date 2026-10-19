#This is PAPER ONE 2024 |DESIGN AND DIGITAL PRODUCTION|
#The first section displays functions that help mark the grade
#The second section displays all the questions and defines the mark schemes with the help of the first section

#Modules
import time
import nltk
from nltk.corpus import wordnet
import csv
import matplotlib.pyplot as plt
from nltk.corpus import stopwords


#Display Universal Splitter
divider =('-------------------------------')
bold_divider = ('_____________________________________')

#STORY: The teacher looks in the library and finds a dictionary containing a book of synonyms of work
#BREAKING DOWN AND TURNING MARK SCHEME VOCAB INTO SYNONYMS
def get_synonyms(markscheme_vocab):
    synonyms = set()

    # Breaking down mark scheme vocabulary
    for word in markscheme_vocab:
        if word is None:
            continue  # Skip None values

        # Extract synonyms using WordNet
        for syn in wordnet.synsets(word[0],pos=word[1]):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())

    return list(synonyms)  # Returning list of synonyms


# ADDING SYNONYMS WITH SELECTED STOP WORDS
def adding_words_to_markscheme(question_stop_words, question_words=[None], add_individual_vocab=[None],add_second_synonyms_vocab=[None]):
    synonyms = get_synonyms(question_words)  # Get synonyms
    add_syn = get_synonyms(add_second_synonyms_vocab)
    adding_answers_list = []  # Initialize answer list

    # Generating word combinations
    for stop_words in question_stop_words:
        for question_vocab in synonyms:
            combined1 = f"{stop_words} {question_vocab}".lower()
            combined2 = f"{question_vocab} {stop_words}".lower()
            combined3 = f"{stop_words} {question_vocab} {stop_words}".lower()
            adding_answers_list.extend([combined1, combined2, combined3])

        # Adding extra vocabulary directly
        for extra_vocab in add_individual_vocab:
            if extra_vocab:
                adding_answers_list.append(extra_vocab.lower())
            for extra in add_syn:
                if extra:
                    adding_answers_list.append(extra.lower())

    # Clean formatting
    upgraded_answer_list = [s.replace("_", " ") for s in adding_answers_list]
    
    #Removing duplicates based on the list being a dictionary and removing too much keys
    upgraded_answer_list = list(dict.fromkeys(upgraded_answer_list))

    return upgraded_answer_list  # Returning processed words




#|THE FIRST SECTION - THE FUNCTIONS THAT MARKS USERS INPUT|
#Story: The Students answers the questions in a paper and the teacher attempts to mark the students answer seeing if the marks fit the ammount of marks of each questions from 1 - 12 marks 
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
            print(f"{divider}\nGood job, 4 marks\n")
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
            print(f"{divider}\nGood job, 4 marks\n")
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
def two_marks(questions,vocab, vocab_two, add_individual_vocab=[None], two_add_individual_vocab=[None]):
   
    score=0
    for question in questions:
        print(question[0])

         #Adding words together
        upgraded_markscheme_var_one = adding_words_to_markscheme(question[1],vocab, add_individual_vocab)
        upgraded_markscheme_var_two = adding_words_to_markscheme(question[2],vocab_two, two_add_individual_vocab)

        user_input = input(f"{divider}\nEnter your answer: ").strip().lower()
        answer1_match = any(word in user_input for word in upgraded_markscheme_var_one)
        answer2_match = any(word in user_input for word in upgraded_markscheme_var_two)

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
def three_marks(questions,vocab, vocab_two, vocab_three, add_individual_vocab=[None], two_add_individual_vocab=[None], three_add_individual_vocab=[None]):
    score=0

    for question in questions:
        print(question[0])
        user_input = input(f"{divider}\nEnter your answer: ").strip().lower()
        
        #Adding words together
        upgraded_markscheme_var_one = adding_words_to_markscheme(question[1],vocab, add_individual_vocab)
        upgraded_markscheme_var_two = adding_words_to_markscheme(question[2],vocab_two, two_add_individual_vocab)
        upgraded_markscheme_var_three = adding_words_to_markscheme(question[3],vocab_three, three_add_individual_vocab)
        
        #Checking if at least one answer enter which if it isn't its false if it is then its true.
        answer1_match = any(word in user_input for word in upgraded_markscheme_var_one)
        answer2_match = any(word in user_input for word in upgraded_markscheme_var_two)
        answer3_match = any(word in user_input for word in upgraded_markscheme_var_three)

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
def four_marks(questions,vocab, vocab_two, vocab_three, vocab_four, add_individual_vocab=[None], two_add_individual_vocab=[None], three_add_individual_vocab=[None],four_add_individual_vocab=[None]):
    score=0

    for question in questions:
        print(question[0])
        user_input = input(f"{divider}\nEnter your answer: ").strip().lower()

        #Adding words together
        upgraded_markscheme_var_one = adding_words_to_markscheme(question[1],vocab, add_individual_vocab)
        upgraded_markscheme_var_two = adding_words_to_markscheme(question[2],vocab_two, two_add_individual_vocab)
        upgraded_markscheme_var_three = adding_words_to_markscheme(question[3],vocab_three, three_add_individual_vocab)
        upgraded_markscheme_var_four = adding_words_to_markscheme(question[4],vocab_four, four_add_individual_vocab)

        answer1_match = any(word in user_input for word in upgraded_markscheme_var_one)
        answer2_match = any(word in user_input for word in upgraded_markscheme_var_two)
        answer3_match = any(word in user_input for word in upgraded_markscheme_var_three)
        answer4_match = any(word in user_input for word in upgraded_markscheme_var_four)

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


#FOUR MARKS WITH MORE OPTIONS
def four_marks_more_options(questions, vocab=[None], vocab_two=[None], add_vocab_one=[None], add_vocab_two=[None], add_word_synonyms_vocab=[None],add_word_synonyms_vocab_two=[None], label=['1.', '2.']):
    score = 0  # Initial score set to 0
    previous_answer = None  # Previous answer tracking

    # Iterating questions
    for question in questions:
        print(question[0])  # Displaying question
        upgraded_answer_list_one = adding_words_to_markscheme(question[1], vocab, add_vocab_one, add_word_synonyms_vocab)
        upgraded_answer_list_two = adding_words_to_markscheme(question[2], vocab_two, add_vocab_two, add_word_synonyms_vocab_two)

        # Iterating user input
        for i in label:
            user_input = input(f'{divider}\n{i} ').lower().strip()

            # Checking if user input fits the expected answer set
            answer_match_1 = any(word in user_input for word in upgraded_answer_list_one)
            answer_match_2 = any(word in user_input for word in upgraded_answer_list_two)

            # Score calculation
            score_count = sum([answer_match_1, answer_match_2])

            if score_count == 2:
                print(f'{bold_divider}\nCorrect\n')
                score += 2
            elif score_count == 1:
                score += 1
            else:
                print(f'{divider}\nIncorrect\n')

            # Deducting points if the answer is repeated
            if previous_answer and all(word in previous_answer.split() for word in user_input.split()) and score_count > 0 and score_count != 2:
                print("That's the same answer, 1 point!")
                score=1
            if previous_answer and all(word in previous_answer.split() for word in user_input.split()) and score_count == 2:
                print("That's the same answer, 2 points!")
                score=2

            previous_answer = user_input  # Updating previous answer tracking

    print("{}\nThat's {} marks\n".format(divider, score))  # Printing final marks

    return score


#6 MARK question FUNCTION
def six_marks(questions,vocab, vocab_two, vocab_three, vocab_four, vocab_five,vocab_six,
              add_individual_vocab=[None], two_add_individual_vocab=[None], three_add_individual_vocab=[None],
              four_add_individual_vocab=[None], five_add_individual_vocab=[None],six_add_individual_vocab=[None]):
    score=0

    for question in questions:
        print(question[0])
        user_input = input(f"{divider}\nEnter your answer: ").strip().lower()

        #Adding words together
        upgraded_markscheme_var_one = adding_words_to_markscheme(question[1],vocab, add_individual_vocab)
        upgraded_markscheme_var_two = adding_words_to_markscheme(question[2],vocab_two, two_add_individual_vocab)
        upgraded_markscheme_var_three = adding_words_to_markscheme(question[3],vocab_three, three_add_individual_vocab)
        upgraded_markscheme_var_four = adding_words_to_markscheme(question[4],vocab_four, four_add_individual_vocab)
        upgraded_markscheme_var_five = adding_words_to_markscheme(question[5],vocab_five, five_add_individual_vocab)
        upgraded_markscheme_var_six = adding_words_to_markscheme(question[6],vocab_six, six_add_individual_vocab)


        answer1_match = any(word in user_input for word in upgraded_markscheme_var_one)
        answer2_match = any(word in user_input for word in upgraded_markscheme_var_two)
        answer3_match = any(word in user_input for word in upgraded_markscheme_var_three)
        answer4_match = any(word in user_input for word in upgraded_markscheme_var_four)
        answer5_match = any(word in user_input for word in upgraded_markscheme_var_five)
        answer6_match = any(word in user_input for word in upgraded_markscheme_var_six)

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
            print(f'{divider}\nAlmost, you got 3 marks\n')
            score+=3
        elif  FULL_SCORE == 4:
            print(f'\n{divider}Good, you got 4 marks\n')
            score+=4
        elif FULL_SCORE == 5:
            print(f'{divider}\nGood, you got 5 marks\n')
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
#Story: The student questions are checked thoroughly by the teachers using the books and mark scheme seeing the marks and creating a final score of marks.
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
            
    #Question 1c
    question_1c = [
    ("1c. Describe how accepted style conventions have been used to make the code in \nFigure 1 more readable. (3 Marks)",
     ['style', 'pep','conventions','in','a','to'],
     ['camelcase', 'snakecase', 'pascalcase','camel case','snake case','pascal case','identifiers','such as','spacing','the reader','the reader to more easily identify the start and end of words','end of words'],
     ['convey the purpose of each variable','purpose of each variable', 'variable', 'code','and','of','ensure'])]
    
    #Vocabulary that will have synonyms
    question_1c_vocabulary = [('sensible',wordnet.ADJ),('naming',wordnet.NOUN),('8',wordnet.ADJ),('conventions',wordnet.VERB),('nomenclature',wordnet.NOUN)]
    question_1c_vocabulary_two = [('meaningful',wordnet.ADJ),('identifiers',wordnet.NOUN),('reader',wordnet.NOUN)]
    question_1c_vocabulary_three = [('convey',wordnet.VERB),('purpose',wordnet.NOUN),('clarify',wordnet.VERB),('structure',wordnet.NOUN),('start',wordnet.NOUN),('end',wordnet.VERB),
                                    ('clearly',wordnet.ADV),('words',wordnet.VERB),('easily',wordnet.ADV)]
    question_1c_more_vocab_one = ['pep 8','pep8','classification style','label style']
    question_1c_more_vocab_two = ['camelcase', 'pascalcase','snakecase']
    question_1c_more_vocab_three = ['variable']

    #Outputing and intiating mark system
    question_1c_score = three_marks(question_1c, question_1c_vocabulary, question_1c_vocabulary_two, question_1c_vocabulary_three,
                                     question_1c_more_vocab_one,question_1c_more_vocab_two,question_1c_more_vocab_three)

    #Question 1c
    question_1d = [("1d. Explain why line 4 in Figure 1 is needed. (3 Marks)",
      ['is a string','string','Because the input'],
      ['into an','into an int','in','integer','int','must be','converted to an','to an'],
      ['in','runtime','error','used','avoid','to','in order to','be used','to be used in calculations','in calculations']
    )]
    
    #Vocabulary that will have synonyms
    question_1d_vocabulary = [('input',wordnet.VERB),('inputing',wordnet.VERB)]
    question_1d_vocabulary_two = [('converted',wordnet.VERB),('integer',wordnet.NOUN),('changed',wordnet.VERB)]
    question_1d_vocabulary_three = [('used',wordnet.VERB),('calculations',None),('calculate',wordnet.VERB),('avoid',wordnet.VERB),('errors',wordnet.NOUN),('mistakes',wordnet.NOUN)]
    question_1d_more_vocab_one = ['input is a string','string','input']
    question_1d_more_vocab_two = ['converted into an','converted into an integer']
    question_1d_score = three_marks(question_1d, question_1d_vocabulary, question_1d_vocabulary_two, question_1d_vocabulary_three,
                                    question_1d_more_vocab_one,question_1d_more_vocab_two)

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
    elif Enter_1 == Enter_2 != '' and Enter_1 == Enter_2 != ' ':
        print("Thats two answer so only one mark!")
    else:
        print("Incorrect!!")
    
    #question 3
    question_3 = [("\n3. Describe how company culture can be established. (3 Marks)", ['company values','values','company','of a','the','could be','can','has','is','are'],
    ['these','to','values','about values','values to employees','about','and clearly','existing','are','clearly communicate these values to existing employees','to existing employees','clearly communicate these values'],
    ['people that fit with these','employees','train employees to the culture', 'training','staff','are','employ people who','employ people who fit with these values','fit with these values','train existing employees in this culture','train','existing employees','employees in this culture'])]
    
    question_3_vocabulary = [('defining',wordnet.VERB),('define',wordnet.VERB,),('values',wordnet.NOUN),('companies',wordnet.NOUN),('business',wordnet.NOUN),('clarify',wordnet.VERB),
                             ('outline',wordnet.NOUN),('specify',wordnet.VERB),('explain',wordnet.VERB),('interpret',wordnet.VERB),('spell_out',wordnet.VERB),('beliefs',wordnet.NOUN)]

    question_3_vocabulary_two = [('communicate',wordnet.VERB),('speak',wordnet.VERB),('values',wordnet.NOUN),('employees',wordnet.NOUN),('talk',wordnet.VERB),('introduce',wordnet.VERB)]

    question_3_vocabulary_three = [('employees',wordnet.NOUN),('values',wordnet.NOUN),('train',wordnet.VERB),('staff',wordnet.NOUN),('principles',wordnet.NOUN),
                                   ('culture',wordnet.VERB),('employ',wordnet.VERB),('people',wordnet.NOUN),('training',wordnet.VERB)]

    question_3_score = three_marks(question_3, question_3_vocabulary, question_3_vocabulary_two, question_3_vocabulary_three)

    #Question 4
    print(f'4. An application is being written for a decorating company. Some Python code from\nthe application is shown in Figure 2.\nThe code does not work as intended.\n\nFigure 2\n{bold_divider}')
    print('1 Area = 0.0\n2')
    print('3 Length = input("Enter length of wall")')
    print('4 Height = input("Enter height of wall")\n5')
    print('6 if Area > 100.0:')
    print('7    print("This job will take more than one day")\n8')
    print('9 Area = float(Length) * float(Height)\n10\n')
    
    #Question 4a and 4b
    question_4a =[
        ('4a. Describe how a mathematical operator has been used in the code shown\nin Figure 2 (3 marks).',['operator','such as','the'],
         ['length and height','height','and','such as','the','as'],
         ['the area','area','the','as','is','int'])]
    
    question_4a_vocabulary = [('multiplication',wordnet.NOUN),('times',wordnet.VERB)]

    question_4a_vocabulary_two = [('length',wordnet.NOUN)]

    question_4a_vocabulary_three = [('calculate',wordnet.VERB)]
    
    #Question score
    question_4a_score = three_marks(question_4a,question_4a_vocabulary,question_4a_vocabulary_two,question_4a_vocabulary_three)

    question_4b = [('4b. Explain why the code written in Figure 2 will not work as intended. (3 marks)', 
         ['is','sequence','will always be','the','area','zero'],
         ['as the','the decision','area calculated after decision','is calculated after'],
         ['will take more than one day','so the','if the job','will never be true','never','say if the job will take more','one day'])]

    question_4b_vocabulary = [('wrong',wordnet.ADJ),('sequence',wordnet.NOUN),('area',wordnet.NOUN),('entering',wordnet.VERB),('decision',wordnet.NOUN),('zero',wordnet.NOUN)]

    question_4b_vocabulary_two = [('area',wordnet.NOUN),('calculated',wordnet.VERB),('after',wordnet.ADV),('because',None),('decision',wordnet.NOUN)]

    question_4b_vocabulary_three = [('program',wordnet.NOUN),('never',None),('state',wordnet.VERB),('condition',wordnet.NOUN),('true',wordnet.ADJ),('one',wordnet.NOUN),
                                    ('day',wordnet.NOUN),('more',wordnet.ADV),('more', wordnet.ADJ)]

    #Question score
    question_4b_score = three_marks(question_4b,question_4b_vocabulary,question_4b_vocabulary_two,question_4b_vocabulary_three)
    

    #Question 5
    print(f'5. An application is being written for a camp site. One function is shown in Figure 3.\n\nfigure 3\n{bold_divider}')
    print('1 def calc_cost(NumofNights, Month):')
    print('2    if Month > 4 and Month < 9:')
    print('3        NightlyCost = 30')
    print('4    else:')
    print('5        NightlyCost = 28')
    print('6    TotalCost = NumofNights * NightlyCost')
    print('7    return TotalCost\n')
    print('⚠️  DISCLAIMER: you CANNOT enter UNDERSCORE "_" because input does not expect it.\nIt is recommended to use a SPACE instead, for all answers when representation of functions.\n')

    #Question 5a
    question_5a = [('5a. Write a line of code that will store the total cost of a 6 night stay in month 12. (4 marks)',['by','a variable (e.g. cost_of_stay = )','a variable','of'],
                    ['correctly','function','of','passing','by','the','in','calling'],
                    ['numofnights','passing','by','the','in'],
                    ['month','passing','by','the','in'])]
    
    question_5a_vocabulary = [('declaring',wordnet.VERB),('cost',wordnet.NOUN),('stay',wordnet.VERB),('6',wordnet.NOUN),('12',wordnet.NOUN)]

    question_5a_vocabulary_two = [('calling',wordnet.VERB),('correctly',wordnet.ADV),('function',wordnet.NOUN)]

    question_5a_vocabulary_three = [('passing',wordnet.VERB),('parameter',wordnet.NOUN),('correctly',wordnet.ADV)]

    question_5a_vocabulary_four = [('passing',wordnet.VERB),('parameter',wordnet.NOUN),('correctly',wordnet.ADV)]

    question_5a_more_vocab_one = ['calc_cost(6,12)','calc_cost(6, 12)','calc_cost','costofstay=','costofstay =','cost']

    question_5a_score = four_marks(question_5a, question_5a_vocabulary, question_5a_vocabulary_two, question_5a_vocabulary_three, question_5a_vocabulary_four, question_5a_more_vocab_one)

    #Question 5b
    question_5b = [('5b. Describe how the developer has used relational operators in the code. (2 marks)',['than 4','four','than','that','is'],
                    ['correct price','allocate correct','to allocate','to','if','in','by','the'])]

    question_5b_vocabulary = [('4',wordnet.NOUN),('greater',wordnet.ADJ),('more',wordnet.ADV),('more', wordnet.ADJ)]
    
    question_5b_vocabulary_two = [('checking',wordnet.VERB),('correct',wordnet.ADJ),('price',wordnet.NOUN),('allocate',wordnet.VERB),('month',wordnet.NOUN),
                                  ('range',wordnet.NOUN),('assign',wordnet.VERB),('grant',wordnet.VERB)]

    question_5b_more_vocab_one = ['less than 9','less than nine']

    question_5b_more_vocab_two = ['checking if month in range']

    question_5b_score = two_marks(question_5b, question_5b_vocabulary, question_5b_vocabulary_two, question_5b_more_vocab_one, question_5b_more_vocab_two)

    #Question 6
    print('6. A program is needed that will calculate the difference between two whole\npositive numbers.\n')
    print('For example if the numbers 2 and 6 are entered then the difference is 4, if the\nnumbers 10 and 8 are entered the difference is 2.\n\nThe program must:\n\n')
    print('a. Allow the user to enter the first number\nb. Check that the number input is a whole positive number\nc. Allow the user to enter the second number\nd. Check that the number input is a whole positive number')
    print(f'e. Calculate the difference\nf. Output the difference\n\nDraw a flowchart that meets the rules of the program.\nUse the space provided on the next page (6 marks)\n{divider}\nTO END THE FLOWCHART, TYPE: "end"\n\nTO INTIATE FLOWCHART SHAPES, TYPE:')
    print("- DECISION SHAPES: 'decision', 'diamond','dia'\n- PROCESS SHAPES: 'process', 'rectangle','rec'\n- INPUT/OUTPUT SHAPES: 'input','output','parelleogram','par'\n")

    
    question_6 = [('\nDraw a flowchart that meets the rules of the program.\nUse the space provided on the next page (6 marks)',
                         ['number1','number2','number 1','number 2','enter number1','enter number2'],
                         ['number1>0','number2>0','number1>-1','number1>-1','number1 > 0','number2 > 0','number1 > -1','number2 > -1','number 1 > 0','number 2 > 0','number 2>0','number 1>0','0<number 1','0 < number 1','0<number 2','0 < number 2'],
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
    calculated_section_A_marks = question_4a_score + question_4b_score + question_3_score + question_1c_score + question_1d_score + question_1a_1b_score + question_5a_score + question_5b_score + question_6_score + question_7_score + marks 

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
                    ['decide on the needed output','needed output','identify necessary data','necessary data','filter out','filter out unnecessary detail','unnecessary detail','identify data needs','data needs'],
                    ['formulate','in the program','key actions in the','through deciding on the','inputs to the system','on what will vary'])]


    question_8b_vocab = [('decide',wordnet.VERB),('needed',wordnet.VERB),('output',wordnet.NOUN),('identify',wordnet.VERB),('necessary',wordnet.NOUN),('data',wordnet.NOUN),
                         ('filter',wordnet.VERB),('unnecessary',wordnet.ADJ),('detail',wordnet.NOUN),('system',wordnet.NOUN)]

    question_8b_vocab_two = [('formulate',wordnet.VERB),('key',wordnet.VERB),('actions',None),('program',wordnet.NOUN),('system',wordnet.NOUN),('inputs',wordnet.VERB),('deciding',wordnet.NOUN)]

    question_8b_score = four_marks_more_options(question_8b, vocab=question_8b_vocab, vocab_two=question_8b_vocab_two)

    #Question 8c
    question_8c = [('8c. Discuss the moral and ethical issues of using wearable technology to track user\nactivities through a fitness app. (6 marks)',
                    ['behaviour of individuals','to','of','the','these','that','such as locations and health data','such as locations','such as a','in','an','such as','have','some','push'],
                    ['can','to have increasing fitness scores','the','to have','an','in','that data gathered','by','could be','wearable devices could be misused if not','if not','could be extracted from the data','from the','inaccurate health indicators'],
                    ['can','cause users to push themselves', 'past safe activity levels','an','in','to','past safe activity levels','companies','health insurance','this could','this could raise privacy concerns','legal issues'],
                    ['their','to','can','in','endangering their health(safety in relation to running and cycling)','location data','and','data','to','is','an','the','unequal access to wearable technologies','access to'],
                    ['environmental','can','issues','environmental','used for','the','due to','due to cost or connectivity issues','or','to','an','is'],
                    ['can','could','due to consumption of','due to','potentially','sensitive information','in some','gaining an','when preparing for','advantage','unfair','the','an','be','can','in'])]

    question_8c_vocabulary = [('changes',wordnet.VERB),('behaviour',wordnet.NOUN),('individuals',wordnet.NOUN),('resources',wordnet.NOUN),('manufacture',wordnet.VERB),
                              ('devices',wordnet.NOUN),('work',wordnet.NOUN),('home',wordnet.NOUN),('locations',wordnet.NOUN),('gps',wordnet.NOUN),('health',wordnet.NOUN),
                              ('data',wordnet.NOUN),('encourage',wordnet.VERB),('more',wordnet.ADV),('more', wordnet.ADJ),('physical',wordnet.ADJ),('activity',wordnet.NOUN),
                              ('walking',wordnet.VERB),('cycling',wordnet.VERB)]

    question_8c_vocabulary_two = [('desire',wordnet.VERB),('increasing',wordnet.VERB),('fitness',wordnet.NOUN),('scores',wordnet.VERB),('fear',wordnet.NOUN),('data',wordnet.NOUN),
                                  ('gathered',wordnet.VERB),('wearable',wordnet.NOUN),('devices',wordnet.NOUN),('misused',wordnet.VERB),('adequately',wordnet.ADV),('protected',wordnet.ADJ),
                                  ('extracted',wordnet.VERB),('inaccurate',None),('health',wordnet.NOUN),('indicators',wordnet.NOUN),('protect',None)]

    question_8c_vocabulary_three = [('users',None),('cause',wordnet.NOUN),('push',wordnet.VERB),('themselves',None),('safe',wordnet.ADJ),('activity',wordnet.NOUN),('levels',wordnet.NOUN),
                                    ('example',wordnet.NOUN),('health',wordnet.NOUN),('insurance',wordnet.NOUN),('companies',wordnet.NOUN),('raise',wordnet.VERB),('privacy',wordnet.NOUN),
                                    ('concerns',wordnet.NOUN),('concerns',wordnet.VERB),('legal',None),('issues',wordnet.NOUN)]

    question_8c_vocabulary_four = [('endangering',wordnet.VERB),('health',wordnet.NOUN),('safety',wordnet.NOUN),('relation',wordnet.NOUN),('running',wordnet.VERB),('cycling',wordnet.VERB),
                                   ('location',wordnet.NOUN),('unequal',wordnet.ADJ),('access',wordnet.VERB),('wearable',wordnet.NOUN),('technologies',wordnet.NOUN)]

    question_8c_vocabulary_five = [('environmental',None),('issues',wordnet.NOUN),('targeted',wordnet.VERB),('marketing',wordnet.NOUN),('cost',wordnet.NOUN),('connectivity',None)]

    question_8c_vocabulary_six = [('consumption',wordnet.NOUN),('energy',wordnet.NOUN),('sensitive',wordnet.ADJ),('information',wordnet.NOUN),('potentially',None),('result',wordnet.NOUN),
                                  ('people',wordnet.NOUN),('gaining',wordnet.VERB),('unfair',wordnet.ADJ),('advantage',wordnet.NOUN),('events',wordnet.NOUN)]

    question_8c_score = six_marks(question_8c,question_8c_vocabulary, question_8c_vocabulary_two, question_8c_vocabulary_three, 
                                  question_8c_vocabulary_four, question_8c_vocabulary_five, question_8c_vocabulary_six)

    #question 9a
    print('9. A company is developing new software to train student nurses.')

    question_9a = [('(a) Explain two ways that an acceptable use policy will govern staff conduct when\ndeveloping the software. (4 marks)',
                    ['list permitted','list prohibited','activities','activity','prohibited','permitted','list','working practice','rules','etiquette rules'],
                    ['could','can','for not','for not adhering to these rules','to these rules','avoid confusion to new employees','to new employees','aid data security','data security','aid','internal and external','and','communication'])]

    question_9a_vocab = [('list',None),('prohibited',None),('activities',wordnet.NOUN),('permitted',wordnet.VERB),('stipulate',wordnet.VERB),('etiquette',None),('rules',wordnet.NOUN)]

    question_9a_vocab_two = [('penalties',wordnet.NOUN),('adhering',wordnet.VERB),('rules',wordnet.NOUN),('avoid',wordnet.VERB),('confusion',wordnet.NOUN),
                             ('employees',wordnet.NOUN),('aid', wordnet.VERB),('data',wordnet.NOUN),('security',wordnet.NOUN),('internal',wordnet.ADJ),('external',wordnet.ADJ),('communication',wordnet.NOUN)]

    question_9a_score = four_marks_more_options(question_9a, vocab=question_9a_vocab, vocab_two=question_9a_vocab_two)

    #question 9b
    question_9b = [('9b. Explain two ways that a developer may express an algorithm. (4 marks)',
                    ['written','annotated'],
                    ['express concepts using diagrams','which express concepts','which uses coding concepts','which uses','explained as a','explained as a narrative','uses existing code','uses existing'])]

    question_9b_vocab_two = [('express',wordnet.VERB),('concepts',wordnet.NOUN),('diagrams',wordnet.VERB),('coding',wordnet.NOUN),('explained',wordnet.VERB),('narrative',wordnet.NOUN),
                             ('existing',wordnet.VERB),('code',wordnet.NOUN)]

    first_mark_question_9b_vocab = [('flowchart',wordnet.NOUN),('pseudocode',None),('written',wordnet.ADJ), ('description',wordnet.NOUN),('annotated',wordnet.VERB), ('code',wordnet.NOUN)]

    first_add_vocab_question_9b = ['flowchart','pseudocode','written', 'description','annotated', 'code']
    
    question_9b_score = four_marks_more_options(question_9b, vocab_two=question_9b_vocab_two,add_vocab_one=first_add_vocab_question_9b,
                                                 add_word_synonyms_vocab=first_mark_question_9b_vocab)

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
                     ['string','real','float'],
                     ['username','username could','could','more than one character','more than','could add','containing pounds and pence','add values containing','to be added to existing','to be added to','to','the'])]

    question_10a_vocab_words = [('convey',wordnet.VERB),('such',None),('thing',None)]

    question_10a_vocab_words_two = [('more',wordnet.ADV),('more', wordnet.ADJ),('character',wordnet.NOUN),('mixture',wordnet.NOUN),('one',wordnet.NOUN),('user',None),('add',wordnet.VERB),
                                    ('values',wordnet.NOUN),('pounds',wordnet.NOUN),('pence',wordnet.NOUN),('decimal',None),('number',wordnet.VERB),('credit',wordnet.NOUN),
                                    ('added',wordnet.VERB),('existing',wordnet.VERB),('contain',wordnet.VERB)]

    first_mark_question_10a = ['string','real','float']

    question_10a_score = four_marks_more_options(question_10a,label=['Username:','Credit_Added:'],vocab=question_10a_vocab_words, add_vocab_one=first_mark_question_10a,
                                                  vocab_two=question_10a_vocab_words_two)

    #question 10b
    print('The user must also enter their mobile phone number.\n\nOne suitable validation technique to check the data entered would be a\npresence check.\n')

    question_10b = [('10b. Describe two other suitable validation techniques that could be used for\nthis data. (4 marks)',
                     ['length check','check'],
                     ['acceptable number of characters','of','acceptable number of','invalid characters are entered','characters are entered','check string starts with 0 or +','or','check string starts with'])]

    question_10b_vocab = [('format',wordnet.NOUN)]

    question_10a_vocab_two = [('acceptable',wordnet.ADJ),('number',wordnet.VERB),('characters',wordnet.NOUN),('invalid',wordnet.VERB),('entered',wordnet.VERB),('no',wordnet.ADV),
                              ('check',wordnet.VERB),('starts',wordnet.VERB),('plus',wordnet.NOUN),('0',wordnet.NOUN)]

    first_mark_question_10b = ['length check','format check']

    question_10b_score = four_marks_more_options(question_10b, vocab=question_10b_vocab, vocab_two=question_10a_vocab_two ,add_vocab_one=first_mark_question_10b)

    #question 10c
    question_10c = [('10c. Describe how the developer would prepare automated test tools when unit\ntesting this module. (3 marks)',
                     ['is created','test file'],
                     ['test data','inserting'],
                     ['expected','results'])]
    
    question_10c_vocabulary = [('test',wordnet.VERB),('file',wordnet.NOUN),('created',wordnet.VERB)]

    question_10c_vocabulary_two = [('inserting',wordnet.VERB),('data',wordnet.NOUN),('test',wordnet.VERB)]

    question_10c_vocabulary_three = [('expected',wordnet.VERB),('results',None)]

    question_10c_score = three_marks(question_10c, question_10c_vocabulary, question_10c_vocabulary_two,question_10c_vocabulary_three)

    #question 10d
    print('Personal information about users will be held in this system.\n')

    question_10d = [('10d. Explain two ways that the company can ensure that it meets the requirements of\ndata protection laws. (4 marks)',
                     ['adequate security measures','adequate','data protection officer','such as','the','could','data controller','controller','audit data stored','audit','data stored','train employees','train'],
                     ['encryption','firewalls','monitor compliance with laws','with','with laws','monitor compliance with','only essential','only essential data is kept','data is kept','correct working practices','correct working practices are adhered to','are adhered to'])]


    question_10d_vocab = [('adequate',wordnet.ADJ),('security_measures',wordnet.NOUN),('data',wordnet.NOUN),('protection',wordnet.NOUN),('officer',wordnet.NOUN),
                          ('controller',wordnet.NOUN),('audit',wordnet.VERB),('stored',wordnet.VERB),('train',wordnet.VERB),('employees',wordnet.NOUN)]

    question_10d_vocab_two = [('encryption',wordnet.NOUN),('firewalls',None),('monitor',wordnet.NOUN),('compliance',wordnet.NOUN),('laws',wordnet.NOUN),('only',wordnet.ADJ),
                              ('essential',wordnet.ADJ),('data',wordnet.NOUN),('kept',wordnet.VERB),('correct',wordnet.ADJ),('working',wordnet.ADJ),('practices',wordnet.VERB),
                              ('adhered',wordnet.VERB)]

    question_10d_score = four_marks_more_options(question_10d, vocab=question_10d_vocab, vocab_two=question_10d_vocab_two)

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

    #Story: The teacher finds the final score and displays it
    #Calculates the full marks (Section A Marks + Section B Marks)
    PAPER_ONE_MARKS = calculated_section_A_marks + calcualated_section_B_marks
    #Display's full marks
    print(f'\nYour marks: {PAPER_ONE_MARKS}/100')
#/END OF SECOND SECTION\