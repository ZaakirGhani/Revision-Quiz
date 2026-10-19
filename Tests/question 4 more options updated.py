from nltk.corpus import wordnet
from nltk.corpus import stopwords


divider = '================================================='
bold_divider = '___________'

# BREAKING DOWN AND TURNING MARK SCHEME VOCAB INTO SYNONYMS
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
            adding_answers_list.extend([combined1, combined2])

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

    print("Generated mark scheme vocabulary:", upgraded_answer_list)  # Debugging output
    
    return upgraded_answer_list  # Returning processed words


# FOUR MARKS WITH MORE OPTIONS FUNCTION
def four_marks_more_options(questions, vocab=[None], vocab_two=[None], add_vocab_one=[None], add_vocab_two=[None], add_word_synonyms_vocab=[None],add_word_synonyms_vocab_two=[None], label=['1.', '2.']):
    score = 0  # Initial score set to 0
    previous_answer = None  # Previous answer tracking

    # Iterating questions
    for question in questions:
        print(question[0])  # Displaying question
        upgraded_answer_list_one = adding_words_to_markscheme(question[1], vocab, add_vocab_one, add_word_synonyms_vocab)
        upgraded_answer_list_two = adding_words_to_markscheme(question[2], vocab_two, add_vocab_two, add_word_synonyms_vocab_two)

        print("Accepted answers:", upgraded_answer_list_one)  # Debug print

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
                print("That's the same answer, so only one 1 point only!")
                score = 1
            if previous_answer and all(word in previous_answer.split() for word in user_input.split()) and score_count == 2:
                print("That's the same answer, 2 points only!")
                score = 2

            previous_answer = user_input  # Updating previous answer tracking

    print("{}\nThat's {} marks".format(divider, score))  # Printing final marks

    return score


#question 9b
question_9b = [('9b. Explain two ways that a developer may express an algorithm. (4 marks)',
                ['written','annotated'],
                ['as','express concepts using','express concepts using','which uses coding concepts','which uses','explained as a','explained as a narrative','uses existing code','uses existing','of language should be considered'])]

question_9b_vocab_tw = ['express','diagrams','coding','concepts','explained','narrative','existing','code','terror loves','productive activities','expensive parts','payback period','language']

question_9b_vocab_two = [('language',wordnet.NOUN),('expensive',wordnet.ADJ),('activities',wordnet.NOUN),('code',wordnet.NOUN),('explained',None),
                         ('diagrams',None),('express',wordnet.VERB),('concepts',wordnet.NOUN),('coding',wordnet.NOUN),('programming',None),('code',wordnet.NOUN),
                         ('existing',wordnet.NOUN),('expensive',wordnet.NOUN),('parts',wordnet.NOUN),('narrative',wordnet.NOUN),('walking',wordnet.VERB)]

first_mark_question_9b_vocab = [('flowchart',wordnet.NOUN),('pseudocode',None), ('document',wordnet.NOUN),('written',wordnet.NOUN), (
    'description',wordnet.NOUN),('annotated',wordnet.VERB),('code',wordnet.NOUN)]

question_9b_score = four_marks_more_options(question_9b, vocab_two=question_9b_vocab_two,add_word_synonyms_vocab=first_mark_question_9b_vocab)