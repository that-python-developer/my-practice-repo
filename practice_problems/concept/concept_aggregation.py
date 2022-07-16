class Student:

    def __init__(self, id):
        self._id = id

    def registration_number(self, department_id) -> str:
        return str(self._id) + '-' + department_id


class Department:

    def __init__(self, id, student):
        self._id = id
        self._student = student

    def student_registration(self):
        return self._student.registration_number(self._id)


if __name__ == '__main__':
    student = Student(10)
    department = Department('ENG', student)
    print(department.student_registration())
