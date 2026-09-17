class Student:
    def __init__(self, name, age, specialty):
        self.name = name
        self.age = age
        self.specialty = specialty

    def show_info(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)
        print("Специальность:", self.specialty)

    def change_specialty(self, new_specialty):
        self.specialty = new_specialty


student = Student("Самандар", 18, "Информационные системы")

print("До изменения:")
student.show_info()

student.change_specialty("Программная инженерия")

print("\nПосле изменения:")
student.show_info()
