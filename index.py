# -*- coding: utf-8 -*-


class Student(object):
  def __init__(self,name,gender):
    self.name=name
    self.__gender=gender
  def get_gender(self):
  	return self.__gender
  def set_gender(self,gender):
    self.__gender=gender



# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('0000!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('0000!')
    else:
        print('1111!')
 



