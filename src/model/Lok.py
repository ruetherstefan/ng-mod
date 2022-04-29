class Lok:

    def __init__(self, lokadresse):
        self.adresse: int = lokadresse
        self.speed: int = 0
        self.forwaerts: bool= True
        self.frontlicht: bool = True

        self.f1: bool = False
        self.f2: bool = False
        self.f3: bool = False
        self.f4: bool = False
