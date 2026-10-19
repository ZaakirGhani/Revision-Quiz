import nltk
from nltk.corpus import wordnet




def get_synonyms(word):
    synonyms = set()
    
    for synset in wordnet.synsets(word):  # Get all synsets for the word
        for lemma in synset.lemmas():  # Get each synonym (lemma)
            synonyms.add(lemma.name())  # Store synonym names
    
    return list(synonyms)  # Return unique synonyms as a list

def check_match(user_input, synonyms_list):
    user_words = user_input.lower().split()  # Break user input into words
    matched_words = [word for word in user_words if word in synonyms_list]
    
    return matched_words

# Example usage:
word_to_expand = "happy"
synonyms = get_synonyms(word_to_expand)
print(f"Synonyms for '{word_to_expand}':", synonyms)

user_input = "I feel joyful today"
matches = check_match(user_input, synonyms)
print("Matched words:", matches)
