class Student:

    def __init__(self, id):
        self._id = id

    def registration_number(self, department_id) -> str:
        return str(self._id) + '-' + department_id


class Department:

    def __init__(self, department_id, student_id):
        self._id = department_id
        self._student = Student(student_id)

    def student_registration(self):
        return self._student.registration_number(self._id)


if __name__ == '__main__':
    department = Department('ENG', 10)
    print(department.student_registration())
