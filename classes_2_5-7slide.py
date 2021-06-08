# 3)Car
# Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
# odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
# а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
# самом начале проверьте, хватит ли вам бензина из расчета того, что машина
# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
# то пусть этот метод добавляет эти километры к значению одометра, но не
# напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
# drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
# more!”
class Car:
    # , make, model, year, odometer, fuel
    def __init__(self):
        self.make = ''
        self.model = ''
        self.year = ''
        self.odometer = 0
        self.fuel = 70

    def __add_distance(self, distance):
        self.odometer += distance

    def __subtract_fuel(self, distance):
        self.fuel -= distance / 10

    def drive(self, distance):
        if self.fuel * 10 >= distance:
            print("Let’s drive!")
            self.__add_distance(distance)
            self.__subtract_fuel(distance)
        else:
            print("Need more fuel, please, fill more!")


BMW = Car()
BMW.drive(1000)
BMW.drive(696)
BMW.drive(10)

# 4)ContactList
# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Замените all_contacts = [ ] на all_contacts =
# ContactList(). Создайте несколько контактов, используйте метод
# search_by_name.


class ContactList(list):
    def search_by_name(self, name):
        result = []
        for i in self:
            if i == name:
                result.append(i)
        return result


all_contacts = ContactList()
all_contacts += ['Vasya', 'Petya', 'Erbol', 'Nurdoolot', 'Apolinarij']
all_contacts.append('Vasya')
print(all_contacts)
print(all_contacts.search_by_name('Vasya'))

# 5)AK-47
# Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)
# Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.
# Where soldier will fire from a gun and reload, and fire one more time.


class AK47:

    def fire(self):
        print('tigi-tigitishh')
