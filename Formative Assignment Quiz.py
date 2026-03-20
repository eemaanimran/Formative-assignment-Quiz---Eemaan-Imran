def askQuestions():
    #Store the questions in a list, pairing them with the answer
    questions = {
    "Question 1: What is 5 * 5?": "25",
    "Question 2: What colour do you get when you mix blue and yellow?": "Green",
    "Question 3: What is the national flower of Japan?": "Cherry Blossom",
    "Question 4: How many days are in a year?": "365",
    "Question 5: How many dots appear on a pair of dice?": "42",
    #returning dictionary to access in other functions
    }
    return questions

#checks answer is correct
def checkAnswers(questions):
    #Score for number of correct answers
    score = 0
    #FOR loop to check answers and add scores
    for question, correctAnswer in questions.items():
        userAnswer = input(question + " ")
        
        if userAnswer.lower() == correctAnswer.lower():
            print("Correct, you earned a point!")
            score += 1
        else:
            print("Incorrect, no point receieved!")
    
    return score

#Runs the quiz and collects
def quizProgram():
    print("Welcome to the quiz!")

    questions = askQuestions()
    score = checkAnswers(questions)
    print("Well Done! You've completed the quiz :D! Your score is:", score, "out of 5")

quizProgram()

        

