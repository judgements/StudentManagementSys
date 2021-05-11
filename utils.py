import student


def searchStudentId(studentList, id):
    idx = 0
    for stu in studentList:
        if stu.getStudentId() == id:
            return idx
        else:
            idx += 1
    return idx


def fileRead(filePath):
    f = open(filePath, "r")
    studentList = []
    for line in f.readlines():
        studentInfo = line.strip().split()
        stu = student.Student(studentInfo[0], int(studentInfo[1]), int(studentInfo[2]))
        studentList.append(stu)
    f.close()
    return studentList


def fileWrite(filePath, studentList):
    f = open(filePath, "w")
    for stu in studentList:
        f.write(str(stu) + '\n')
    f.close()


def checkId(id):
    if len(id) == 4 and id.isdigit():
        return True
    else:
        return False


def checkGrade(grade):
    if grade.isdigit() and 0 <= int(grade) <= 100:
        return True
    else:
        return False

