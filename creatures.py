class Creatures:
    def __init__(self, name, occupy, speed, deadliness, health, pattern):
        self.name = name
        self.traits = [occupy, speed, deadliness, health, pattern]
        