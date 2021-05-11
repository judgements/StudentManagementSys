import utils


def addStudent(filePath):
    print('请输入学生信息，其中id为四位数字')
    name = input('请输入学生姓名：').replace(' ', '')
    id = input('请输入学生id：')
    while not utils.checkId(id):
        id = input('格式错误，请输入正确id格式：')
    grade = input('请输入学生成绩：')
    while not utils.checkGrade(grade):
        grade = input('格式错误！请输入正确成绩格式：')
    print('您已经成功添加：')
    print('姓名：', name, '，id：', id, '，成绩：', grade)
    instruct = input('保存？（Y/N）:')
    if instruct.lower() == 'y':
        f = open(filePath, 'a')
        f.write(name + '\t' + id + '\t' + grade + '\n')
        f.close()
        print('保存...')
