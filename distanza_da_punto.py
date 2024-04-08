class Punto:
    x = 0
    y = 0

    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        return ((self.x)**2 + (self.y)**2)**0.5

p = Punto()
dx = int(input("Dammi una nuova coordinata x :\n"))
dy = int(input("Dammi una nuova coordinata y :\n"))

p.muovi()  # Muovi le coordinate

p.distanza_da_origine()  # Calcola la distanza dall'origine
print("La distanza dall'origine è", p.distanza_da_origine)
