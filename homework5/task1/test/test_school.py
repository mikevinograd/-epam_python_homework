import pytest
import datetime
from task1.school import Homework, Student, Teacher


def student_initialization():
    initialization = Student("Sychov", "Yan")
    return initialization


def teacher_initialization():
    initialization = Teacher("Feynman", "Richard")
    return initialization


def homework_initialization():
    initialization = Homework("text of HW", 10, datetime.datetime.now())
    return initialization


def test_homework_is_created():
    test_homework = Homework(
        "text of HW", 10, datetime.datetime(2020, 11, 19, 11, 23, 33, 604000)
    )
    assert test_homework.text == "text of HW"
    assert test_homework.deadline == 10
    assert test_homework.created == datetime.datetime(2020, 11, 19, 11, 23, 33, 604000)


def test_homework_is_active():
    active_homework = homework_initialization()
    assert active_homework.is_active() is True


def test_homework_is_disactive():
    active_homework = Homework(
        "text of HW", 10, datetime.datetime(2000, 11, 19, 11, 23, 33, 604000)
    )
    assert active_homework.is_active() is False


def test_student_is_created():
    test_student = student_initialization()
    assert test_student.first_name == "Yan"
    assert test_student.last_name == "Sychov"


def test_teacher_is_created():
    test_teacher = teacher_initialization()
    assert test_teacher.first_name == "Richard"
    assert test_teacher.last_name == "Feynman"


def test_student_doing_homework():
    test_student = student_initialization()
    test_homework = homework_initialization()
    assert test_student.do_homework(test_homework) == test_homework


def test_student_late(capfd):
    test_student = student_initialization()
    late_homework = Homework(
        "text of HW", 10, datetime.datetime(2000, 11, 19, 11, 23, 33, 604000)
    )
    test_student.do_homework(late_homework)
    stdout, stderr = capfd.readouterr()
    assert test_student.do_homework(late_homework) is None
    assert stdout == "You are late\n"
    assert stderr == ""
