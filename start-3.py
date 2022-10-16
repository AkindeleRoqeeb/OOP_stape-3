################################### give a datatype ########################################################

class item:
    def __init__(self, name: str, price: float, quantity: float, quality=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.quality = quality
    def calculate_total_price(self):
        return self.price * self.quality

########################################################### notice the int that is use as str ##########################
item1 = item('laptop', 300, 3, 2)
item2 = item('phone', 100, 43, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

############################################### checking for reguirement #################################################

class item:
    def __init__(self, name: str, price: float, quantity: float, quality=0):
        ############### run validation to the recieve argument ######################
        # assert price >= 0
        ##################### OR ###############
        assert price >= 0, f"price {price} is not greater or equal zero"

        # assert quality >= 0
        ##################### OR ###############
        assert quality >= 0, f"quality {quality} is not greater or equal zero"

        self.name = name
        self.price = price
        self.quantity = quantity
        self.quality = quality

    ############## Asign to self object ############################
    def calculate_total_price(self):
        return self.price * self.quality

########################################################### notice the int that is use as str ##########################
# item1 = item('laptop', 300, 3, -2)
item1 = item('laptop', 300, 3, 2)
item2 = item('phone', 100, 43, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
