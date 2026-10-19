#UPDATE SYNONYMS TO LIST APPROACH
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize
import string 

bold_divider ='___________'

divider = '-------------------'

def length_check(element):
    score = 0
    if len(element) >= 9:
        score-=1
    else:
        pass
    return score






def get_synonyms(words):
    synonyms = set()

    for word in words:  # Process only the words passed, not the entire `question`
        broken_sentence = sent_tokenize(word)
        broken_words = ' '.join(broken_sentence)
        print(broken_words)
        print(f"Processing word: {broken_words}")  # Debugging print
        for syn in wordnet.synsets(broken_words):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())


    return list(synonyms or broken_words)



def two(questions):
    score=0

    for question in questions:
        print(question[0])
        user_input = input(': ')
        
        length_checking_user_input = length_check(user_input)
        
        #Synonyms in lists of individual mark scheme
        marks_scheme_one_syn = get_synonyms(question[1])
        marks_scheme_two_syn = get_synonyms(question[2])

        
        answer1_match = any(word in user_input for word in marks_scheme_one_syn or question[1])
        answer2_match = any(word in user_input for word in marks_scheme_two_syn or question[2])
    
       

        score_count = sum([answer1_match, answer2_match])

    #3 marks
        if score_count == 3 and length_checking_user_input:
            print(f"{bold_divider}\nCorrect\n")
            score+=3
    #2 marks    
        elif score_count == 2 and length_checking_user_input:
            print(f"{divider}\nGood job, 2 marks\n")
            score+=2
    #1 mark
        elif score_count == 1 and length_checking_user_input:
            print(f"{divider}\nAlmost, you got 1 mark\n")
            score+=1
        else:
            print(f"{divider}\nIncorrect\n")
            score+=0
    return score

#word stop word
#stop word
#word word stop word word word
question = [('• a supported conclusion as to which algorithm the developer should choose. (12 marks)',
                     ['easy to understand','and develop','list of users','not need to be sorted before searched','efficient'],
                     ['very ineffecient','take a long time to complete','some users,','could be waiting a long time before their details were retrieved.','search increases greatly','o(n)',
                      'could hinder the growth of the number of users accessing the game.'])]



two(question)