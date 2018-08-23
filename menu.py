r'''
    1.显示菜单信息；
    2.按字符串长短自适应的显示学生信息。
'''
def get_print_width(lst):
    r'''
        获得最长的字符串宽度，默认名字宽度为4，默认年龄宽度为3，默认成绩宽度为5
        输入参数：
            lst 类的列表
    '''
    name_width = 4
    age_width = 3
    score_width = 5
    for stu in lst:
        if name_width <= len(str(stu.get_name())):
            name_width = len(str(stu.get_name()))
            
        if age_width <= len(str(stu.get_age())):
            age_width = len(str(stu.get_age()))
            
        if score_width <= len(str(stu.get_score())):
            score_width = len(str(stu.get_score()))
    
    return [name_width, age_width, score_width]


def show_menu():
    r'''
        打印菜单
    '''
    print('+-------------------------------------+')
    print('| 1 ) 添加学生信息                    |')
    print('| 2 ) 显示学生信息                    |')
    print('| 3 ) 删除学生信息                    |')
    print('| 4 ) 修改学生信息                    |')
    print('| 5 ) 按学生成绩高-低显示学生成绩     |')
    print('| 6 ) 按学生成绩低-高显示学生成绩     |')
    print('| 7 ) 按学生年龄高-低显示学生成绩     |')
    print('| 8 ) 按学生年龄低-高显示学生成绩     |')
    print('| 9 ) 保存学生信息(默认si.txt)        |')
    print('| 10) 加载学生信息(默认si.txt)        |')
    print('| q ) 退出                            |')
    print('+-------------------------------------+')
    

def print_head_line(width):
    r'''
        根据传入的宽度参数输出方框的顶和底线
    '''
    print('+', end = '')
    print('-' * width[0], end = '+')
    print('-' * width[1], end = '+')
    print('-' * width[2], end = '+\n')
    return None


def display_head(width):
    r'''
        自适应输出信息头
        输入参数：
            width：为一个列表
                   第一个元素为name对应的头的快读
                   第二个元素为age对应的头的宽度
                   第三个元素为score对应的头的宽度
    '''
    print_head_line(width)
    print('|' + 'name'.center(width[0]), end = '')
    print('|' + 'age'.center(width[1]), end = '')
    print('|' + 'score'.center(width[2]), end = '|\n')
    print_head_line(width)
    return None
