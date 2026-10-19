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
divider =('--------------------------------------------------------------')
bold_divider = ('_________________________________________________________')


#STORY: The teacher looks in the library and finds a dictionary containing a book of synonyms of work
#BREAKING DOWN AND TURNING MARK SCHEME VOCAB INTO SYNONYMS
def get_synonyms(markscheme_vocab):
    synonyms = set()

    # Breaking down mark scheme vocabulary
    for word in markscheme_vocab:
        if word is None:
            continue  # Skip None values

        # Extract synonyms using WordNet
        for syn in wordnet.synsets(word):
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
    
    return upgraded_answer_list  # Returning processed words


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
        elif Enter_1 == Enter_2 != '' and Enter_1 == Enter_2 != ' ':
            print(f"{divider}\nThats two answer so only one mark!\n")
        else:
            print(f"{divider}\nIncorrect!!\n")
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
                   ['document sharing','sharing','document','communication tools','communication','tools','file storage','storage','file','most up to date version is accessed','up to date version','is accessed'],
                   ['to work together','multiple users to work together in drafting','multiple users','business issues','issues','discuss business','discuss business issues','allow','allow centralised data storage','data storage'
                    ,'are','real time','documents are updated','documents are updated in real time'])]

    question_2_vocab = ['document','sharing','communication','tools','file','storage','recent','to_date','accessed','most','new']

    question_2_vocab_two = ['multiple','users','work','drafting','together','discuss','business','issues','centralised','data','storage','documents','updated']

    question_2_score = four_marks_more_options(question_2, vocab=question_2_vocab, vocab_two=question_2_vocab_two)

    #Question 3a
    print('\n3. An animation studio is upgrading the workstations used by animators.\n')
    
    question_3a = [('(a) Explain why the studio would choose liquid cooling for the new workstations. (3 marks)',
                   ['liquid cooling reduces','allows for better','allows better','then','than air cooled','lower temperature','processors','dissipation','efficient heat dissipation','at a lower','keeps','within accepted','Provides efficient','Provides efficient heat'],
                   ['as powerful','load','would be heavier','reducing workload','processor fan','as the load on the','reducing the workload of','fan'],
                   ['which','run required','run required software','due to','due to processing required','system quieter','reduces power usage','which makes the','reduces power','by animation software','would be needed to','due to the','would be needed to run required','required'])]
    
    question_3a_vocab = ['power','allows','better','cooling','air','cooled','lower','temperature','processors','efficient','heat','dissipation']

    question_3a_vocab_two = ['processors','powerful','load','heavier','reducing','workload','fan']

    question_3a_vocab_three = ['run','required','software','processing','system','quieter','reduces','power','usage','animation','software','run']

    question_3a_score  =  three_marks(question_3a, question_3a_vocab, question_3a_vocab_two, question_3a_vocab_three)

    #Question 3b
    print('An employee needs to use a design package that is incompatible with\nthe new workstations.\n')

    question_3b = [('3b. Describe how the studio could use this package on the new workstations (2 marks)',
                    ['virtualisation','virtual machine'],
                    ['emulate the required environment'])]
    
    question_3b_score = two_marks(question_3b)

    #Question 4
    question_4 = [('4. Explain why a company would want to keep its client list confidential. (3 marks)',
                   ['to stop','with','to comply with','maintain trust of','contacting','contacting company','to stop competitors from','comply with'],
                   ['avoiding','is preserved','ensure company reputation','ensure','better','to tempt them with','tempt them with better offers','company reputation is preserved','legal consequences'],
                   ['result in','which could','retention','with','to help with','avoid loss','to avoid loss','profit','business','avoid loss of','help with customer'])]

    question_4_vocab = ['stop','competitors','contacting','company','clients','trust','comply','legislation']

    question_4_vocab_two = ['tempt','offers','offers','company','reputation','preserved','legal','consequences','avoiding']

    question_4_vocab_three = ['avoid','loss','profit','business','help','customer','retention','result','fines']

    question_4_score = three_marks(question_4, question_4_vocab, question_4_vocab_two, question_4_vocab_three)

    #Question 5
    question_5 = [('5. Describe one potential technical threat to data when using open Wi-Fi networks. (3 marks)',
                   ['packet','hotspot','Use a packet','use a mobile'],
                   ['to imitate','in the middle','in the middle attack','man in the middle','spoof an official','an official','to intercept'],
                   ['router','from the wifi','data packet','the wifi router','malware','spread malware','poison','being sent to','to harvest'])]

    question_5_vocab = ['sniffer','mobile','hotspot']

    question_5_vocab_two = ['man','middle','attack','intercept','earsdrop','perform','spoof','official','network','wifi','imitate']

    question_5_vocab_three = ['data','packet','router','wifi','poison','spread','harvest','sent']

    question_5_score = three_marks(question_5, question_5_vocab, question_5_vocab_two, question_5_vocab_three)

    #Question 6a
    print("6. A company manufactures children's bicycles.\n")

    question_6a = [('(a) Explain two ways that digital systems can be used to support the company in the\nmarketing of a new bicycle. (4 marks)',
                    ['to create adverts','software to create adverts','to','social media','online forms','online','forms','analyse sales','search engine','search engine optimisation'],
                    ['could be','in cycling media','target parents that are more likely to buy the bicycle','gather','gather opinion','of new products','drive advertising focus','to','draw attention','draw attention to website'])]

    question_6a_vocab  = ['software','create','adverts','media','online','forms','analyse','sales','search','engine','optimisation','basically']

    question_6a_vocab_two = ['basically','placed','cycling','media','target','parents','likely','buy','bicycle','opinion','products','new','drive','advertising','focus','attention','website','gather']

    question_6a_score = four_marks_more_options(question_6a, vocab=question_6a_vocab, vocab_two=question_6a_vocab_two)

    #Question 6b
    print('6b. The company wishes to install a new Computer Aided Manufacturing machine.\n')
    question_6b = [('Explain one potential drawback of installing this machine. (3 marks)',
                    ['ensure','might not be','might not be familiar','cost of','intial cost of','with the new','maintenance cost','less need for human labour','less need for','cost','less need for human'],
                    ['would need','could be','ensure','likely to be','to','leading to'],
                    ['therefore the','is likely to be','activity','part','could be needed','morale','community','needed','could','is'])]


    question_6b_vocab = ['intial','cost','machine','staff','new','maintenance','less','human','labour','familiar']

    question_6b_vocab_two = ['likely','high','training','redundancies']

    question_6b_vocab_three = ['long','payback','period','productive','activities','expensive','parts','external','staff','impact','morale','local','community','unplanned','planned']

    question_6b_score = three_marks(question_6b, question_6b_vocab, question_6b_vocab_two, question_6b_vocab_three)

    #Question 7
    print("7. A new digital system is being developed for a doctor's surgery\n")

    question_7 = [('Explain why it is important to consider cultural awareness and diversity when developing this system. (3 marks)',
                   ['not','could be not','have an','have an offensive','prefer','could'],
                   ['might not', 'ui ','some','their direct'],
                   ['should be taken when','should be allowed','so choice of','should be','should be allowed','should be taken when','of language should be'])]

    question_7_vocab = ['users','native','speakers','certain','icons','offensive','connotation','cultures','clear concise','language']

    question_7_vocab_two = ['understand','primary','language','cultures','reflecting','style']

    question_7_vocab_three = ['language','care','icons','selecting','directness','considered','select']

    question_7_score = three_marks(question_7, question_7_vocab, question_7_vocab_two, question_7_vocab_three)

    #Question 8
    question_8 = [('8. Evaluate the effectiveness of Data as a Service (DaaS) to organisations. (9 marks)',
                   ['None'],
                   ['None'],
                   ['None'])]

    question_8_score = nine_marks_evaluation(question_8)

    #Calculate section A
    section_A = (question_1a_and_1b_score + question_1c_score + question_2_score + question_3a_score + question_3b_score + question_4_score + question_5_score + question_6a_score + question_6b_score + question_7_score
                 + question_8_score)

    print(f'#########################################\nCongrats, you got Section A: {section_A}/40\n#########################################')
#/END OF SECOND SECTION\