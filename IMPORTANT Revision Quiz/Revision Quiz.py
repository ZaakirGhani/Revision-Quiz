#Created modules
import Paper_One_2024
import Paper_Two_2024
import content_1

#built in modules
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet
import time
import threading
import csv
import matplotlib.pyplot as plt

#Universal divider
divider = ("-------------------------------")

#Variable that will kill the thread after all the questions are done
Stop_thread = False

#Timer
def normal_timer():
   
    for x in range(0, 9000, 1):
        global Stop_thread
        #calculated seconds, minutes and hours
        seconds = x % 60
        minutes = (x / 60) % 60
        hours = (x / 3600)
        #Stopping multi threading
        if Stop_thread:
            #Displaying time at the end
            print(f'____________________________________________\nYou time was: {round(hours):02} hrs: {round(minutes):02} min: {round(seconds):02} sec')
            return
        time.sleep(1)

    print('\nTIMES UP!\n2 hr : 30 mins passed')
    exit()

def extra_time():
    global Stop_thread
    for x in range(0, 11280, 1):
        #calculated seconds, minutes and hours
        seconds = x % 60
        minutes = (x / 60) % 60
        hours = (x / 3600)
        #Stopping multi threading
        if Stop_thread:
            #Displaying time at the end
            print(f'____________________________________________\nYou time was: {round(hours):02} hrs: {round(minutes):02} min: {round(seconds):02} sec')
            return
        time.sleep(1)

    print('\nEXTRA TIME UP!\n3 hr : 8 mins passed')
    exit()

#Multi tasking timer while doing exams
def normal_multi_threading():
    signal = True
    print('_____________________________________________\n- Normal time(2 hrs and 30 mins)\n- Extra time(3 hrs 8 mins)')
    while signal:
        try:
            chosen_time = input('_______________\nSelect time: ').strip().lower()
        except:
            signal = True
        else:
            if chosen_time in ['normal','normal time','normal time(2 hrs and 30 mins)','1','2 hrs and 30 mins']:
                stopwatch = threading.Thread(target=normal_timer)
                stopwatch.start()
                signal = False
            elif chosen_time in ['extra','extra time','2','extra time(3 hrs 8 mins)','3 hrs 8 mins']:
                stopwatch = threading.Thread(target=extra_time)
                stopwatch.start()
                signal = False
            else:
                print(f'\nSorry, you have either not entered anything or incorrectly typed the wrong words or number\nType, 1 for first option and 2 for second or type the option names\n{divider}')
    return stopwatch
    

#Menu FUNCTION
def year_one_menu():
    signal = True
    #Displaying options
    print("Digital Production Revision Quiz Kit")
    print("- 2024 Papers")
    print("- Revision")
    print("- Exit")
    while signal:
        try:
            #Enter Options
            select_menu = input("Select: ").strip().lower()
        except:
            signal = True
        else:
            #branching specific options:
            #2024 paper
            if select_menu in ['2024','2024 papers','1', '2024papers','2024 paper', '2024paper']:
                paper_2024()
                signal = False
            #revision selection            
            elif select_menu in ['revision','2']:
                revision()
                signal = False
            elif select_menu in ['exit','3']:
                print("Exiting...")
                exit()
            else:
                print(f'{divider}\nSorry, you have not entered anything!\n{divider}')


def revision():
    #Signal default true
    signal = True
    #Display topics
    print('_______________\nRevision Topics:\n- Content 1: Problem Solving\n- Content 2: Programming\n- Content 3: Moral & Ethical\n- Content 4: Legislation')
    print('- Content 5: Business Environment\n- Content 6: Data\n- Content 7:  Digital environments\n- Content 8: Security\n______________________')

    #Contents functions stored in dictionary
    contents_dictionary = {
    '1':content_1_selection, #Numbers
    '2':'programming',
    '3':'moral and ethical',
    '4':'legislation',
    '5':'business environment',
    '6':'data',
    '7':'digital environments',
    '8':'security',
    'problem solving':content_1_selection, #Words
    'programming':'content 2',
    'moral and ethical':'content 3',
    'legislation':'content 4',
    'business environment':'content 5',
    'data':'content 6',
    'digital environment':'content 7',
    'security':'content 8',
    'moral':'content 3',    #varition of words
    'moral & ethical':'content 3',
    'business':'content 5',
    'digital environments':'content 7',
    }

    #looping based on signal as true
    while signal:
        #error handling
        try:
            select_content = input('Select Content: ').lower().strip()
        except:
            signal = True
        else:
            #Searching contents
            find_contents = contents_dictionary.get(select_content)
            
            #Display or work function and break out of loop
            if find_contents:
                find_contents()
                signal = False
            else:
                    #Display error
                    print(f'{divider}\nSorry, you have not inputed the following: \nFOR\n PROBLEM SOLVING, SELECT: 1, problem solving\nPROGRAMMING, SELECT: 2, programming')
                    print('MORAL AND ETHICAL ISSUES, SELECT: 3, moral, ethical, moral and ethical, moral & ethical\nLEGISLATION, SELECT: 4, legislation\nBUSINESS ENVIRONMENT, SELECT: 5, business, business environment')
                    print(f'DATA, SELECT: 6, data\n DIGITAL ENVIRONMENTS, SELECT: 7, digital environments, digital environment\nSECURITY, SELECT: 8, security\n{divider}')
                    

#Selecting paper 
def paper_2024():
    print("_______________\n2024 papers:\n- paper 1\n- paper 2\n_______________")
    #Options stored in lists:
    #Papers
    signal = True
    while signal:
        try:
            select_paper = input("Select Paper: ")
        except:
            signal = True
        else:
            if select_paper in ['paper 1', '1']:
                first_paper_1_2024()
                signal = False
            elif select_paper in ['paper 2', '2']:
                second_paper_2_2024()
                signal = False
            else:
                print(f'{divider}\nSorry, you have not inputed the following: \nFOR\nPAPER 1, SELECT: 1, paper 1\nPAPER 2, SELECT: 2, paper 2\n{divider}')
                signal = True

#2024 paper 1 FUNCTION
def first_paper_1_2024():
   stopwatch = normal_multi_threading()
   Paper_One_2024.paper_1_2024()
   global Stop_thread
   Stop_thread = True
   stopwatch.join()
   

#2024 paper 2 FUNCTION
def second_paper_2_2024():
    stopwatch = normal_multi_threading()
    Paper_Two_2024.paper_2_2024()
    global Stop_thread
    Stop_thread = True
    stopwatch.join()
    



#CONTENT 1 selection FUNCTION
def content_1_selection():
    print('_____________________________\nCONTENT 1: PROBLEM SOLVING\n- Quiz\n- Information material')
    user_selections = input('Select: ').lower().strip()
    if user_selections in ['quiz','1']:    
        content_1.content_1_quiz()
    elif user_selections in ['information','information material','2']:
        content_1.content_1_information()

def Stopwords(user_input):

    Stop_Words = set(stopwords.words('english'))

    

    word = word_tokenize(user_input)

    word_list = []

    for w in word:
        if w not in Stop_Words:
            word_list.append(w)
    
    print (word_list)


year_one_menu()