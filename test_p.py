from pattern import *


def test_car_status_true():
    car_good = Car("TestModel", True)
    assert car_good._Car__is_good is True
def test_car_status_false():
    car_bad = Car("TestModel", False)
    assert car_bad._Car__is_good is False


def test_subscribe():
    car = Car("TestModel")
    driver = Driver("TestDriver")

    car.add_observer(driver)
    assert driver in car.observers
def test_unsubscribe():
    car = Car("TestModel")
    driver = Driver("TestDriver")
    car.add_observer(driver)
    car.remove_observer(driver)
    assert driver not in car.observers