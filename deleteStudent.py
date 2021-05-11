import student
import utils


def deleteStudent(filePath):
    f = open(filePath, 'r')
    studentList = []
    for line in f.readlines():
        stuInfo = line.strip().split()
        stu = student.Student(stuInfo[0], int(stuInfo[1]), int(stuInfo[2]))
        studentList.append(stu)
    f.close()

    if len(studentList) == 0:
        print('没有学生信息，请添加学生：')
        return

    id = input('请输入学生id：')
    idx = utils.searchStudentId(studentList, int(id))
    instruct = input('确定删除？Y/N')
    if instruct.lower() == 'y':
        del studentList[idx]
        f = open(filePath, 'w')
        for stu in studentList:
            f.write(str(stu) + '\n')
        f.close()
        print('保存...')
