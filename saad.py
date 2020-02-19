class students:
    saad='ssss'
    zaid=666

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    @classmethod
    def fun(cls,name):
        cls.zaid=name

    @staticmethod
    def printf(*sss,**ddd):
        print("hello world",sss,ddd)




obj1=students('saad',33)
obj1.fun(000.0089)
print(obj1.saad)
print(obj1.zaid)
a=[1,2,3]
c={'s':'siddiqui'}
students.printf(*a,**c)