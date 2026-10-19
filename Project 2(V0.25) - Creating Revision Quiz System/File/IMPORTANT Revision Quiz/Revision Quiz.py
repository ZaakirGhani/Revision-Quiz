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
    
    print('_____________________________________________\n- Normal time(2 hrs and 30 mins)\n- Extra time(3 hrs 8 mins)')

    chosen_time = input('_______________\nSelect time: ').strip().lower()
    

    if chosen_time in ['normal','normal time','normal time(2 hrs and 30 mins)','1','2 hrs and 30 mins']:
        stopwatch = threading.Thread(target=normal_timer)
        stopwatch.start()
    elif chosen_time in ['extra','extra time','2','extra time(3 hrs 8 mins)','3 hrs 8 mins']:
        stopwatch = threading.Thread(target=extra_time)
        stopwatch.start()
    else:
        print('Sorry, you have not entered anything')
    return stopwatch
    

#Menu FUNCTION
def menu():
    #Displaying options
    print("Digital Production Revision Quiz Kit")
    print("- 2024 Papers")
    print("- Revision")
    
    #Enter Options
    select_menu = input("Select: ").strip().lower()

    #Options stored in lists:
    #Papers
    papers = ((first_paper_1_2024,['paper 1', '1']),
              (second_paper_2_2024,['paper 2','2']))
    #Content
    contents = ((content_1_selection,['1','problem solving']), ('content 2',['2','programming']), ('content 3',['moral','ethical','3','moral and ethical','moral & ethical']),('content 4',['legislation','4']),
                ('content 5',['5','business','business environment']),('content 6',['data','6']),('content 7',['7','digital environments','digital environment']), ('content 8',['8','security']))
        
    #branching specific options:
    #2024 paper
    if select_menu in ['2024','2024 papers','1', '2024papers','2024 paper', '2024paper']:
        print("_______________\n2024 papers:\n- paper 1\n- paper 2\n_______________")
        select_paper = input("Select Paper: ")
        for function,keyword in papers:
            if select_paper in keyword:
                function()
    #revision selection            
    elif select_menu in ['revision','2']:
        print('_______________\nRevision Topics.\n- Content 1: Problem Solving\n- Content 2: Programming\n- Content 3: Moral & Ethical\n- Content 4: Legislation')
        print('- Content 5: Business Environment\n- Content 6: Data\n- Content 7:  Digital environments\n- Content 8: Security\n______________________')
        select_content = input('Select Content: ').lower().strip()
        for function,keyword in contents:
            if select_content in keyword:
                function()


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


menu()