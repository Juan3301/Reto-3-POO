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
        isinstance(i.item, MainCourse) and i.item.protein_type == "carne"
        for i in self.items
        )

        if has_meat:
            discount += total * 0.05

        return discount
    
    def total_order(self) -> float:
        total = self.subtotal_order() - self.discounts()
        return total
    
    
if __name__ == "__main__":    
    #Ejemplo de pedido (Familia de 3 personas)
    #Mamá:
    bebida_mamá = Drink("limonada", 10000, "mediana", "no alcohol")
    entrada_mamá = Starter("ceviche", 20000, "frio", "pequeño", "cazuela")
    fuerte_mamá = MainCourse("salmón", 50000, "pescado", "esparragos", "grande", 
                            "horno")
    postre_mamá =   Dessert("banana split", 15000, "helado", "dulce", "frio")

    #Papá:
    bebida_papá = Drink("Cerveza", 5000, "mediana", "alcohol")
    entrada_papá = Starter("empanadas", 10000, "caliente", "pequeño", "cazuela")
    fuerte_papá = MainCourse("Lomo", 50000, "carne", "ensalada", "grande", 
                            "parrilla")
    postre_papá =   Dessert("Suzzete", 20000, "crepe", "dulce", "caliente")

    #Hijo:
    bebida_hijo = Drink("Jugo hit", 3500, "mediana", "no-alcohol")
    comida_hijo = Starter("nuggets", 15000, "caliente", "pequeño", "bandeja")
    adicion_hijo = Additional("papas fritas", 6000)

    pedido = Order()
    pedido.add_item(bebida_mamá, 2)
    pedido.add_item(entrada_mamá, 1)
    pedido.add_item(fuerte_mamá, 1)
    pedido.add_item(postre_mamá, 2)
    pedido.add_item(bebida_papá, 3 )
    pedido.add_item(entrada_papá, 1)
    pedido.add_item(fuerte_papá, 1)
    pedido.add_item(postre_papá, 1)
    pedido.add_item(bebida_hijo, 1)
    pedido.add_item(comida_hijo, 2)
    pedido.add_item(adicion_hijo, 1)

    print(pedido.total_order())
        
        
        
    
        