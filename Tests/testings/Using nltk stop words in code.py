#Using nltk stop words in code
from nltk.corpus import stopwords, wordnet
import random
from itertools import product

def stop_words():
    #Stop words being establish by the stop words key words
    stopword = stopwords.words('english')
    
    return list(stopword)

def filtering():
    stopword_list = stop_words()

    stopword_list.append('a')
    stopword_list.append('i')
    #newlist = [x for x in fruits if x != "apple"]

    #Remove words list
    remove_words = ['a','q','w','e','r','t','y','u','o','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','i']
    #Removing alphabetic letters except for words
    filtered = [s for s in stopword_list if s not in remove_words]
    return filtered

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
def adding_words_to_markscheme(question_static_words, question_words=[None], add_individual_vocab=[None],add_second_synonyms_vocab=[None]):
    synonyms = get_synonyms(question_words)  # Get synonyms
    add_syn = get_synonyms(add_second_synonyms_vocab)
    adding_answers_list = []  # Initialize answer list

    filtered_stop_words = filtering()

    second_stop_words = filtered_stop_words.copy()

    third_stop_words = filtered_stop_words.copy()

    random.shuffle(second_stop_words)
    random.shuffle(third_stop_words)

    ports = 1870

    # Generating word combinations
    if ports == 1080:
        for combination_var_1 in product(question_static_words, synonyms):
            #Question 1c, 4a
            #[Gerund] [Noun]
            combo = ' '.join(list(combination_var_1)).lower()
            adding_answers_list.extend([combo])
    elif ports == 1280:
        #Question 3
        for combination_var_2 in product(synonyms, add_syn, question_static_words):
            combo_1 = ' '.join(list(combination_var_2)).lower()
            adding_answers_list.extend([combo_1])
    elif ports == 1480:
        #question 4a
        for combination_var_3 in product(synonyms, filtered_stop_words, question_static_words):
            combo_2 = ' '.join(list(combination_var_3)).lower()
            adding_answers_list.extend([combo_2])
    elif ports == 1680:
        #Question 4a, 4b
        for combination_var_4 in product(synonyms, filtered_stop_words, question_static_words):
            combo_3 = ' '.join(list(combination_var_4)).lower()
            adding_answers_list.extend([combo_3])
    elif ports == 1860:
        #Question 4b
        for combination_var_5 in product(question_static_words, filtered_stop_words, synonyms, second_stop_words, add_syn):
            combo_4 = ' '.join(list(combination_var_5)).lower()
            adding_answers_list.extend([combo_4])
    elif ports == 1870:
        #Question 4b
        for combination_var_6 in product(synonyms, filtered_stop_words, add_syn, second_stop_words, synonyms ,question_static_words):
            combo_5 = ' '.join(list(combination_var_6)).lower()
            adding_answers_list.extend([combo_5])
    elif ports == 1880:
        #Question 3
        for combination_var_7 in product(synonyms, filtered_stop_words, add_syn, second_stop_words, question_static_words):
            combo_6 = ' '.join(list(combination_var_7)).lower()
            adding_answers_list.extend([combo_6])
    elif ports == 2080:
        #Question 1c
        for combination_var_8 in product(synonyms, filtered_stop_words, add_syn, question_static_words):
            combo_7 = ' '.join(list(combination_var_8)).lower()
            adding_answers_list.extend([combo_7])

        for combination_var_9 in product(synonyms, filtered_stop_words, add_syn, second_stop_words, question_static_words):
            combo_8 = ' '.join(list(combination_var_9)).lower()
            adding_answers_list.extend([combo_8])
    elif ports == 2280:
        #Default
        for combination_var_10 in product(synonyms, question_static_words):
            combo_9 = ' '.join(list(combination_var_10)).lower()
            adding_answers_list.extend([combo_9])

        for combination_var_11 in product(question_static_words, synonyms):
            combo_10 = ' '.join(list(combination_var_11)).lower()
            adding_answers_list.extend([combo_10])
    elif ports == 2480:
        #Question 1d
        for combination_var_12 in product(synonyms, filtered_stop_words, add_syn):
            combo_11 = ' '.join(list(combination_var_12)).lower()
            adding_answers_list.extend([combo_11])

        for combination_var_13 in product(synonyms, filtered_stop_words, second_stop_words, add_syn):
            combo_12 = ' '.join(list(combination_var_13)).lower()
            adding_answers_list.extend([combo_12])
    elif ports == 2680:
        #Question 4b
        for combination_var_14 in product(synonyms, filtered_stop_words, question_static_words, second_stop_words, add_syn):
            combo_13 = ' '.join(list(combination_var_14)).lower()
            adding_answers_list.extend([combo_13])

    #Adding extra vocabulary directly    
    if add_individual_vocab:
        if ports == 1280:
            for combination_extra_var_1 in product(add_syn, filtered_stop_words, add_syn, second_stop_words, add_individual_vocab):
                combo_extra = ' '.join(list(combination_extra_var_1)).lower()
                adding_answers_list.extend([combo_extra])
        elif ports == 1340:
            for combination_extra_var_2 in product(synonyms, filtered_stop_words, add_individual_vocab):
                combo_extra_1 = ' '.join(list(combination_extra_var_2)).lower()
                adding_answers_list.extend([combo_extra_1])

            for combination_extra_var_3 in product(synonyms, filtered_stop_words, second_stop_words, add_individual_vocab):
                combo_extra_2 = ' '.join(list(combination_extra_var_3)).lower()
                adding_answers_list.extend([combo_extra_2])
        elif ports == 1540:
            #Question 3
            for combination_extra_var_4 in product(add_syn, synonyms, add_individual_vocab):
                combo_extra_3 = ' '.join(list(combination_extra_var_4)).lower()
                adding_answers_list.extend([combo_extra_3])
        elif ports == 1740:
            #Question 3
            
            
            for combination_extra_var_6 in product(synonyms, question_static_words, filtered_stop_words, add_syn, second_stop_words, add_individual_vocab):
                combo_extra_5 = ' '.join(list(combination_extra_var_6)).lower()
                adding_answers_list.extend([combo_extra_5])
        else:
            for add_vocab in add_individual_vocab:
                adding_answers_list.append(add_vocab.lower())

    # Clean formatting
    upgraded_answer_list = [s.replace("_", " ") for s in adding_answers_list]

    upgraded_answer_list = set(upgraded_answer_list)

    print("Generated mark scheme vocabulary:", len(upgraded_answer_list))  # Debugging output
    
    return upgraded_answer_list  # Returning processed words

#question 9b stop words
question_9b = [(['employee'])]

question_9b_vocab_two = ["train"]

extra_answer_vocab = ['existing']
#[train][existing][employees]
add = ['value']

adding_words_to_markscheme(question_static_words=question_9b[0], question_words=question_9b_vocab_two, add_individual_vocab=add ,add_second_synonyms_vocab=extra_answer_vocab)

