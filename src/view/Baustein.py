
class Baustein:

    image_size = 32
    bilder_ordner = "../../resource/"

    def __init__(self, screen):
        super().__init__()
        self.position_index = None
        self.screen = screen

    def set_position_index(self, position_index):
        self.position_index = position_index

    def get_position_index(self):
        return self.position_index

    def get_position(self):
        return [self.position_index[0] * Baustein.image_size, self.position_index[1] * Baustein.image_size]

    def draw(self):
        self.screen.blit(self.bild, self.get_position())


