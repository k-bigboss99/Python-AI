"""
class 類別名:
    屬性(成員變數)
    屬性
    ...
    成員函數(成員方法)
"""
class Person:
    num = 1
    def __init__(self, str, n):
        self.name = str
        self.age = n
    def SayHello(self):
        print("Hello")
    def PrintName(self):
        print("name:", self.name, "age:", self.age)
    def printNum(self):
        print(Person.num)

# 建立物件
p1 = Person("shizu", 20)
p2 = Person("charles", 19)
p1.PrintName()
p2.PrintName()

Person.num = 2
p1.printNum()
p1.printNum()

# 私有成員
"""
物件名稱._類別名+私有成員
"""

class Car:
    price = 100000
    def __init__(self, c, w):
        self.color = c     # 公有屬性color
        self.__weight = w  # 私有屬性weight

car1 = Car("Red", 10.5)
car2 = Car("Blue", 11.8)
print(car1.color)
# print(car1.__weight)
print(car1._Car__weight)

# 公有方法、私有方法、靜態方法
class Fruit:
    price = 0
    def __init__(self):
        self.__color = 'Red'
        self.__city = 'Kunming'
    def __outputColor(self):
        print(self.__color)
    def __outputCity(self):
        print(self.__city)
    def output(self):
        self.__outputColor()
        self.__outputCity()
    @ staticmethod
    def getPrice():
        return Fruit.price
    @ staticmethod
    def setPrice(p):
        Fruit.price = p

apple = Fruit()
apple.output()
print(Fruit.getPrice())
Fruit.setPrice(9)
print(Fruit.getPrice())

# 類別的繼承
"""
class 衍生類別名(基礎類別名):
    衍生類別成員
"""
import types
# 基礎類別必須繼承於object，否則再衍生類別中將無法使用super()函數
class Person(object):
    def __init__(self, name='', age=20, sex='male'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)
    def setName(self, name):
        if(type(name) != str):
            print("name must be string")
            return
        self.__name = name
    def setAge(self, age):
        if(type(age) != int):
            print("name must be int")
            return
        self.__age = age
    def setSex(self, sex):
        if(sex != 'male' and sex != 'female'):
            print("sex wrong")
            return
        self.__sex = sex
    def show(self):
        print("name:", self.__name, "age:", self.__age, "sex:", self.__sex)

class Student(Person):
    def __init__(self, name='', age=20, sex='male', schoolyear=1999):
        # 呼叫基礎類別建置方法初始化基礎類別的私有資料成員
        super(Student, self).__init__(name, age, sex)
        # Person.__init__(self, name, age, sex)
        self.setSchoolyear(schoolyear) # 初始化衍生類別的資料成員
    def setSchoolyear(self, schoolyear):
        self.__schoolyear = schoolyear
    def show(self):
        Person.show(self)
        # super(Student, self).show()
        print("year: ", self.__schoolyear)

if __name__ == '__main__':
    zhangsan = Person('張三', 19, 'male')
    zhangsan.show()
    lisi = Student('李四', 18, 'male', 2015)
    lisi.show()
    lisi.setAge(20)
    lisi.show()

