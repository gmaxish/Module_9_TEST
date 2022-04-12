"""
Тема 2: “Подключение и использование модулей”
	•	В файлах “AI_students.txt” и “IS_students.txt” содержится информация о студентах, обучающихся по специальностям
“Прикладная информатика” и “Защита информации” соответственно. Каждая строка в указанных файлах содержит информацию об
одном конкретном студенте в следующем формате:
[Фамилия] [Имя] [Отчество] [дата рождения] [балл при поступлении] [курс] [группа] [средний балл]
-Например:
Дмитриев Иван Петрович 12.5.2003 76 1 ПИ-11 4.3
Любимова Мария Ивановка 05.08.2000 98 4 ЗИ-42 5.0

С помощью модуля texttable выведите на экран в виде таблицы информацию о студентах, обучающихся на обеих специальностях,
отсортированную по названию специальности и фамилии студента (внутри каждой специальности) в следующем формате:
Фамилия И.О. | дата рождения | специальность | курс | группа | балл при поступлении | средний балл
"""
import texttable
import Topic_02_1

file_1 = "./Files/AI_Students.txt"
file_2 = "./Files/IS_Students.txt"


class Students:
    def __init__(self, file_name, speciality):
        self.student_list = Students.load_students_file(file_name, speciality)

    @staticmethod
    def load_students_file(file_name, speciality):
        with open(file_name, 'r') as f:
            st_list = f.readlines()
        students = []
        for st in st_list:
            if st.endswith("\n"):
                st = st[:-1]
            surname, name, second_name, birthday, entry_points, course, group, avg_points = st.split()
            students.append(Topic_02_1.Student(surname, name, second_name, birthday, int(entry_points), int(course),
                                               group, float(avg_points), speciality))
        return students

    def sort_by_surname(self):
        self.student_list = sorted(self.student_list, key=lambda st: st.surname)

    def get_students_list(self, sort=False):
        if sort:
            self.sort_by_surname()
        st_list = []
        for st in self.student_list:
            st_list.append(st.get_data())
        return st_list


studentsAI = Students(file_1, "AI")
studentsIS = Students(file_2, "IS")

all_students = studentsAI.get_students_list(sort=True)
all_students.extend(studentsIS.get_students_list(sort=True))

texttable = texttable.Texttable()
texttable.set_cols_align(["l", "c", "c", "c", "c", "c", "c"])
texttable.set_cols_width([18, 10, 15, 5, 6, 15, 12])
texttable.set_precision(1)
headers = ["Ф.И.О", "Дата рождения", "Специальность", "Курс", "Группа", "Балл при поступлении", "Средний балл"]
data = [headers]
data.extend(all_students)
texttable.add_rows(data)
print(texttable.draw())
