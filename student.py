class Student:
    def __init__(self, name, id, grade):
        """init the method"""
        self.name = name
        self.id = id
        self.grade = grade

    def __lt__(self, other):
        return self.grade > other.grade

    def __str__(self):
        return self.name + '\t' + str(self.id) + '\t' + str(self.grade)

    def getStudentName(self):
        return self.name

    def getStudentId(self):
        return self.id

    def getStudentGrade(self):
        return self.grade

    def setStudentGrade(self, grade):
        self.grade = grade

