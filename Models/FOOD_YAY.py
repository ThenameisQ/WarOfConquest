class FOOD_YAY:
    def __init__(self, Fatty_index, Shorty_index, Dish, restaurant):
        self.Fatty_index = Fatty_index
        self.Short_index = Shorty_index
        self.Dish = Dish
        self.restaurant = restaurant
    def index_chang(self, neo_fatty_index, Neo_short_index):
        self.Fatty_index = neo_fatty_index
        self.Short_index = Neo_short_index