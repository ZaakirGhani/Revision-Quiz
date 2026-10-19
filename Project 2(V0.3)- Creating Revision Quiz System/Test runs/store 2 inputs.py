#Function that contains default value 
def io(label=['1.','2.']):
    #Score count defaulted to 0
    score=0
    #Lists to gain a score
    terance=[(['bikes','help'],['terrance','mike'])]
    
    #Variable is set to none
    checking_previous_input = None
    #Check
    for t in terance:
        for i in label:
            user_input = input(f'{i} ').strip().lower()
            
        
            answer_match_1 = any(word in user_input for word in t[0])
            answer_match_2 = any(word in user_input for word in t[1])
            
            
            summing = sum([answer_match_1, answer_match_2])
            
            
            
            
            if summing == 2:
                print('Correct')
                score+=2
            elif summing == 1:
                score+=1
            else:
                print('Incorrect')
                
            
            #Checking if any word of split words 
            if checking_previous_input and any(word in user_input.split() for word in checking_previous_input.split()) and summing > 0 and not summing == 2:
                print('Thats two of the same answer, so a mark has been deducted!')
                score -= 1
            
            if checking_previous_input and any(word in user_input.split() for word in checking_previous_input.split()) and summing == 2:
                print('Thats two of the same answer, so two marks has been deducted!!')
                score -= 2
            

            
            
            checking_previous_input = user_input

            
    return score

score =io(['user_input:','card:'])
print(score)