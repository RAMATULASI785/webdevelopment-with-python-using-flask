'''print("HELLO RAMATULASI")
#function without parameter
def rama():
    print("tulasi reddy")
rama()

#function with parameters
def hari(name):
    print("welcome" +name)
hari("sonu")

# parameter with value
def hari(name="sonu"):
    print("welcome" +name)
hari()

#function with keyword arguments
def demo(name,age,des):
    print(name)
    print(age)
    print(des)
demo("tulasi",20,"student")


#function with keyword arguments with different order
def demo(name,age,des):
    print(name)
    print(age)
    print(des)
demo(age="tulasi",name=20,des="student")

 list with functions
list =["romaba","wbc","bnx"]
list1 =[{"name":"benz","year":2012},{"name":"samsu","year":2013},{"name":"cod","year":2014}]
print (list1)'''

##### print in a tabluar format using functions
'''def demo1(list3):
    for i in list3:
        print(i)
list3=["rama","krish","tulasi"]
demo1(list3)'''
####### print by index
'''def demo1(list3):
    for i in list3:
        print(i)
        print(list3[2])
list3=["rama","krish","tulasi"]
demo1(list3)'''

####### classes and object
# creating object
class register:
    print("welcome")
    x = 7875
    t = 'tulasi'
obj=register()
print(obj)
print(obj.x)
print(obj.t)

#### using init function

class register1:
    def __init__(self,name,des):
        self.name=name
        self.des=des
    def login(self):
        print("login completed",self.name)
object=register1("rama","krish")
print(object.name)
object.login()








