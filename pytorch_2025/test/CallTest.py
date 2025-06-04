class Person:
    def __call__(self, name):
        print("__call__"+"Hello"+name)

    def hello(self, name):
        print("hello"+name)

person = Person()
person("zhangsan")#直接用对象调用
person.hello("zhangsan")#调用了对象的方法