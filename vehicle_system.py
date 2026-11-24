from abc import ABC, abstractmethod


class Vehicle(ABC):

  @abstractmethod
  def start(self):
    print("Start......")


class Car(Vehicle):

  def start(self):
    print("Car ")


class Bike(Vehicle):

  def start(self):
    print("Bike")


c = Car()
c.start()  # Prints: Car
