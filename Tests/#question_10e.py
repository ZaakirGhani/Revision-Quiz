divider = '------------------------------------'

def twelve_marker_evaluation_variation_one(questions):
    score=0
    for question in questions:
        print(question[0])
        user_input = input(f"{divider}\nEnter your answer: ").strip().lower()

        benefits = any(word in user_input for word in question[1])
        benefits2 = any(word in user_input for word in question[2])
        drawbacks = any(word in user_input for word in question[3])
        drawbacks2 = any(word in user_input for word in question[4])
        conclusion = any(word in user_input for word in question[5])

        full_marks_1 = all(word in user_input for word in question[1])
        full_marks_2 = all(word in user_input for word in question[2])
        full_marks_3 = all(word in user_input for word in question[3])
        full_marks_4 = all(word in user_input for word in question[4])
        full_marks_5 = all(word in user_input for word in question[5])

        score_count = sum([benefits, benefits2, drawbacks, drawbacks2, conclusion])

        full_marks = sum([full_marks_1, full_marks_2, full_marks_3, full_marks_4, full_marks_5])

        FULL_SCORE = sum([score_count, full_marks])
        
        #Some marks
        if FULL_SCORE == 1:
            print('Unfortutunately, this is one mark!!')
            score+=1
        elif FULL_SCORE == 2:
            print('Almost, you got 2 marks')
            score+=2
        elif FULL_SCORE == 3:
            print('Almost, you got 3 marks')
            score+=3
        elif  FULL_SCORE == 4:
            print('Good, you got 4 marks')
            score+=4
        elif FULL_SCORE == 5:
            print('Good, you got 5 marks')
            score+=5
        #Full marks
        elif FULL_SCORE == 6:
            print('Good, 8 marks.')
            score+=8
        elif FULL_SCORE == 7:
            print('Great, 9 marks')
            score+=9
        elif FULL_SCORE == 8:
            print('Great, 10 marks')
            score+=10
        elif FULL_SCORE == 9:
            print('Excellent, 11 marks')
            score+=11
        elif FULL_SCORE == 10:
            print('Correct, Full marks')
            score+=12
        else:
            score=0
    
    return score



question_10e = [('• a supported conclusion as to which algorithm the developer should choose. (12 marks)',
                     ['easy to understand','and develop','list of users','not need to be sorted before searched'],
                     ['very ineffecient','take a long time to complete','some users','could be waiting a long time before their details were retrieved','search increases greatly','o(n),',
                      'could hinder the growth of the number of users accessing the game'],
                     ['efficient','users would be able to access the game with little delay','search time does not grow rapidly','o(log^2n)'],
                     ['more complex algorithm to understand and develop','data must be in order for the algorithm to work'],
                     ['efficent','complexity','should choose binary search if the list is sorted','if unsorted','choose linear search','linear search offers flexibility','linear time complexity'],
                     [''])]

q = twelve_marker_evaluation_variation_one(question_10e)

print(q)