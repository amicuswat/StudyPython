import datetime
import random

from questions import Add, Multiply


class Quiz:
    questions = []
    answers = []

    def __init__(self):
        question_types = (Add, Multiply)
        # generat 10 random questions with numbers from 1 to 10
        for _ in range(10):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = random.choice(question_types)(num1, num2)
            self.questions.append(question)
        # add these questions into self.questions

    def take_quiz(self):
        # log the start time
        # ask all of the questions
        # log if they got question right
        # log the end time
        # show a summary
        pass

    def ask(self, question):
        # log the start time
        # capture the answer
        # check the answer
        # log the end time
        # if the answer's right, send back True
        # otherwise, send back False
        # send back the elapsed time, too
        pass

    def total_correct(self):
        # return the total # of correct answers
        total = 0
        for answers in self.answers:
            if answer[0]:
                total += 1
        return total

    def summary(self):
        # print how many you got right and the total # of questions. 5/10
        print("You got {} out of {} right.".format(
            self.total_correct(), len(self.quesitons)
        ))
        # print the total time for the quiz: 30 seconds!
        print("It took you {} seconds total.".format(
            (self.end_time-self.start_time).seconds
        ))
