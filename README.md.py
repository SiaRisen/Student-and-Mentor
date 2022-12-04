class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    def _mid_grade_(self):  # средняя оценка студентов за домашние задания
        sum = 0
        count = 0
        for grade in self.grades.values():
            for x in grade:
                sum += x
                count += 1
        return sum / count

    def __lt__(self, other):  # сравнение средней оценки студентов
        if not isinstance(other, Student):
            print('not a Student')
            return
        if (self._mid_grade_() > other._mid_grade_()) == True:
            return f'Высшую среднюю оценку за ДЗ имеет: {self.name} {self.surname}'
        else:
            return f'Высшую среднюю оценку за ДЗ имеет: {other.name} {other.surname}'

    def __str__(self):
        some_student = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {round(self._mid_grade_(), 1)}\n Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n Завершенные курсы: {",".join(self.finished_courses)}'
        return some_student


def all_hw(students_list,
           cource_name):  # подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
    sum = 0
    count = 0
    for student in students_list:
        for grade in student.grades[cource_name]:
            sum += grade
            count += 1
    return round(sum / count, 1)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    def _mid_lecturer_(self):  # средняя оценка лекторов за лекции
        sum = 0
        count = 0
        for grade in self.lecturer_grades.values():
            for x in grade:
                sum += x
                count += 1
        return sum / count

    def __lt__(self, other):  # сравнение средней оценки лекторов
        if not isinstance(other, Lecturer):
            print('not a Lecturer')
            return
        if (self._mid_lecturer_() > other._mid_lecturer_()) == True:
            return f'Высшую среднюю оценку за лекции имеет: {self.name} {self.surname}'
        else:
            return f'Высшую среднюю оценку за лекции имеет: {other.name} {other.surname}'

    def __str__(self):
        some_lecturer = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {round(self._mid_lecturer_(), 1)}'
        return some_lecturer


def all_lecturers(lecturers_list, cource_name):  # подсчет средней оценки за лекции всех лекторов в рамках курса
    sum = 0
    count = 0
    for lecturer in lecturers_list:
        for grade in lecturer.lecturer_grades[cource_name]:
            sum += grade
            count += 1
    return round(sum / count, 1)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Имя: {self.name}\n, Фамилия: {self.surname}'
        print(some_reviewer)


Student1 = Student('Ruoy', 'Eman', 'man')
Student2 = Student('Emma', 'Watson', 'woman')
Mentor1 = Mentor('Some', 'Buddy')
Mentor2 = Mentor('Shelly', 'Dou')
Lecturer1 = Lecturer('Larry', 'Sanders')
Lecturer2 = Lecturer('Kenny', 'Klarck')
Reviewer1 = Reviewer('Kendy', 'Gous')
Reviewer2 = Reviewer('Jhon', 'Travis')

Student1.courses_in_progress += ['Git']
Student1.courses_in_progress += ['Python']
Student2.courses_in_progress += ['Git']
Student2.courses_in_progress += ['Python']
Student1.finished_courses += ['Введение в программирование']
Student1.grades['Введение в программирование'] = [7, 9, 10]
Student2.finished_courses += ['Введение в программирование']
Student2.grades['Введение в программирование'] = [9, 10, 10]
Lecturer1.courses_attached += ['Git']
Lecturer1.courses_attached += ['Python']
Lecturer2.courses_attached += ['Git']
Lecturer2.courses_attached += ['Python']
Reviewer1.courses_attached += ['Python']
Reviewer2.courses_attached += ['Git']

Reviewer1.rate_hw(Student1, 'Python', 6)
Reviewer1.rate_hw(Student1, 'Python', 10)
Reviewer1.rate_hw(Student1, 'Python', 9)
Reviewer2.rate_hw(Student1, 'Git', 9)
Reviewer2.rate_hw(Student1, 'Git', 8)
Reviewer2.rate_hw(Student1, 'Git', 8)
Reviewer1.rate_hw(Student2, 'Python', 7)
Reviewer1.rate_hw(Student2, 'Python', 9)
Reviewer1.rate_hw(Student2, 'Python', 7)
Reviewer2.rate_hw(Student2, 'Git', 5)
Reviewer2.rate_hw(Student2, 'Git', 10)
Reviewer2.rate_hw(Student2, 'Git', 10)

Student1.rate_lecturer(Lecturer1, 'Python', 9)
Student1.rate_lecturer(Lecturer2, 'Python', 6)
Student1.rate_lecturer(Lecturer1, 'Git', 7)
Student1.rate_lecturer(Lecturer2, 'Git', 8)
Student2.rate_lecturer(Lecturer1, 'Python', 9)
Student2.rate_lecturer(Lecturer2, 'Python', 9)
Student2.rate_lecturer(Lecturer1, 'Git', 9)
Student2.rate_lecturer(Lecturer2, 'Git', 10)

print(Student1)
print()
print(Student2)
print()
print(Student1.__lt__(Student2))
print()
print(Lecturer1)
print()
print(Lecturer2)
print()
print(Lecturer1.__lt__(Lecturer2))
print()
print("Средняя оценка за домашние задания по всем студентам в рамках курса Python:")
print(all_hw([Student1, Student2], 'Python'))
print("Средняя оценка за домашние задания по всем студентам в рамках курса Git:")
print(all_hw([Student1, Student2], 'Git'))
print("Средняя оценка за домашние задания по всем студентам в рамках курса Введение в программирование:")
print(all_hw([Student1, Student2], 'Введение в программирование'))
print("Средняя оценка за лекции всех лекторов в рамках курса Python:")
print(all_lecturers([Lecturer1, Lecturer2], 'Python'))
print("Средняя оценка за лекции всех лекторов в рамках курса Git:")
print(all_lecturers([Lecturer1, Lecturer2], 'Git'))