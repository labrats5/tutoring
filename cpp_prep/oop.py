from __future__ import annotations
from enum import Enum
from random import randint
import platform

class Gender(Enum):
    MALE = 1
    FEMALE = 2

    @classmethod
    def random(cls):
        return cls(randint(1, 2))


class Animal:
    def __init__(self, name: str, weight: float, gender: Gender):
        self.name: str = name
        self.weight: float = weight
        self.__gender: Gender = gender

    def __del__(self):
        print('Destructor called, Animal deleted.')

    def getGender(self) -> Gender:
        return self.__gender

    def makeSound(self):
        print("animal sound")

    @staticmethod
    def compareWeight(a: Animal, b: Animal):
        if a.weight < b.weight:
            return -1
        elif a.weight > b.weight:
            return 1
        else:
            return 0


class Bird(Animal):
    def __init__(self, name: str, weight: float, gender: Gender, wingspan: float):
        self.wingspan: float = wingspan
        super().__init__(name, weight, gender)

    def makeSound(self):
        print("tweet!")

    @classmethod
    def parrot(cls):
        return cls("parrot", 0.5, Gender.random(), 34.0)

    @classmethod
    def pidgeon(cls):
        return cls("pidgeon", 5.6, Gender.random(), 45.0)

    @staticmethod
    def compareWingspan(a: Bird, b: Bird):
        if a.wingspan < b.wingspan:
            return -1
        elif a.wingspan > b.wingspan:
            return 1
        else:
            return 0


class Hen(Bird):
    def __init__(self, name, weight, wingspan):
        super().__init__(name, weight, Gender.FEMALE, wingspan)

    def layEgg(self, babyWeight, babyWingspan):
        return Bird(self.name, babyWeight, Gender.random(), babyWingspan)

    @classmethod
    def fromBird(cls, bird: Bird):
        return cls(bird.name, bird.weight, bird.wingspan)

    @classmethod
    def parrot(cls):
        return cls.fromBird(Bird.parrot())

    @classmethod
    def pidgeon(cls):
        return cls.fromBird(Bird.pidgeon())


print(platform.system(),
      platform.platform(),
      platform.release(),
      platform.mac_ver(),
      platform.architecture())

# print(Gender.random())

# p = Hen.parrot()
# p.makeSound()
# print(p.weight)
# parrot = Bird.parrot()
# pidgeon = Animal("pidgeon", 5.6, Gender.FEMALE)
# print(parrot.getGender())
# print(Animal.compareWeight(parrot, pidgeon))
