#Question 2
def question_2_more_answers(question):
    question_2 = ("\n2. State two professional organisations that provide guidance on accessibility and \nquality in IT systems. (2 Marks)")        
    print(question_2)
    
    #Enter Answer
    print("______________\nName two:")
    Enter_1 = input("1: ")
    
    
    if any(word in Enter_1 for word in question):
        marks+=1
        print("Correct")
    else:
        print("Incorrect")
    
    Enter_2 = input("2: ")
    
    if any(word in Enter_2 for word in question) and Enter_2 != Enter_1:
        marks+=1
        print("Correct")
    elif Enter_1 == Enter_2:
        print("Thats two answer so only one mark!")
    else:
        print("Incorrect!!")