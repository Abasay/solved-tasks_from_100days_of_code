
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """function to check if questions still remain"""
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        #OR
        # return self.question_number < len(self.question_list)

    def next_question(self):
        """Function to retreive the the current question from the question list"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)
    
    def check_answer(self, user_answer, db_answer):
        if user_answer.lower() == db_answer.lower():
            self.score = self.score + 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer is {db_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print()
        