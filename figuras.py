import math


def area_circulo(radio):
    return math.pi * radio ** 2


def area_rectangulo(base, altura):
    return base * altura


def area_triangulo(base, altura):
    return base * altura / 2


if __name__ == "__main__":
    print("Circulo:", area_circulo(5))
    print("Rectangulo:", area_rectangulo(4, 3))
    print("Triangulo:", area_triangulo(6, 2))