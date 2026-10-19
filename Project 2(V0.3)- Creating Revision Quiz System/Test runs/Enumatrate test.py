QUESTION_2 = ("\n2. State two professional organisations that provide guidance on accessibility and \nquality in IT systems. (2 Marks)")        
print(QUESTION_2)

QUESTION_2_ANSWER = ['ISO','W3C','IETF','BCS','IEEE','NTSE']

answers = [input("1. ").strip().lower(), input("2. ").strip().lower()]

for i,m in enumerate(answers):
    if (word in answers for word in m.split()):
        print('Correct')
        if i==1:
            print("Thats one")
            break
    else:
        print('Incorect')