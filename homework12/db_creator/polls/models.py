from django.db import models


class Homework(models.Model):
    db_table = "Homework"

    text = models.CharField(max_length=200)
    deadline = models.IntegerField(default=7)
    created = models.DateTimeField()

    def __str__(self) -> str:
        return self.text


class HomeworkResult(models.Model):
    db_table = "HomeworkResult"

    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.CharField(max_length=2000)
    author = models.ForeignKey("Student", on_delete=models.CASCADE)
    created = models.DateTimeField()

    def __str__(self) -> str:
        return self.solution


class Student(models.Model):
    db_table = "Student"

    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"self.last_name, self.first_name"


class Teacher(models.Model):
    db_table = "Teacher"

    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    homework_done = models.ForeignKey(HomeworkResult, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"self.last_name, self.first_name"
