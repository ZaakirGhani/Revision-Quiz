#filtering information
from nltk.corpus import wordnet

def get_synonyms(markscheme_vocab):
    synonyms = set()

    # Breaking down mark scheme vocabulary
    for word in markscheme_vocab:
        # Extract synonyms using WordNet
        for syn in wordnet.synsets(word[0],pos=word[1]):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name()) 
    
    #Filtering words based on word list
    filtering_synonyms = [wasted_words for wasted_words in synonyms if wasted_words not in word[2]]

    return sorted(filtering_synonyms)

wording =('oeuvre','dwelling_house','placement','forcible','body_process','twist','household','house','somebody','datum','GPS','abode','place','physical','workplace','work','wheel','action',
          'Global_Positioning_System','advance','base','alter','activeness','condom','wellness','rubber','safe','safety','want')

question_8c_vocabulary = [('changes',wordnet.VERB, wording),('behaviour',wordnet.NOUN,wording),('individuals',wordnet.NOUN,wording),('resources',wordnet.NOUN,wording),('manufacture',wordnet.VERB,wording),
                              ('devices',wordnet.NOUN, wording),('work',wordnet.NOUN,wording),('home',wordnet.NOUN,wording),('locations',wordnet.NOUN,wording),
                              ('gps',wordnet.NOUN, wording),('health',wordnet.NOUN,wording),('data',wordnet.NOUN,wording),('encourage',wordnet.VERB,wording),('more',wordnet.ADV,wording),
                              ('more', wordnet.ADJ,wording),('physical',wordnet.ADJ,wording),('activity',wordnet.NOUN,wording),('walking',wordnet.VERB,wording),('cycling',wordnet.VERB,wording),
                              ('safety',None,wording),('desire',wordnet.VERB,wording)]

syno = get_synonyms(question_8c_vocabulary)
print(syno)