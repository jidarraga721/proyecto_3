class Carta:
    PINTAS = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

# Crear una carta con valor y pinta específicos


mi_carta = Carta(10, 'Corazones')

print("Valor de la carta:", mi_carta.valor)
print("Pinta de la carta:", mi_carta.pinta)
