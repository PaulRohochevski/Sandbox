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
Создайте уникальный маршрут случайной длины для каждой машины (от 55.000 до 286.000 км), требуя заправлять полный
бак авто каждый раз, как он опустеет.
Машины должны уметь предоставлять сведения о себе:
- пробег    <tachograph>
- остаточная стоимость  <price>
- сколько было потрачено на топливо за всю поездку
- сколько раз машина заправлялась   <number_of_vehicle_refills>
- сколько осталось пробега до утилизации
После пробега отсортируйте машины: дизельные – по остаточной стоимости, бензиновые – по тому сколько им осталось ездить.
Посчитайте суммарную стоимость машин а автопарке после пробега.
"""

import check_python_version


# Класс, который создает легковые автомобили, согласно задания
class Car(object):
    from random import randint
    engine_counter = 1
    fuel_tank_counter = 1

    def __init__(self, name):
        self.name = name
        self.tachograph = self.odometr
        self.engine(Car.engine_counter)
        self.fuel_tank(Car.fuel_tank_counter)
        self.number_of_vehicle_refills = self.number_of_vehicle_refills()
        self.price = self.mileage()
        self.fuel_consumption = self.general_fuel_cost()
        self.total_cost_of_fuel = self.total_cost_of_fuel()
        Car.engine_counter += 1
        Car.fuel_tank_counter += 1

    # В зависимости от типа ДВС присваиваются соответствующие атрибуты
    def engine(self, engine_counter):
        if engine_counter % 3 == 0:
            self.engine = "diesel"
            self.fuel_consumption = 6
            self.loss_in_price = 10.5
            self.fuel_cost = 1.8
            self.overhaul_cost = 700
            self.overhaul = 150000
        else:
            self.engine = "petrol"
            self.fuel_consumption = 8
            self.loss_in_price = 9.5
            self.fuel_cost = 2.4
            self.overhaul_cost = 500
            self.overhaul = 100000

    # Дает каждой пятой машине бак на 75 литров, всем остальным на 60
    def fuel_tank(self, fuel_tank_counter):
        if fuel_tank_counter % 5 == 0:
            self.fuel_tank = 75
        else:
            self.fuel_tank = 60

    # Позволяет реализовать секьюрный тахограф
    @property
    def odometr(self):
        return Car.randint(55000, 286000)

    # Снижение стоимости автомобиля
    def mileage(self):
        factor = self.tachograph / 1000  # Количество пройденных 1000км
        price = 10000 - (self.loss_in_price * factor)  # Стоимость автомобиля после пробега
        factor2 = self.tachograph / self.overhaul  # Количество капитальных ремонтов
        self.price = price - (self.overhaul_cost * factor2)  # Стоимость автомобиля после пробега и кап. ремонтов
        return self.price

    # Расход топлива
    def general_fuel_cost(self):
        factor = self.tachograph / 1000
        factor2 = 0.01 * factor + 1  # Коэффициент увеличения расхода топлива
        self.fuel_consumption = self.fuel_consumption * factor2
        return self.fuel_consumption

    # Количество заправок
    def number_of_vehicle_refills(self):
        self.number_of_vehicle_refills = (self.tachograph / float((self.fuel_tank * 100) / self.fuel_consumption))
        return self.number_of_vehicle_refills

    # Всего потрачено денег на топливо
    def total_cost_of_fuel(self):
        self.total_cost_of_fuel = self.number_of_vehicle_refills * self.fuel_tank * self.fuel_cost
        return self.total_cost_of_fuel


# car1 = Car("car1")
# car2 = Car("car2")
# car3 = Car("car3")
# car4 = Car("car4")
# car5 = Car("car5")
#
# print (car1.__dict__)
# print (car2.__dict__)
# print (car3.__dict__)
# print (car4.__dict__)
# print (car5.__dict__)
