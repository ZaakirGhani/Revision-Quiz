#Content 1 Quiz
def content_1_quiz():
    print('___________________________\nQuiz')
    #1.1.1: Top-down, Bottom-up and modularisation
    #top-down questions
    top_down_questions = [('How do you use TOP DOWN APPROACH to problem solve?',['Answers 1'],
                           'What are the benefits of the TOP DOWN APPROACH',['always broken down into smaller units',
                                                                             'the designer can define the requirements of what the program needs to do',
                                                                             'subunits gets less complex as you progress',
                                                                             'tasks and code can be reused again',
                                                                             'saves time','units can be updatable'],
                           'What are the challenges of the TOP DOWN APPROACH',['Answers 3'])]
    
    for questions in top_down_questions:
        print(questions[0])
        print(questions[1])

#Content 1 Information Material
def content_1_information():
    print('___________________________\nInformation Material\n')
    print('1.1 COMPUTATIONAL THINKING\n___________________________')
    #Outputing 1.1
    print('1.1.1 - Top down, bottom up and modularisation approach\n1.1.2 - Decomposition\n1.1.3 - Pattern Recognition\n1.1.4 - Abstraction')
    #Outputiing 1.2
    print('___________________________\n1.2 Algorithms\n___________________________\n1.2.1 - Understand how algorithms are expressed\n1.2.2 - Expressing algorithms with flowcharts and pseudocode')
    print('1.2.3 - Algorithms and programming constructs(Sequence, Selection and Iteration)\n1.2.4 - Understand the purpose and how algorithms work\n1.2.5 - determine correct output of an algorithm')
    print('1.2.6 - To identify and correct errors in an algorithm\n')

    select_material = input('Select material: ')