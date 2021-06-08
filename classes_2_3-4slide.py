# 1)Student
# Создайте класс Student, конструктор которого имеет параметры name, lastname,
# department, year_of_entrance. Добавьте метод get_student_info, который
# возвращает имя, фамилию, год поступления и факультет в
# отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:
# Программирование.”

class Student:
    def __init__(self, name, lastname, department, entrance_year):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = entrance_year

    def get_student_info(self):
        return f"{self.name} {self.lastname} поступил в {self.year_of_entrance} г. на факультет: {self.department}"


Vasyok = Student('Vazya', 'Pupkin', 'Программная инженерия', 2013)

print(Vasyok.get_student_info())

# 2)Airplane
# Создайте новый класс Airplane. Создайте следующие характеристики (полей)
# объекта:
# ● make (марка)
# ● model
# ● year
# ● max_speed
# ● odometer
# ● is_flying
# и методы имитирующих поведение самолета take off (взлет), fly (летать), land
# приземление). Метод take off должен изменить is_flying на True, а land на False. По
# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте
# все методы класса.


class Airplane:
    def __init__(self):
        self.make = ''
        self.model = ''
        self.year = 0
        self.max_speed = 9999
        self.odometer = 0
        self.is_flying = False

    def take_off(self):
        self.is_flying = True

    def fly(self, spatium):
        if self.is_flying:
            self.odometer += spatium

    def land(self):
        self.is_flying = False


Kukuruznik = Airplane()
Kukuruznik.take_off()
Kukuruznik.fly(777)
Kukuruznik.fly(69)
Kukuruznik.land()
Kukuruznik.fly(69)

print(Kukuruznik.odometer)
