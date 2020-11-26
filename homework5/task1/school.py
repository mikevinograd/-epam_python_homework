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

    def do_homework(self, Homework):
        return Homework if Homework.is_active() else print("You are late")


class Teacher:

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text, deadline):
        return Homework(text, deadline, datetime.datetime.now())
