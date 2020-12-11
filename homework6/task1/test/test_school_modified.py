import pytest
import datetime
from task1.school_modified import Homework, HomeworkResult, Student, Teacher, DeadlineError


def test_homework_result_income_type_exception():
    good_student = Student("Sychov", "Yan")
    with pytest.raises(ValueError, match="You gave a not Homework object"):
        HomeworkResult("Not suitable HW type", "Some solution", good_student, datetime.datetime.now())


def test_deadline_exeption():
    hw_deadlined = Homework("Some text", -1, datetime.datetime.now())
    good_student = Student("Sychov", "Yan")
    with pytest.raises(DeadlineError, match="You are late"):
        good_student.do_homework(hw_deadlined, "Some solution")


def test_check_homework():
    opp_teacher = Teacher('Daniil', 'Shadrin')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    result = good_student.do_homework(oop_hw, 'I have done this hw')

    assert opp_teacher.check_homework(result) is True
    assert result.homework in opp_teacher.homework_done


def test_check_homework_negative_result():
    opp_teacher = Teacher('Daniil', 'Shadrin')
    bad_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    result = bad_student.do_homework(oop_hw, 'done')

    assert opp_teacher.check_homework(result) is False
    assert result.homework not in opp_teacher.homework_done


def test_homework_done():
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    good_student = Student('Lev', 'Sokolov')
    oop_hw = opp_teacher.create_homework('Learn OOP', 1)

    result = good_student.do_homework(oop_hw, 'I have done this hw')
    opp_teacher.check_homework(result)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result)
    temp_2 = Teacher.homework_done

    assert temp_1 == temp_2
