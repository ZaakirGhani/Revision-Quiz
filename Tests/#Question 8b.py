divider = '----------'

# 4-mark question function with 2 inputs
def four_marks_more_options(questions, Label1, label2):
    score = 0

    for question in questions:
        print(question[0])
        user_input1 = input(f"{divider}\n{Label1}: ").strip().lower()
        user_input2 = input(f"{divider}\n{label2}: ").strip().lower()
        
        users_inputs = [user_input1, user_input2]  # Store both responses

        score_count = sum(
            any(word in user_response for word in question[i])
            for user_response in users_inputs
            for i in range(1, 5)  # Check against all four answer lists
        )

        # Assign marks based on correct matches
        if score_count == 4:
            print(f"{divider}\nCorrect, full marks!\n")
            score += 4
        elif score_count == 3:
            print(f"{divider}\nGood job, 3 marks\n")
            score += 3
        elif score_count == 2:
            print(f"{divider}\nNice work, 2 marks\n")
            score += 2
        elif score_count == 1:
            print(f"{divider}\nAlmost! You got 1 mark\n")
            score += 1
        else:
            print(f"{divider}\nIncorrect\n")

    return score

# Example question
question_8b = [
    ('8b. Describe two ways the developer could use abstraction when developing the app. (4 marks)',
     ['decide on the needed inputs', 'needed inputs'],
     ['formulate key actions in the program', 'make key actions in the program'],
     ['identify necessary data', 'filter out unnecessary detail', 'identify data needs', 'data needs'],
     ['deciding on the inputs to the system', 'decide on the inputs', 'deciding on what will vary'])
]

# Run the function
question_8b_score = four_marks_more_options(question_8b, 'Option 1', 'Option 2')
print(f"Total Score: {question_8b_score}")
