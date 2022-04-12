class Student:
    def __init__(self, surname, name, second_name, birthday, entry_points, course, group, avg_points, speciality):
        self.surname = surname
        self.name = name
        self.second_name = second_name
        self.birthday = birthday
        self.entry_points = entry_points
        self.course = course
        self.group = group
        self.avg_points = avg_points
        self.speciality = speciality

    def get_data(self):
        name = f'{self.surname} {self.name[0]}.{self.second_name[0]}.'
        return [name, self.birthday, self.speciality, self.course, self.group, self.entry_points, self.avg_points]
