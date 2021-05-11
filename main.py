import os
import addStudent
import deleteStudent
import rankStudent
import changestudent

filePath = 'student.txt'


def main():
    if not os.path.isfile(filePath):
        open(filePath, 'a').close()

    while True:
        print('\n\n')
        print('-------------------学生信息管理系统--------------------')
        print('|   菜单                                     |')
        print('|   1：添加学生信息                            |')
        print('|   2：删除学生信息                            |')
        print('|   3：更改学生信息                            |')
        print('|   4：按成绩排序                              |')
        print('|   0：退出                                   |')
        print('-----------------------------------------------------')
        instruct = input('请输入选项：')
        if instruct == '0':
            exit(0)
        elif instruct == '1':
            addStudent.addStudent(filePath)
        elif instruct == '2':
            deleteStudent.deleteStudent(filePath)
        elif instruct == '3':
            changestudent.changeStudent(filePath)
        elif instruct == '4':
            rankStudent.rankStudent(filePath)
        else:
            print('输入错误，请输入正确选项...')


if __name__ == '__main__':
    main()
