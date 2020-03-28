import datetime

class Person:
    def __init__(self, full_name, birth_year):
        self.full_name = full_name
        self.birth_year = birth_year
        if len(self.full_name.split(" "))<2:
            raise NameError ("Check name")
        if 1900>birth_year or birth_year>2019:
            raise NameError("Check year")


    def get_name(self):
        x = self.full_name.find(" ")
        self.name = self.full_name[:x]
        return self.name


    def get_surname(self):
        x = self.full_name.find(" ")
        self.surname = self.full_name[x+1:]
        return self.surname

    def get_age_in_year(self, y=None):
        if y is None:
            y = datetime.datetime.now().year
        if y<self.birth_year:
            return "Person was not born yet!"
        else:
             self.age = y - self.birth_year
             return self.age

    def __str__(self):
        return f"Person with fulname  {self.full_name}, name {self.name}, surname {self.surname}, year of birthday {self.birth_year}"


a = Person("Vasya Pupkin", 1985)
print(a.get_name())
print(a.get_surname())
#print(a.get_age_in_year())
print(a)


class Employee(Person):
    def __init__(self, full_name, birth_year, position, experience, salary):
        Person.__init__(self, full_name, birth_year)
        self.position = position
        self.experience = experience
        self.salary = salary
        if experience < 0 or salary < 0:
            raise NameError("This person cannot work in our company")

    def checking_position(self):
        if self.experience < 3:
            return "Junior " + self.position
        elif 3 <= self.experience < 6:
            return "Middle " + self.position
        else:
            return "Senior " + self.position

    def raise_salary(self, add_to_salary):
        self.salary += add_to_salary
        return self.salary

    def __str__(self):
        return f"Person with fulname  {self.full_name},  year of birthday {self.birth_year}, position {self.position}, " \
               f"salary {self.salary}, experience {self.experience}"


z = Employee("Nata Test", 1985, "QA", 6, 2500)
print(z.checking_position())
z.raise_salary(500)
print(z.salary)
print(z)


class ITEmployee(Employee):
    def __init__(self, full_name, birth_year, position, experience, salary, skills=None):
        Employee.__init__(self, full_name, birth_year, position, experience, salary)
        if skills is None:
            self.skills = []
        else:
            self.skills = skills


    def add_skill(self, skill):
        self.skills.append(skill)

    def add_skills(self, *skills):
        for i in skills:
            self.skills.append(i)

    def __str__(self):
        return f"Person with fullname  {self.full_name},  year of birthday {self.birth_year}, position {self.position}, salary {self.salary}, experience {self.experience}"


it_empl = ITEmployee("Nata Titiu", 1985, "Engineer", 5, 1500)
it_empl.add_skill("aaaa")
it_empl.add_skill("adsad")
it_empl.add_skills("a few", "sdasd", "sds")
print (it_empl)
