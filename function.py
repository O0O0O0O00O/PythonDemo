import math


def equation(a, b, c):
    """
    一元二次方程的根
    :param a:
    :param b:
    :param c:
    :return:
    """
    if a == 0 and b==0:
        return "a，b不能同时为零"
    elif a == 0 and b != 0:
        x = (-c)/b
        return x
    elif a != 0 and b!=0:
        x1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
        return x1, x2



def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)
print("阶乘：", fact(3))


def add(x, y=5):
    print("x+y=", x+y)

add(3)

def addTest(L=None):
    if L is None:
        L = []
    L.append("test")
    print(L)

addTest()
addTest()


def _sum(*numbers):
    s = 0
    for n in numbers:
        s=s+n
    print("结果为：", s)

_sum(1, 2, 3)
_sum(1, 2, 3, 4, 5)
#定义列表，*numbers将list的所有元素作为可变参数传进去
numbers=[1,2,3,4,5]
_sum(*numbers)


def student(name, age, **keywords):
    print("name:",name,",age:",age,",keywrods:",keywords)

student("guangyi",16)
student("guangyi", 16, city="hang", gender="M")
information={"city" : "hang", "gender":"M","other":"nothing"}
# 将字典information的所有key-value用关键字参数传递到函数的**keywords中，keywords将获得一个字典，它是传information的拷贝
student("guangyi", 16, **information)

def student(name,age,*,city,job):
    print("name:", name, ",age:", age, ",city:", city,"job:",job)

student("guangyi",16,city="hang",job="IT engineer")

def student(name,age,*args,city,job):
    print("name:", name, ",age:", age,"args:",args ,",city:", city,"job:",job)

student("guangyi",16,1,2,"test",city="hang",job="IT engineer")

def student(name,age,*args,city="hang zhou ",job):
    print("name:", name, ",age:", age,"args:",args ,",city:", city,"job:",job)

student("guangyi", 16, 1, 2, "test", job="IT engineer")