import forges

class TopViewController(forges.Entity):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.window = forges.forges.get_window()

        self.speed = 3
        self.sprint_speed = 6

        for i in kwargs:
            setattr(self, i, kwargs[i])

        self.target_speed = self.speed

    def update(self):
        if self.window.input.key_pressed(self.window.keys["LSHIFT"]):
            self.target_speed = self.sprint_speed

        else:
            self.target_speed = self.speed

        if self.window.input.key_pressed(self.window.keys["S"]):
            self.y += self.target_speed

        if self.window.input.key_pressed(self.window.keys["W"]):
            self.y -= self.target_speed

        if self.window.input.key_pressed(self.window.keys["D"]):
            self.x += self.target_speed

        if self.window.input.key_pressed(self.window.keys["A"]):
            self.x -= self.target_speed