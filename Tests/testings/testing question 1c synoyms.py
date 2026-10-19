from nltk.corpus import wordnet

divider = '---------------'
bold_divider = '_____________'



#BREAKING DOWN AND TURNING MARK SCHEME VOCAB INTO SYNONYMS
def get_synonyms(markscheme_vocab):
    synonyms = set()

    #Breaking down question mark scheme vocabulury 
    for word in markscheme_vocab:
        # Process synonyms while skipping None values
        if word is None:
            continue
        #Processing vocabulary
        for syn in wordnet.synsets(word):
            #Using lemma method storing vocabulary into specific synonyms
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())
    #Returning synonyms to be called upon
    return list(synonyms)


#ADDING SYNONYMS WITH SELECTED STOP WORDS
def adding_words_to_markscheme(question_stop_words, question_words=[None],add_individual_vocab=[None]):
    #Getting synonyms
    synonyms = get_synonyms(question_words)
    add_syn = get_synonyms(add_individual_vocab)
    #Establishing lists of joined answers
    adding_answers_list = []

    #Creating list of question
    
    for stop_words in question_stop_words:
        for question_vocab in synonyms:
            #Combination of mark scheme words such as stop words and synonym of vocabulary 
            combined = f"{stop_words} {question_vocab}".lower()
            combined2 = f"{question_vocab} {stop_words} {question_vocab}".lower()
            combined3 = f"{question_vocab} {stop_words}".lower()

            #Adding all combination to one list
            adding_answers_list.append(combined)
            adding_answers_list.append(combined2)
            adding_answers_list.append(combined3)
            for extra_vocab in add_individual_vocab:
            #Checking specific words
                if extra_vocab is None:
                    continue
                else:
                    pass
                extra_combined = f"{extra_vocab}".lower()
                adding_answers_list.append(extra_combined)


            
            
    # Clean up formatting of generated phrases
    upgraded_answer_list = [s.replace("_", " ") for s in adding_answers_list]
    print(upgraded_answer_list)
    #Return the upgraded mark scheme of combination
    return upgraded_answer_list


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

        print(upgraded_markscheme_var_one)
        print(upgraded_markscheme_var_two)
        print(upgraded_markscheme_var_three)

        answer1_match = any(word in user_input for word in upgraded_markscheme_var_one)
        answer2_match = any(word in user_input for word in upgraded_markscheme_var_two)
        answer3_match = any(word in user_input for word in upgraded_markscheme_var_three)
        print(answer1_match)
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

 #Question 1c and 1d: NEEDS MORE WORK SUCH AS NLTK
question_1c = [
    ("1c. Describe how accepted style conventions have been used to make the code in \nFigure 1 more readable. (3 Marks)",
     ['style', 'pep','conventions'],
     ['camelcase', 'snakecase', 'pascalcase','camel case','snake case','pascal case','spacing'],
     ['the of each variable', 'variable', 'code',' and','of word','function'])]

question_1c_vocabulary = ['sensible','naming','8','conventions']

question_1c_vocabulary_two = ['meaningful','identifiers']

question_1c_vocabulary_three = ['convey','purpose','clarify','structure','start','end']

question_1c_more_vocab_one = ['avoid', 'identifiers']

    #Outputing and intiating mark system
question_1c_1d_score = three_marks(question_1c, question_1c_vocabulary, question_1c_vocabulary_two, question_1c_vocabulary_three,[None],question_1c_more_vocab_one)