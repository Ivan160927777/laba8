import random


class Observer:
    def notify(self,car_model:str, message: str):
        pass

class Car:
    __is_good=None
    def __init__(self, model: str, is_good: bool = None):
        self.model = model
        self.__is_good = random.choice([True, False]) if is_good is None else is_good
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def __notify_observers(self, message: str):
        for observer in self.observers:
            observer.notify(self.model, message)

    def drive(self):
        if self.__is_good:
            print(self.model+" едет")
            if random.random()<0.3:
                self.__is_good=False
                self.__notify_observers(" паламалася")
        else:
            print(self.model + " не едет")

class Driver(Observer):
    def __init__(self, name):
        self.name = name

    def notify(self, model: str, message: str):
        print(f"Водитель {self.name} получил уведомление: Автомобиль {model} {message}")

if __name__ == "__main__":
    car = Car("ВАЗ 2107", True)
    driver1=Driver("Владимир")
    driver2=Driver("Елена")
    #car.add_observer(driver1)
    car.add_observer(driver2)
    stop=False
    while not stop:
        car.drive()
        on=input()