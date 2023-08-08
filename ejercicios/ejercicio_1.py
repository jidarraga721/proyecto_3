class Vehículo: 

    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima: float = velocidad_maxima
        self.kilometraje: int = kilometraje


mi_auto = Vehículo(200, 15000)
print("Velocidad máxima:", mi_auto.velocidad_maxima)
print("Kilometraje:", mi_auto.kilometraje)
