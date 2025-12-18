class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house # 初始化时也会自动调用setter

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")

        return cls(name, house)



def main():
    student = Student.get()

    print(student) # 当打印时会自动调用对象的__str__方法

if __name__ == "__main__":
    main()