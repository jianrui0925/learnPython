class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"This restaurant's name is {self.restaurant_name},it's cuisine type is {self.cuisine_type}.")
    def open_restaurant(self):
            print(f"This restaurant is opening!")

# my_restaurant = Restaurant("MC","fast food")
# print(my_restaurant.restaurant_name+my_restaurant.cuisine_type)
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["苹果","草莓","巧克力"]
    def display_iceCream(self):
        print(self.flavors)
iceHome = IceCreamStand("KFC","fast food")
iceHome.display_iceCream()
