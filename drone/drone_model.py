from box_model import Box

class Drone(Box):
    def __init__(self, x, y, initial_speed, width, height, name):
        super(Drone, self).__init__(x, y, width, height, name)
        self.speed = initial_speed

    def next_up_y(self):
        return self.y - self.speed

    def next_down_y(self):
        return self.y + self.speed

    def next_right_x(self):
        return self.x + self.speed

    def next_left_x(self):
        return self.x - self.speed