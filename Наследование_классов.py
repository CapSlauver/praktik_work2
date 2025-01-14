import math

class Figure:
    sides_count = 0
    def __init__(self, sides, color, filled=False):
       if not isinstance(sides, list):
           raise TypeError("Sides must be a list")

       if len(sides) == 0 or not all(isinstance(side, (int, float)) for side in sides):
            raise ValueError("Sides must be a non-empty list of numbers")

       if len(sides) != self.sides_count and self.sides_count != 0:
             raise ValueError(f"This shape requires {self.sides_count} sides.")

       if not isinstance(color, tuple) or len(color) != 3 or not all(isinstance(c, int) for c in color):
             raise TypeError("Color must be a tuple of 3 integers")
       if not all(0 <= c <= 255 for c in color):
             raise ValueError("Color values must be between 0 and 255")


       self.__sides = sides
       self.__color = color
       self.filled = filled

    def get_color(self):
        return list(self.__color)

    def _is_valid_color(self, r, g, b):
      if not all(isinstance(c, int) for c in (r,g,b)):
            return False
      return all (0<=c<=255 for c in (r,g,b))


    def set_color(self, new_color):
      if not self._is_valid_color(*new_color):
          print (f"New color {new_color} is not valid")
          return
      self.__color = new_color

    def _is_valid_sides(self, sides):
         return all(isinstance(side, (int, float)) for side in sides) and all(side > 0 for side in sides)

    def get_sides(self):
        return list(self.__sides)

    def set_sides(self, new_sides):
      if not isinstance(new_sides, list):
          print(f"New sides {new_sides} is not a valid list")
          return
      if len(new_sides) != self.sides_count and self.sides_count != 0:
         print(f"New sides {new_sides} do not meet the required length.")
         return
      if not self._is_valid_sides(new_sides):
         print(f"New sides {new_sides} are not valid numbers")
         return
      self.__sides = new_sides


    def __len__(self):
        return int(sum(self.__sides))

class Circle(Figure):
    sides_count = 1

    def __init__(self, radius, color, filled=False):
        super().__init__([radius], color, filled)
        self.__radius = radius

    def get_square(self):
      return math.pi * (self.__radius**2)

    def get_radius(self):
       return self.__radius

    def set_radius(self, new_radius):
       if not self._is_valid_sides([new_radius]):
            print (f"New radius {new_radius} is not valid.")
            return
       self.__radius = new_radius
       self.__sides = [new_radius]

    def __len__(self):
       return int(2 * math.pi * self.__radius)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides, color, filled=False):
      super().__init__(sides, color, filled)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, side, color, filled = False):
        super().__init__([side for _ in range(12)], color, filled)

    def get_volume(self):
        side = self.get_sides()[0]
        return side**3


# Code for Checks
circle1 = Circle(10, (200, 100, 10))  # Corrected initialization
cube1 = Cube(6, (222, 35, 130))      # Corrected initialization


# Checking Color
circle1.set_color((55, 66, 77))
print(circle1.get_color())
cube1.set_color((300, 70, 15))
print(cube1.get_color())


# Checking Sides
cube1.set_sides([5, 3, 12, 4, 5, 1, 1, 1, 1, 1, 1, 1]) # Corrected set_sides with list
print(cube1.get_sides())

circle1.set_sides([15]) #Corrected set_sides with list
print(circle1.get_sides())


# Checking Perimeter (Circle)
print(len(circle1))


# Checking volume(Cube)
print(cube1.get_volume())