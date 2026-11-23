VOLUMES = [1, 3, 6, 12, -1]
class Items:
    def __init__(self, name, weight, vol):
        self.name = name
        self.weight = weight #more than 10 cant move out of room, more than 7 cant move out of floor
        self.volume = vol #5, very_small, small, medium, big, massive| 1, 3, 6, 12