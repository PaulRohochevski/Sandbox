# _*_ coding:utf-8 _*_
"""
Создайте класс который производит легковые автомобили – они будут нам нужны для класса «таксопарк».
Стоимость литра бензина 2,4$, дизеля – 1,8$.
Создайте 100 машин, из которых класс сам будет выпускать каждый третий автомобиль дизельным
(остальные, соответственно, бензиновые), стандартный бензобак будет 60 литров, а каждый пятый авто – с баком
на 75 литров.
Стоимость каждой машины будет 10.000$. Каждая машина должна иметь тахограф (он считает пройденный километраж),
который нельзя сбрасывать/уменьшать.
Максимальный пробег до капремонта бензиновой – 100.000 километров, дизельной – 150.000 км. Пробег без капремонта не
может быть превышен – при попытке это сделать машина должна быть сначала отозвана в СТО и проведен капремонт. Его
стоимость для бензиновой машины 500$, для дизельной – 700$.
Расход топлива у бензиновой – 8 л/100 км, расход дизеля – 6 л/100 км.
Каждая 1.000 км пробега снижает стоимость бензиновой машины на 9.5$, дизельной – на 10.5$, при этом увеличивая расход
топлива на 1%.
Создайте уникальный маршрут случайной длины для каждой машины (от 55.000 до 986.000 км), требуя заправлять полный
бак авто каждый раз, как он опустеет.
- Дайте возможность заменить двигатель на новый, в случае 100% износа, вместо того чтобы отправить машину в утиль.
Стоимость замены пусть будет равна 3000$ для любого типа двигателей, разрешено уводить стоимость машины в минус
(как в кредит, сумма кредитов должны быть подсчитана для всего автопарка).
- Первые 50.000 км. пробега, машины с бензиновым двигателем должны заправляться АИ92 (2.2$/литр), и только
потом – АИ95 (2.4$/литр).
Используйте модуль logging чтобы выводить информацию о пробеге на экран и в файл «cars_report.log»
Машины должны уметь предоставлять сведения о себе:
- пробег    <total_mileage>
- остаточная стоимость  <price>
- сколько было потрачено на топливо за всю поездку  <fuel_cost>
- сколько раз машина заправлялась   <number_of_vehicle_refills>
После пробега отсортируйте машины: дизельные – по остаточной стоимости, бензиновые – по тому сколько им осталось ездить.
Посчитайте суммарную стоимость машин а автопарке после пробега.
"""

import check_python_version
from random import randint


# Класс, который создает легковые автомобили, согласно задания
class Car(object):
    engine_counter = 1
    fuel_tank_counter = 1

    def __init__(self, name):
        self.trip = randint(55000, 286000)
        self.name = name
        self.engine_replacement_cost = 3000
        Engine.engine_type(self)
        Fuel_tank.fuel_tank(self)
        self.odometr
        self.fuel_consumption = self.to_ride()
        self.price = self.reduce_price()
        self.number_of_vehicle_refills = self.refills_number()
        self.fuel_cost = self.total_cost_of_fuel()
        Car.engine_counter += 1
        Car.fuel_tank_counter += 1

    # Позволяет реализовать секьюрный тахограф
    @property
    def odometr(self):
        self.total_mileage = self.total_mileage + self.trip
        return self.total_mileage

    # Увеличивает расход топлива, пересчет происходит на каждой итерации
    def to_ride(self):
        parts_of_trip = self.total_mileage / 1000
        start_fuel_consumption = self.fuel_consumption
        total = 0
        for part in xrange(0, parts_of_trip):
            self.fuel_consumption = start_fuel_consumption * 0.01 + self.fuel_consumption
            total += self.fuel_consumption
        return total / parts_of_trip

    # Снижение стоимости автомобиля
    def reduce_price(self):
        parts_of_trip = self.total_mileage / 1000  # Количество пройденных 1000км
        overhaul_count = self.total_mileage / self.overhaul  # Количество капитальных ремонтов
        price = 10000  # Первоначальная цена автомобиля
        for part in xrange(0, parts_of_trip):
            price -= self.loss_in_price
        for part in xrange(0, overhaul_count):
            price += self.overhaul_cost
        return price  # Стоимость автомобиля после пробега и кап. ремонтов

    # Количество заправок
    def refills_number(self):
        number_of_refills = (self.total_mileage / float((self.fuel_tank * 100) / self.fuel_consumption))
        return int(number_of_refills) + 1

    # Всего потрачено денег на топливо
    def total_cost_of_fuel(self):
        if self.type == "diesel":
            fuel_cost = self.number_of_vehicle_refills * self.fuel_tank * self.diesel_price
        else:
            fuel_cost = self.number_of_vehicle_refills * self.fuel_tank * self.petrol_price
        return fuel_cost


# Дает каждой пятой машине бак на 75 литров, всем остальным на 60
class Fuel_tank(Car):
    @staticmethod
    def fuel_tank(self):
        if not Car.fuel_tank_counter % 5:
            self.fuel_tank = 75
        else:
            self.fuel_tank = 60


# В зависимости от типа ДВС присваиваются соответствующие атрибуты
class Engine(Car):
    @staticmethod
    def engine_type(self):
        if not Car.engine_counter % 3:
            self.type = "diesel"
            self.total_mileage = 0
            self.fuel_consumption = 6
            self.loss_in_price = 10.5
            self.diesel_price = 1.8
            self.overhaul_cost = 700
            self.overhaul = 150000
        else:
            self.type = "petrol"
            self.total_mileage = 0
            self.fuel_consumption = 8
            self.loss_in_price = 9.5
            self.overhaul_cost = 500
            self.overhaul = 100000
            if self.trip <= 50000:
                self.petrol_price = 2.2
            else:
                self.petrol_price = 2.4


car1 = Car("car1")
car2 = Car("car2")
car3 = Car("car3")
car4 = Car("car4")
car5 = Car("car5")

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)
print(car4.__dict__)
print(car5.__dict__)
