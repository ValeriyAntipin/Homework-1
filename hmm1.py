class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lections(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in self.courses_in_progress and course in lecture.attached_courses:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def avg_rate_hm(self):
        grades_ = []
        for something, grades_list in self.grades.items():
            grades_.extend(grades_list)
        if len(grades_) != 0:
            avg = sum(grades_) / len(grades_)
            return avg
        return 0
    
    def __str__(self) -> str: 
        return f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.avg_rate_hm()}
Курсы в процесе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}
'''
    def __lt__(self, other):
        if (not isinstance(self, Student) or (not isinstance(other, Student))):
            return
        if other.avg_rate_hm() < self.avg_rate_hm():
            print(f'Средняя оценка выше у студента {self.name}') 
        else:
            print(f'Средняя оценка выше у студента {other.name}')



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.attached_courses = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_rate_lections(self):
        grades_ = []
        for something, grades_list in self.grades.items():
            grades_.extend(grades_list)
        if len(grades_) != 0:
            avg = sum(grades_) / len(grades_)
            return avg
        return 0

    def __str__(self) -> str:
        return f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.avg_rate_lections()}
'''
    def __lt__(self, other):
        if (not isinstance(self, Lecturer) or (not isinstance(other, Lecturer))):
            return
        if other.avg_rate_lections() < self.avg_rate_lections():
            print(f'Средняя оценка выше у лектора {self.name}') 
        else:
            print(f'Средняя оценка выше у лектора {other.name}')



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hm(self, student, course, grade):
        if isinstance(student, Student) and course in self.attached_courses and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else: 
                student.grade[course] = [grade]
        else: 
            return 'Ошибка'

    def __str__(self) -> str:
        return f'''
Имя: {self.name}
Фамилия: {self.surname}
'''


#блок студентов
stu1 = Student('Ivan', 'Ivanov', 'man')      
stu1.courses_in_progress += ['python']
stu1.finished_courses += ['git']
stu1.grades['git'] = [10, 10, 10, 10, 10]
stu1.grades['python'] = [10, 10]
stu2 = Student('Alex', 'Alexov', 'man')
stu2.courses_in_progress += ['python']
stu2.finished_courses += ['git']
stu2.grades['git'] = [10, 7, 10, 8, 10]
stu2.grades['python'] = [9, 7]


#блок лекторов
mnt1 = Lecturer('Semen', 'Semenuch')         
mnt1.attached_courses += ['python']
mnt1.grades['python'] = [10, 7, 8 , 5]
mnt2 = Lecturer('Ilya', 'Ilich')
mnt2.attached_courses += ['git']
mnt2.grades['git'] = [10, 10, 10 , 5]


#блок ревьюеров 
mnt3 = Reviewer('Petr', 'Petrov')            
mnt3.rate_hm(stu1, 'python', 10)
mnt4 = Reviewer('Nina', 'Fomina')
mnt4 .rate_hm(stu2, 'git', 7)

students = [stu1, stu2]
lectures = [mnt1, mnt2]


def avg_rate_students(students, course):
    sum_ = 0
    res = 0
    grades_list = []
    for student in students:
        for key, value in student.grades.items():
            if key == course:
                grades_list.extend(value)
    sum_ += sum(grades_list)
    res = round(sum_ / len(grades_list), 2)
    print(f'Средняя оценка по {course}: {res}')


def avg_rate_lectures(lectures, course):
    sum_ = 0
    res = 0
    grades_list = []
    for lecturer in lectures:
        for key, value in lecturer.grades.items():
            if key == course:
                grades_list.extend(value)
    sum_ += sum(grades_list)
    res = round(sum_ / len(grades_list), 2)
    print(f'Средняя оценка по {course}: {res}')

avg_rate_students(students, 'git')
avg_rate_lectures(lectures, 'python')