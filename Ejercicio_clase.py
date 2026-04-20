import numpy as np 

class Point:
    definition: str = (
    "Entidad geometrica abstracta que representa "
    "una ubicacion en un espacio."
)
    def __init__(self, x: float, y: float):
        self.x = x 
        self.y = y
    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y
    def reset(self):
        self.x = 0
        self.y = 0
    def compute_distance(self, point: "Point")-> float:
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance   

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()
    
    def compute_length(self):
        self.length = ((self.start.x - self.end.x)**2 + (self.start.y - self.end.y)**2) ** (0.5)
        return f"La longitud de la linea es {self.length}"
    
    def compute_slope(self):
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        if dx == 0:
            return None # pendiente infinita
        self.slope = np.arctan(dy/dx) * 180/np.pi
        return f"La pendiente de la linea es {self.slope}"
    
    def compute_horizontal_cross(self):
        if self.start.y == 0 or self.end.y == 0:
            return "Si hay intersección con el eje x"
        elif self.start.y < 0 and self.end.y > 0:
            return "Si hay intersección con el eje x"
        elif self.end.y < 0 and self.start.y > 0:
            return "Si hay intersección con el eje x"
        else:
            return "No hay intersección en x"
    
    def compute_vertical_cross(self):
        if self.start.x == 0 or self.end.x == 0:
            return "Si hay intersección con el eje y"
        elif self.start.x < 0 and self.end.x > 0:
            return "Si hay intersección con el eje y"
        elif self.end.x < 0 and self.start.x > 0:
            return "Si hay intersección con el eje y"
        else:
            return "No hay intersección en y"
        

class Rectangle:
    def __init__(self, method: int, p1 = None, p2 = None, width = None, 
        height = None, line1 = None, line2 = None, line3 = None, line4 = None
        ):
        if method == 1: 
            self.width = width
            self.height = height
            self.center = Point(p1.x + width/2, p1.y + height/2)
            
        elif method == 2:
            self.width = width 
            self.height = height
            self.center = p1
            
        elif method == 3:
            self.width = abs(p2.x - p1.x)
            self.height = abs(p2.y - p1.y)
            self.center = Point((p1.x+p2.x)/2, (p1.y+p2.y)/2)
            
        elif method == 4:
            points = [line1.start, line1.end, line2.start, line2.end, 
                      line3.start, line3.end, line4.start, line4.end]
            x_coords = [p.x for p in points]
            y_coords = [p.y for p in points]
            min_x, max_x = min(x_coords), max(x_coords) 
            min_y, max_y = min(y_coords), max(y_coords)
            self.width = max_x - min_x
            self.height = max_y - min_y
            self.center = Point((min_x + max_x) / 2, (min_y + max_y) / 2)
            
    def compute_area(self):
            return f"el area es: {self.width * self.height}"
    def compute_perimeter(self):
            return f"El perimetro es: {(self.width*2)+(self.height*2)}"
            
            
class Square(Rectangle):

    def __init__(self, method, p1, p2, width, height):
        super().__init__(method, p1, p2, width, height)      
        
    def compute_interference_point(self, point):
        xmin = self.center.x - self.width/2
        xmax = self.center.x + self.width/2
        ymin = self.center.y - self.height/2
        ymax = self.center.y + self.height/2

        if xmin <= point.x <= xmax and ymin <= point.y <= ymax:
            print("El punto está dentro del rectángulo")
            return True
        else:
            print("El punto está fuera del rectángulo")
            return False    
                       
            
if __name__ == "__main__":            
            
    #Ejemplo de uso con creación de objetos. El mismo rectangulo de las 4 maneras 
    #posibles de inicializar

    lin1 = Line(Point(0,0),Point(2,0))
    lin2 = Line(Point(2,0),Point(2,4))
    lin3 = Line(Point(2,4),Point(0,4))
    lin4 = Line(Point(0,4),Point(0,0))
    
    rec1 = Rectangle(method = 1, p1 = Point(0,0), width = 2, height = 4)
    rec2 = Rectangle(method = 2, p1 = Point(1,2), width = 2, height = 4)
    rec3 = Rectangle(method = 3, p1 = Point(0,0), p2 = Point(2,4))
    rec4 = Rectangle(method = 4, line1 = lin1, line2 = lin2, line3 = lin3, 
                    line4 = lin4)
    
    print(rec1.compute_area())
    print(rec2.compute_area())
    print(rec3.compute_area())
    print(rec4.compute_area())

    print(rec1.compute_perimeter())
    print(rec2.compute_perimeter())
    print(rec3.compute_perimeter())
    print(rec4.compute_perimeter()) #Deberia devolver el mismo área y perimetro de los rectangulos.

    print(lin1.compute_length()) #2
    print(lin2.compute_length()) #4
    print(lin3.compute_length()) #2
    print(lin4.compute_length()) #4 

    print(lin1.compute_slope())
    print(lin2.compute_slope())
    print(lin3.compute_slope())
    print(lin4.compute_slope())  #0 lineas horizontales, None lineas verticales.

    print(lin1.compute_horizontal_cross())
    print(lin2.compute_horizontal_cross())
    print(lin3.compute_horizontal_cross())
    print(lin4.compute_horizontal_cross()) # Solo la linea de arriba (line3) no interseca

    print(lin1.compute_vertical_cross())
    print(lin2.compute_vertical_cross())
    print(lin3.compute_vertical_cross())
    print(lin4.compute_vertical_cross()) # Solo (line2) no interseca.
