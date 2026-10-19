from nltk.corpus import wordnet
divider = ('________________________')
bold_divider =('-----')

#Take list of words that will be broken down
def broken_list():
    question1 = [(['easy','understand','develop','list','users','sorted','searched','ineffecient'])]
    return question1


#Break the synonyms into their words
def synon(matched_case):
    question1 = broken_list()
    synonyms = set()
    for phrases in question1:
        for words in phrases:
            print(words)
            for syn in wordnet.synsets(words):
                for lemma in syn.lemmas():
                    synonyms.add(lemma.name())
    return synonyms

#3 MARK question FUNCTION
def three_marks(questions, user_input):
    score=0

    for question in questions:
        print(question[0])
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


user_input = input(f"{divider}\nEnter your answer: ").strip().lower()
synonyms=synon()
matched_words = [word for word in synonyms if word in user_input] 

questions = [('mike',['mike'] + matched_words,'mi',['io'])]

twos_quest_score = three_marks(questions, user_input)

print(twos_quest_score)

   
