import nltk
from nltk.corpus import wordnet

divider = '____'

bold_divider = '_-----'

# Function to generate synonyms for a given word
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().lower())
    return list(synonyms)

# Expand question keywords with their synonyms
def expand_keywords(words):
    expanded_words = set(words)  # Start with original words
    for word in words:
        expanded_words.update(get_synonyms(word))  # Add synonyms
    return list(expanded_words)

def twelve_marker_evaluation_variation_one(questions):
    score = 0
    for question in questions:
        print(question[0])
        user_input = input(f"{divider}\nEnter your answer: ").strip().lower()

        # Expand each keyword list with synonyms
        benefits = expand_keywords(question[1])
        benefits2 = expand_keywords(question[2])
        drawbacks = expand_keywords(question[3])
        drawbacks2 = expand_keywords(question[4])
        conclusion = expand_keywords(question[5])

        # Check input against keywords (including synonyms)
        score_count = sum([
            any(word in user_input for word in benefits),
            any(word in user_input for word in benefits2),
            any(word in user_input for word in drawbacks),
            any(word in user_input for word in drawbacks2),
            any(word in user_input for word in conclusion)
        ])

        full_marks = sum([
            all(word in user_input for word in benefits),
            all(word in user_input for word in benefits2),
            all(word in user_input for word in drawbacks),
            all(word in user_input for word in drawbacks2),
            all(word in user_input for word in conclusion)
        ])

        FULL_SCORE = score_count + full_marks

        # Score evaluation logic
        if FULL_SCORE == 1:
            print(f'{divider}\nUnfortunately, this is one mark!!\n')
            score += 1
        elif FULL_SCORE == 2:
            print(f'{divider}\nAlmost, you got 2 marks\n')
            score += 2
        elif FULL_SCORE == 3:
            print(f'\n{divider}Almost, you got 3 marks\n')
            score += 3
        elif FULL_SCORE == 4:
            print(f'\n{divider}Good, you got 4 marks\n')
            score += 4
        elif FULL_SCORE == 5:
            print(f'\n{divider}Good, you got 5 marks\n')
            score += 5
        elif FULL_SCORE == 6:
            print(f'{divider}\nGood, 8 marks.\n')
            score += 8
        elif FULL_SCORE == 7:
            print(f'{divider}\nGreat, 9 marks\n')
            score += 9
        elif FULL_SCORE == 8:
            print(f'{divider}\nGreat, 10 marks\n')
            score += 10
        elif FULL_SCORE == 9:
            print(f'{divider}\nExcellent, 11 marks\n')
            score += 11
        elif FULL_SCORE == 10:
            print(f'{bold_divider}\nCorrect, Full marks\n')
            score += 12
        else:
            score = 0
            print(f'\nIncorrect!!!\n')
    return score


question = [('• a supported conclusion as to which algorithm the developer should choose. (12 marks)',
                     ['easy to understand','and develop','list of users','not need to be sorted before searched'],
                     ['very ineffecient','take a long time to complete','some users','could be waiting a long time before their details were retrieved','search increases greatly','o(n),',
                      'could hinder the growth of the number of users accessing the game'],
                     ['efficient','users would be able to access the game with little delay','search time does not grow rapidly','o(log^2n)'],
                     ['more complex algorithm to understand and develop','data must be in order for the algorithm to work'],
                     ['efficent','complexity','should choose binary search if the list is sorted','if unsorted','choose linear search','linear search offers flexibility','linear time complexity'])]


twelve_marker_evaluation_variation_one(question)