import student
import utils


def changeStudent(filePath):
    f = open(filePath, 'r')
    studentList = []
    for line in f.readlines():
        stuInfo = line.strip().split()
        stu = student.Student(stuInfo[0], int(stuInfo[1]), int(stuInfo[2]))
        studentList.append(stu)
    f.close()

    if len(studentList) == 0:
        print('没有学生信息！请添加学生信息....')
        return

    id = input('请输入学生id：')
    idx = utils.searchStudentId(studentList, int(id))
    while idx > len(studentList):
        id = input('学生信息没有找到，请输入正确学生id：')
        idx = utils.searchStudentId(studentList, int(id))

    grade = input('请更改此学生的成绩：')
    while not utils.checkGrade(grade):
        grade = input('格式错误，请输入正确成绩：')

    studentList[idx].setStudentGrade(grade)
    instruct = input('保存？Y/N: ')
    if instruct.lower() == 'y':
        f = open(filePath, 'w')
        for stu in studentList:
            f.write(str(stu) + '\n')
        f.close()
        print('保存...')
