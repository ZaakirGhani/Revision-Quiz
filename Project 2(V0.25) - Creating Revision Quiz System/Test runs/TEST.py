Questions = {
    "Question 1.1":{
        "Question": "1a. Identify one constant used in the program shown in Figure 1. (1 Mark)",
        "Answer":['ENTRY_COST','entry_cost','entry cost']
    },      
    "Question 1.2":{
        "Question": "1b. Identify one variable used in the program shown in Figure 1. (1 Mark)",
        "Answer": ['numoftickets','costoftickets']
    },
    "Question 1.3":{
      "Question": "1c. Describe how accepted style conventions have been used to make the code in \nFigure 1 more readable. (3 Marks)",
      "Answer": ['sensible naming styles', 'sensible naming style', 'pep 8','pep8','conventions'], 
      "Answer2": ['camelcase', 'snakecase', 'pascalcase','camel case','snake case','pascal case','meaningful identifiers','spacing'],
      "Answer3": ['convey the purpose of each variable', 'variable', 'clarify code structure',' start and end of words']
    },
    "Question 1.4":{
        "Question": "1d. Explain why line 4 in Figure 1 is needed. (3 Marks)",
        "Answer": ['input is a string'],
        "Answer2": ['converted into an intger','changed into an int'],
        "Answer3": ['used in calculations','avoid runtime errors','avoid errors']
    }
}




for key, Value in Questions.items():
    print(Value['Question'])
    d = input(": ").strip().lower()
    if d in Value['Answer']:
        print("Correct")
    elif d in Value['Answer1'] and d not in Value['Answer']:
        print("Correct")
    elif d in Value['Answer2']and d not in Value['Answer']:
        print("Correct")
    elif d in Value['Answer3']and d not in Value['Answer']:
        print("Correct")
    else:
        print("Incorrect")
        
        
        
    
    