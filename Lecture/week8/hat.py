import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # 类属性，所有的对象共享，只有一份

    @classmethod # 表示这个是一个类方法，属于类，而不是类的对象
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Liweijie")