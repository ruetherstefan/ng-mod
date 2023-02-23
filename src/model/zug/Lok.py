class Lok:

    def __init__(self, lokadresse):
        self.adresse: int = lokadresse
        self.speed: int = 0
        self.forwaerts: bool = True
        self.frontlicht: bool = True

        self.f1: bool = False
        self.f2: bool = False
        self.f3: bool = False
        self.f4: bool = False

    def __eq__(self, other):
        return self.adresse == other.adresse \
               and self.speed == other.speed \
               and self.forwaerts == other.forwaerts \
               and self.frontlicht == other.frontlicht \
               and self.f1 == other.f1 \
               and self.f2 == other.f2 \
               and self.f3 == other.f3 \
               and self.f4 == other.f4
