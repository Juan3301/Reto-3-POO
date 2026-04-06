## Escenario de restaurante.

Se propone un programa que ayuda a calcular la cuenta de un pedido de un cliente en un restaurante.
Para ello se desarrolló un sistema el cual pueda gestionar pedidos en un restaurante. Se definió una clase base `MenuItem`, 
de la cual se heredan diferentes tipos de productos que pueden venir en el menú como `Drink`, `Starter`, `MainCourse`, `Dessert` y `Additional`, 
cada uno con sus respectivos atributos específicos.

En cuanto al manejo de los pedidos, se implementó la clase `Order`, que contiene una lista de ítems (`OrderItem`) 
donde se asocia cada producto con su cantidad. Esta clase permite agregar elementos, calcular el subtotal del pedido y aplicar
descuentos según ciertas condiciones, las cuales fueron la inclusión de un menú completo (entrada, bebida, plato fuerte y postre), 
la cantidad de productos (Si son más de 5), o el tipo de plato, 
que en este programa si el pedido tiene en su plato fuerte carne, se aplicará un descuento.

El sistema finalmente calcula el total a pagar integrando toda la lógica anterior de forma organizada y modular.

El sistema se resume en el siguiente diagrama de clases UML.

## Diagrama de clases.

```mermaid

classDiagram


class MenuItem {
    + name: str
    + price: float
    + total_price() float
}

class Drink {
    + size: str
    + drink_type: str
}

class Starter {
    + temperature: str
    + size: str
    + presentation: str
}

class MainCourse {
    + protein_type: str
    + side_dish: str
    + size: str
    + style: str
}

class Dessert {
    + dessert_type: str
    + flavor: str
    + temperature: str
}

class Additional {
}

%% Relaciones de herencia
MenuItem <|-- Drink
MenuItem <|-- Starter
MenuItem <|-- MainCourse
MenuItem <|-- Dessert
MenuItem <|-- Additional


class OrderItem {
    - item: MenuItem
    - quantity: int
    + subtotal() float
}

OrderItem --> MenuItem


class Order {
    - items: List~OrderItem~
    + add_item()
    + subtotal_order() float
    + discounts() float
    + total_order() float
}

Order *-- OrderItem 
