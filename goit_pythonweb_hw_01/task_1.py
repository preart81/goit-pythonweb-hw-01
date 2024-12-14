"""
Модуль з класом Vehicle, що описує транспортний засіб.

Клас Vehicle є абстрактним класом, що описує транспортний засіб.
Він має атрибути make та model, та абстрактний метод start_engine,
який повинний бути реалізований у класах-нащадках.
"""

from abc import ABC, abstractmethod
import logging

# налаштування логування
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)


# todo 1.Створити абстрактний базовий клас Vehicle з методом start_engine().
class Vehicle(ABC):
    """
    Абстрактний клас, що описує транспортний засіб.

    Він має атрибути make та model, та абстрактний метод start_engine,
    який повинен бути реалізований у класах-нащадках.
    """

    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        """Абстрактний метод, що повинен бути реалізований у класах-нащадках."""


# todo 2.Змінити класи Car та Motorcycle, щоб вони успадковувались від Vehicle.
class Car(Vehicle):
    """Клас, що описує автомобіль."""

    def start_engine(self) -> None:
        logging.info("%s %s: Двигун запущено", self.make, self.model)


class Motorcycle(Vehicle):
    """Клас, що описує мотоцикл."""

    def start_engine(self) -> None:
        logging.info("%s %s: Мотор заведено", self.make, self.model)


# todo 3.Створити абстрактний клас VehicleFactory з методами create_car() та create_motorcycle().
class VehicleFactory(ABC):
    """Абстрактна фабрика, що створює транспортні засоби."""

    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        """Абстрактний метод, що повинен бути реалізований у класах-нащадках."""

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        """Абстрактний метод, що повинен бути реалізований у класах-нащадках."""


# todo 4.Реалізувати два класи фабрики: USVehicleFactory та EUVehicleFactory. Ці фабрики повинні створювати автомобілі та мотоцикли з позначкою регіону наприклад, Ford Mustang (US Spec) відповідно для США.
class USVehicleFactory(VehicleFactory):
    """Фабрика для США."""

    region_code = "(US Spec)"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, " ".join([model, self.region_code]))

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, " ".join([model, self.region_code]))


class EUVehicleFactory(VehicleFactory):
    """Фабрика для ЄС."""

    region_code = "(EU Spec)"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, " ".join([model, self.region_code]))

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, " ".join([model, self.region_code]))


if __name__ == "__main__":
    # Використання
    logging.info("# --------- Використання без фабрики: ---------")
    vehicle1 = Car("Toyota", "Corolla")
    vehicle1.start_engine()

    vehicle2 = Motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()

    # todo 5.Змініть початковий код так, щоб він використовував фабрики для створення транспортних засобів.
    logging.info("# --------- Використання з фабриками: ---------")
    us_factory = USVehicleFactory()
    us_car = us_factory.create_car("Ford", "Mustang")
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    us_car.start_engine()
    us_motorcycle.start_engine()

    eu_factory = EUVehicleFactory()
    eu_car = eu_factory.create_car("Volvo", "V40")
    eu_motorcycle = eu_factory.create_motorcycle("BMW", "R1200GS")
    eu_car.start_engine()
    eu_motorcycle.start_engine()

    eu_car_2 = USVehicleFactory().create_car("Volvo", "V90")
    eu_motorcycle_2 = USVehicleFactory().create_motorcycle("BMW", "S1000R")
    eu_car_2.start_engine()
    eu_motorcycle_2.start_engine()
