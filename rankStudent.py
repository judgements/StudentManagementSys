import student


def rankStudent(filePath):
    f = open(filePath, 'r')
    studentList = []
    for line in f.readlines():
        stuInfo = line.strip().split()
        stu = student.Student(stuInfo[0], int(stuInfo[1]), int(stuInfo[2]))
        studentList.append(stu)
    f.close()

    if len(studentList) == 0:
        print('没有学生信息，请添加学生信息..')
        return

    sortStudentList = sorted(studentList)
    print('姓名\t\t\tid\t\t\t成绩')
    for stu in sortStudentList:
        print(stu.getStudentName() + '\t\t\t' + str(stu.getStudentId()) + '\t\t\t' + str(stu.getStudentGrade()))