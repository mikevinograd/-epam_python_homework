import datetime


class Homework:
    """Created when new customer registers"""

    def __init__(self, text: str, deadline: int, created: datetime):
        self.text = text
        self.deadline = deadline
        self.created = created

    def is_active(self):
        return datetime.datetime.now() < (self.created + datetime.timedelta(days=self.deadline))


ex = Homework('testtest', 10, datetime.datetime(2021, 11, 19, 11, 23, 33, 604000))


# print(ex.is_active())

class Student:
    """Created when new customer registers"""

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, Homework):
        return Homework if Homework.is_active() else print('You are late')


exstudent = Student('Sychov', 'Yan')


# print(exstudent.do_homework(ex))

class Teacher:
    """Created when new customer registers"""

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text, deadline):
        return Homework(text, deadline, datetime.datetime.now())


teach = Teacher("Yoba", "Boba")
# print(teach.create_homework('123456', 20).text)
if __name__ == '__main__':
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')
    teacher.last_name  # Daniil
    student.first_name  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
