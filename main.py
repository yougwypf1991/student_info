#!/usr/bin/env python3
r'''
    学生管理系统入口模块
'''
from menu import *
from student_info import *


students = []
filename = '/home/tarena/kanglu/exercise/student/si.txt'
while True:
    try:
        show_menu()
        myinput = input('请输入你的选择：')
        if myinput == '1':
            while True:
                stu = input_student(students)
                if stu == None:
                    break
                students.append(stu)
        elif myinput == '2':
            output_student(students)
        elif myinput == '3':
            if any(students):
                del_student(students)
            else:
                continue
        elif myinput == '4':
            if any(students):
                modify_student(students)
                pass
            else:
                continue
        elif myinput == '5':
            output_student_by_score(students, True)
        elif myinput == '6':
            output_student_by_score(students, False)
        elif myinput == '7':
            output_student_by_age(students, True)
        elif myinput == '8':
            output_student_by_age(students, False)
        elif myinput == '9':
            fname = input('请输入保存信息的文件名(默认直接enter)：')
            if fname == '':
                fname = filename
            save_si_file(students, fname)
        elif myinput == '10':
            fname = input('请输入加载信息的文件名(默认直接enter)：')
            if fname == '':
                fname = filename
            load_si_file(students, fname)
        elif myinput in ['q', 'Q', 'quit', 'Quit', 'QUIT', 'exit', 'EXIT', 'Exit']:
            break
        else:
            print('输入错误，请重新输入。')
    except (KeyboardInterrupt, EOFError):
        print('\nDo you really want to exit ([y]/n)?')
        s = input()
        if s in ['', 'y', 'yes', 'Y', 'YES']:
            break
