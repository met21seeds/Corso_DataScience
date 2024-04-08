class Punto:
    x = 0
    y = 0

    # def stampa_coordinate(self):
    #     print("Le coordinate sono", x, y)

    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        return ((self.x)**2 + (self.y)**2)**0.5

p = Punto()
dx = int(input("Dammi una nuova coordinata x :\n"))
dy = int(input("Dammi una nuova coordinata y :\n"))

p.muovi(dx, dy)  # Muovi le coordinate
#p.stampa_coordinate()  # Stampa le nuove coordinate

distanza = p.distanza_da_origine()  # Calcola la distanza dall'origine
print("La distanza dall'origine è", distanza)


