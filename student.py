r''' 
    本模块主要包含学生的类
'''
class Student:
    r'''
        关于学生的类
            包含属性：姓名，年龄，成绩
    '''
    def __init__(self, name = '', age = 5, score = 0):
        self.__name, self.__age, self.__score = name, age, score
        
    def get_info(self):
        r'''
            返回给调用者关于姓名、年龄和成绩的元组
        '''
        return (self.__name, self.__age, self.__score)
    
    def get_name(self):
        r'''
            返回给调用者姓名
        '''
        return self.__name
    
    def get_age(self):
        r'''
            返回给调用者年龄
        '''
        return self.__age
    
    def get_score(self):
        r'''
            返回给调用者成绩
        '''
        return self.__score
    def modify_infos(self, name, age, score):
        self.__name, self.__age, self.__score = name, age, score
    
    def write2file(self, fd):
        fd.write(self.__name)
        fd.write(',')
        fd.write(str(self.__age))
        fd.write(',')
        fd.write(str(self.__score))
        fd.write('\n')
