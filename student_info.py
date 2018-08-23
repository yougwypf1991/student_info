r'''
    本模块包含：
        1.输入学生信息
        2.输出学生信息
        3.按成绩高-低输出学生信息
        4.按成绩低-高输出学生信息
        5.按年龄高-低输出学生信息
        6.按年龄低-高输出学生信息
        7.删除学生信息
        8.修改学生信息
        9.保存学生信息到si.txt文件
        10.加载数据
'''

from menu import *
from student import *

def input_score():
    r'''
        输入学生成绩
    '''
    try:
        score = int(input('请输入学生成绩(0~100)：'))
    except:
        print('输入了无效的成绩。')
        score = 0
    else:
        if score < 0 or score > 100:
            print('输入成绩超过限制(0~100)。')
            score = 0
    finally:
        return score

    
def input_age():
    r'''
        输入年龄
    '''
    try:
        age = int(input('请输入学生年龄(5-70)：'))
    except:
        print('输入了无效的年龄。')
        age = 5
    else:
        if age < 5 or age > 70:
            print('输入年龄超过限制(5~70)。')
            age = 5
    finally:
        return age
    

def input_student(lst):
    r'''
        输入学生信息
        输入参数：
            lst 类的列表
    '''
    name = input("请输入学生姓名：") 
    if name == '':
        print("输入结束！")
        return
    age = input_age()
    score = input_score()
    stu_class = Student(name, age, score)
    
    return stu_class
    
    
    
def output_student(lst):
    r'''
        显示学生信息
        输入参数：
            lst 类的列表
    '''
    if not any(lst):
        return
    width = []
    width = get_print_width(lst)
    display_head(width)
    for S in lst:
        name, age, score = S.get_info()
        print('|' + name.center(width[0]), end = '')
        print('|' + str(age).center(width[1]), end = '')
        print('|' + str(score).center(width[2]), end = '|\n')
        
    print_head_line(width)
    
    

def output_student_by_score(lst, rever):
    '''
        rever = True: output desc by score
        rever = True: output asc by score
        输入参数：
            lst 类的列表
    '''
    L = sorted(lst, key = lambda stu : stu.get_score(), reverse=rever)
    output_student(L)


def output_student_by_age(lst, rever):
    '''
        rever = True: output desc by age
        rever = True: output asc by age
        lst为类的列表
    '''
    L = sorted(lst, key = lambda stu : stu.get_age(), reverse=rever)
    output_student(L)


def del_student(lst):
    r'''
        删除学生信息
        输入参数：
            lst 类的列表
    '''
    idx = 0
    name = input("请输入学生姓名(直接按enter结束)：") 
    if name == '':
        print("输入结束！")
        return
    it = iter(lst)           # 生成迭代器
    try:
        while True:
            stu = next(it)
            if name != stu.get_name():
                idx += 1
            else:
                break
    except StopIteration:
        print('没有查找到' + name + '的信息。')
        return
    else:
        del lst[idx]
    
        

def modify_student(lst):
    r'''
        修改学生信息
        输入参数：
            lst 类的列表
        注意：
            这里年龄和成绩是转换为字符串的方式存储到文件的，所以在加载该文件时需要重新转换为整型
    '''
    idx = 0
    name = input("请输入学生姓名(直接按enter结束)：") 
    if name == '':
        print("输入结束！")
        return
    age = input_age()
    score = input_score()
    
    it = iter(lst)               # 生成迭代器
    try:
        while True:
            stu = next(it)
            if name != stu.get_name():
                idx += 1
            else:
                break
    except StopIteration:
            print('没有查找到' + name + '的信息。')
            lst.append(Student(name, age, score))
    else:
        lst[idx].modify_infos(name, age, score)
        
    finally:
        return

    
def save_si_file(lst, filename):
    r'''
        保存学生信息到si.txt
            以逗号为分隔符，元素名称分别为：name, age, score
            输入参数：
                lst：携带学生信息的类的列表
        注意：
            年龄、成绩需要转换为整型数据
    '''
    try:
        fd = open(filename, 'w')
        for stu in lst:
            stu.write2file(fd)
    except:
        print('保存失败.')
    else:
        print('保存成功.')
    finally:
        fd.close()
    
    
def load_si_file(lst, filename):
    r'''
        从si.txt文件中加载学生信息
            输入参数：
                lst：将读取到的信息以类的形式追加到该列表中
    '''
    try:
        fd = open(filename, 'r')
        while True:
            person = fd.readline()
            if person == '':
                break
            person = person.strip()   # 去除换行符
            Name, Age, Score = person.split(',')
            stu_class = Student(Name, int(Age), int(Score))
            lst.append(stu_class)
    except:
        print('加载失败.')
    else:
        print('加载成功.')
    finally:
        fd.close()
