import random
CLOTHES_DICT = {
    "shirt": ["t-shirt", "sweater", "hoodie"],
    "pants": ["jeans", "shorts", "sweatpants"],
    "shoes": ["sneakers", "boots", "sandals"]
}
class Player:
    name = None
    def __init__(self, name):
        self.clothes = [random.choice(CLOTHES_DICT["shirt"]),
        random.choice(CLOTHES_DICT["pants"]),
        random.choice(CLOTHES_DICT["shoes"])]
        self.name = name