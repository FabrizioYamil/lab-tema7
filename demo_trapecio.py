from figuras_solid import Figura, Circulo, Rectangulo, Triangulo, CalculadoraAreas


class Trapecio(Figura):
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def area(self):
        return (self.base_mayor + self.base_menor) * self.altura / 2


figuras = [Circulo(5), Rectangulo(4, 3), Triangulo(6, 2), Trapecio(6, 4, 3)]
for figura in figuras:
    print(type(figura).__name__, figura.area())
print("Total con trapecio:", CalculadoraAreas().total(figuras))