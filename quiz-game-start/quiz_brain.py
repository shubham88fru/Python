class QuizBrain:
    def __init__(self, questions):
        self.questions_list = questions
        self.question_number = 0

    def next_question(self):
        ans = input(f"Q.{self.question_number}: {self.questions_list[self.question_number].text} (True/False)?: ")
        if ans == self.questions_list[self.question_number].answer:
            print("Correct")
        else:
            print("BOO")
        self.question_number += 1

    def has_question(self):
        return self.question_number < len(self.questions_list)
