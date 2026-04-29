class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def total_price(self, quantity: int)-> float:
        return self.price * quantity
    
class Drink(MenuItem):
    def __init__(self, name: str, price: float, size: str, drink_type: str):
        super().__init__(name, price)
        self.size = size
        self.drink_type = drink_type
    
class Starter(MenuItem):
    def __init__(self, name: str, price: float, temperature: str, size: str,
                 presentation: str):
        super().__init__(name, price)
        self.temperature = temperature
        self.size = size
        self.presentation = presentation
        
class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, protein_type: str,
                 side_dish: str, size: str, style: str):
        super().__init__(name, price)
        self.protein_type = protein_type
        self.side_dish = side_dish
        self.size = size
        self.style = style
        
class Dessert(MenuItem):
    def __init__(self, name: str, price: float, dessert_type: str, flavor: str,
                 temperature: str):
        super().__init__(name, price)
        self.dessert_type = dessert_type
        self.flavor = flavor
        self.temperature = temperature
        
class Additional(MenuItem):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)
        
class OrderItem:
    def __init__(self, item: MenuItem, quantity: int):
        self.item = item
        self.quantity = quantity

    def subtotal(self) -> float:
        return self.item.total_price(self.quantity)
    
    
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem, quantity: int):
        self.items.append(OrderItem(item, quantity))

    def subtotal_order(self) -> float:
        subtotal = 0
        for order_item in self.items:
            subtotal += order_item.subtotal()
        return subtotal
    
    def discounts(self) -> float:
        total = self.subtotal_order()
        discount = 0

        has_starter = any(isinstance(i.item, Starter) for i in self.items)
        has_main = any(isinstance(i.item, MainCourse) for i in self.items)
        has_drink = any(isinstance(i.item, Drink) for i in self.items)
        has_dessert = any(isinstance(i.item, Dessert) for i in self.items)

        if has_starter and has_main and has_drink and has_dessert:
            discount += total * 0.10

        total_items = sum(i.quantity for i in self.items)

        if total_items >= 5:
            discount += total * 0.05


        has_meat = any(
        isinstance(i.item, MainCourse) and i.item.protein_type == "meat"
        for i in self.items
        )

        if has_meat:
            discount += total * 0.05

        return discount
    
    def total_order(self) -> float:
        total = self.subtotal_order() - self.discounts()
        return total
    
    
if __name__ == "__main__":    
    #Example with a family three persons
    # Mom
    mom_drink = Drink("Lemonade", 10000, "medium", "non-alcoholic")
    mom_starter = Starter("Ceviche", 20000, "cold", "small", "bowl")
    mom_main = MainCourse("Salmon", 50000, "fish", "asparagus", "large", "oven")
    mom_dessert = Dessert("Banana Split", 15000, "ice cream", "sweet", "cold")

    # Dad
    dad_drink = Drink("Beer", 5000, "medium", "alcoholic")
    dad_starter = Starter("Empanadas", 10000, "hot", "small", "plate")
    dad_main = MainCourse("Steak", 50000, "meat", "salad", "large", "grill")
    dad_dessert = Dessert("Crepe Suzette", 20000, "crepe", "sweet", "hot")

    # Kid
    kid_drink = Drink("Juice", 3500, "medium", "non-alcoholic")
    kid_food = Starter("Nuggets", 15000, "hot", "small", "tray")
    kid_extra = Additional("Fries", 6000)

    order = Order()
    order.add_item(mom_drink, 2)
    order.add_item(mom_starter, 1)
    order.add_item(mom_main, 1)
    order.add_item(mom_dessert, 2)

    order.add_item(dad_drink, 3)
    order.add_item(dad_starter, 1)
    order.add_item(dad_main, 1)
    order.add_item(dad_dessert, 1)

    order.add_item(kid_drink, 1)
    order.add_item(kid_food, 2)
    order.add_item(kid_extra, 1)

    print("Total order:", order.total_order())
        
        
        
    
        