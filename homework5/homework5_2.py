import datetime

class Room:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def square(self):
        self.square = self.side1 * self.side2

    def perimeter(self):
        self.perimeter = (self.side1 + self.side2) * 2

    def __str__(self):
        return f"Room with side1  {self.side1}, side2 {self.side2}, square {self.square}, perimeter {self.perimeter}"


r1 = Room(5, 6)
r1.square()
r1.perimeter()
print(r1.square)
print(r1.perimeter)
print(r1)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_null(self):
        self.dist_to_null = ((self.x - 0) ** 2 + (self.y - 0) ** 2) ** (1 / 2)

    def distance_between_2points(self, x2, y2):
        self.dist_btwn_2points = ((self.x - x2) ** 2 + (self.y - y2) ** 2) ** (1 / 2)

    def change_coord_system(self, a):
        new_x = a[0][0] * self.x + a[0][1] * self.y
        new_y = a[1][0] * self.x + a[1][1] * self.y
        return new_x, new_y

    def __str__(self):
        return f"Point with x  {self.x}, y {self.y}, distance to 0:0 {self.dist_to_null}"


point1 = Point(3, 5)
point1.distance_to_null()
point2 = Point(4, 7)
point1.distance_between_2points(point2.x, point2.y)
print(point1.dist_to_null)
print(point1.dist_btwn_2points)
matr_A = [[5, 6], [1, -2]]
new_point = point1.change_coord_system(matr_A)
print(new_point)
print(point1)


class Student:
    def __init__(self, full_name, specialty, intro_year, list_of_rates):
        self.full_name = full_name
        self.speciality = specialty
        self.intro_year = intro_year
        self.list_of_rates = [list_of_rates]

    def add_rate(self, rate):
        self.list_of_rates.append(rate)

    def get_avg_rate(self):
        total_rate = 0
        for i in self.list_of_rates:
            total_rate += i
        self.avg_rate = total_rate/len(self.list_of_rates)
        return self.avg_rate

    def how_many_year(self):
        now = datetime.datetime.now()
        return now.year - self.intro_year

    def __str__(self):
        return f"Student with full name  {self.full_name}, speciality {self.speciality}, into year - {self.intro_year}, list of rates {self.list_of_rates}, avg rate {self.avg_rate}"


stud1 = Student("Vasya Pupkin", "economist", 2016, 5)
stud1.add_rate(4)
stud1.add_rate(4)
stud1.add_rate(2)
print(stud1.get_avg_rate())
print(stud1.how_many_year())
print(stud1.list_of_rates)
print(stud1)