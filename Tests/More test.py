from nltk.corpus import wordnet
divider = '____-'
bold_divider = '_------'
#Take list of words that will be broken down
def broken_list():
    question1 = [(['easy','understand','develop','list','users','sorted','searched','ineffecient'])]
    return question1

#Break the synonyms into their words
def synon():
    question1 = broken_list()
    synonyms = set()
    for phrases in question1:
        for words in phrases:
            print(words)
            for syn in wordnet.synsets(words):
                for lemma in syn.lemmas():
                    synonyms.add(lemma.name())
    return synonyms

def two(questions):
    synonyms = synon()

    score=0

    for question in questions:
        print(question[0])
        user_input = input(f"\nEnter your answer: ").strip().lower()
        #Check the word of the input check if atleast one word from the synonyms fit
        matched_words = [word for word in synonyms if word in user_input]
        matched = ' '.join(matched_words)
        question2 = list(question[1])
        question2.append(matched)
        print(question2)
        question_again = list(question[2])
        question_again.append(matched)
        answer1_match = any(word in user_input for word in question2)
        answer2_match = any(word in user_input for word in question_again)
    

        score_count = sum([answer1_match, answer2_match])

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



questions = [('mike',['mike','ds'],['io'])]

score = two(questions)
