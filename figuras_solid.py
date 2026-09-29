from abc import ABC, abstractmethod
import math


class Figura(ABC):
    @abstractmethod
    def area(self):
        pass


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2


class CalculadoraAreas:
    def total(self, figuras):
        return sum(figura.area() for figura in figuras)


if __name__ == "__main__":
    figuras = [Circulo(5), Rectangulo(4, 3), Triangulo(6, 2)]
    for figura in figuras:
        print(type(figura).__name__, figura.area())
    print("Total:", CalculadoraAreas().total(figuras))