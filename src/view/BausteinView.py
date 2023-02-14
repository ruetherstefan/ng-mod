
class BausteinView:

    image_size = 32

    def __init__(self):
        super().__init__()
        self.position_index = None

    def set_position_index(self, position_index):
        self.position_index = position_index

    def get_position_index(self):
        return self.position_index

    def get_position(self):
        return [self.position_index[0] * BausteinView.image_size, self.position_index[1] * BausteinView.image_size]

    def draw(self, screen):
        screen.blit(self.bild, self.get_position())

    def click(self, event):
        pass
