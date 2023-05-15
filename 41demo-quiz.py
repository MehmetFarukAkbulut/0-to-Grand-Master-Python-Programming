#  Question

class Question:
    def __init__(self,text,choices,answer) :
        self.text=text
        self.choices=choices
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer
        

# Quiz
class Quiz:
    def __init__(self,questions) :
        self.questions=questions
        self.score=0
        self.questionIndex=0
    def getQuestion(self):
        return self.questions[self.questionIndex]
    def displayQuestion(self):
        question =self.getQuestion()
        print(f"Soru {self.questionIndex+1}: {question.text}")
        
        for q in question.choices:
            print("-"+q)
        
        answer= input("Cevap: ")
        self.guess(answer)
        
    def guess(self,answer):
        question =self.getQuestion()
        if question.checkAnswer(answer):
            self.score+=1
        self.questionIndex+=1
        self.displayQuestion()
            
q1=Question("En iyi programlama dili hangisidir ?",["C#","python","javascript","java"],"python")
q2=Question("En popüler programlama dili hangisidir ?",["javascript","C#","python","java"],"python")
q3=Question("En çok kazandıran programlama dili hangisidir ?",["python","C#","javascript","java"],"python")
questions=[q1,q2,q3]

quiz=Quiz(questions)
quiz.displayQuestion()