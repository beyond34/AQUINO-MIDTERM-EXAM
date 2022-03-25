class student:
    #initialize
    def __init__ (self, name, subject, section):
        self.name = name
        self.subject = subject
        self.section = section
    #accept inputs
    def input_student(self, name, subject, section):
        self.name = str(input("Enter you Surname: "))
        self.subject = str(input("Enter your Subject: "))
        self.section = str(input("Enter your section: "))
    #display inputs
    def displayINfo (self, name, subject, section):
        print("Hi! ", self.name, "you are taking Midterm Exam on the subject", self.subject, "Section", self.section)
        print("Thank you! Mr.", self.name, "you finish the exam")
name=("")
subject=("")
section=("")
obj = student(name, subject, section)
obj.input_student(name, subject, section)
obj.displayINfo(name,subject,section)