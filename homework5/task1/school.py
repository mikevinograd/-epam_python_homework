import datetime


class Homework:

    def __init__(self, text: str, deadline: int, created: datetime):
        self.text = text
        self.deadline = deadline
        self.created = created

    def is_active(self):
        return datetime.datetime.now() < (
            self.created + datetime.timedelta(days=self.deadline)
        )


class Student:

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework: Homework):
        return homework if homework.is_active() else print("You are late")


class Teacher:

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline, datetime.datetime.now())
