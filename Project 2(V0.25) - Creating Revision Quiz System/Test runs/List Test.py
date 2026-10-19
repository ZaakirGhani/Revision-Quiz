#List Test
question_1c_and_1d = [
    ("1c. Describe how accepted style conventions have been used to make the code in \nFigure 1 more readable. (3 Marks)",
     ['sensible naming styles', 'sensible naming style', 'pep 8','pep8','conventions'],
     ['camelcase', 'snakecase', 'pascalcase','camel case','snake case','pascal case','meaningful identifiers','spacing'],
     ['convey the purpose of each variable', 'variable', 'clarify code structure',' start and end of words']),
    
    ("1d. Explain why line 4 in Figure 1 is needed. (3 Marks)",
      ['input is a string'],
      ['converted into an intger','changed into an int'],
      ['used in calculations','avoid runtime errors','avoid errors']
    )
]


marks=0



for Q in question_1c_and_1d:
    print(Q[0])
    D = input(": ")
    answer1_match = any(word in D for word in Q[1])
    answer2_match = any(word in D for word in Q[2])
    answer3_match = any(word in D for word in Q[3])
    #3 marks
    if answer1_match and answer2_match and answer3_match:
        print("Correct")
        marks+=3
    #2 marks    
    elif answer1_match and answer2_match or answer2_match and answer3_match:
        print("Correct")
        marks+=2
    #1 mark
    elif answer1_match or answer2_match or answer3_match:
        print("Correct")
        marks+=1
    else:
        print("Incorrect")
        
print("Marks:",marks)

