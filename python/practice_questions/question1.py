# Creating a class Circle
class Circle:
    # Constructor method
    def __init__(self, radius=1 ):
        # Initializing the value
        self.radius = radius
        self.pi = 3.14159

    def area(self):
        """
        Calculates and returns the area of the circle object.

        Args:
        None

        Returns:
        area : float : the area of the circle object
        """
        return self.pi * self.radius **2
    
    def circumference(self):
        """
        Calculates and returns the circumference of the circle object.

        Args:
        None

        Returns:
        area : float : the circumference of the circle object
        """
        return 2 * self.pi * self.radius

if __name__ == "__main__":
    # Initializing a class object with radius 3.7
    my_circle = Circle(3.7)
    # Calling and displaying the results of area and circumference methods
    print(F"The area of circle with radius {my_circle.radius} is {my_circle.area()} unit s.q.")
    print(F"The circumference of circle with radius {my_circle.radius} is {my_circle.circumference()} units.\n\n")

    # Initializing a circle object without radius, so default is 1
    unit_circle = Circle()
    # Calling and displaying the results of area and circumference methods
    print(F"The area of circle with radius {unit_circle.radius} is {unit_circle.area()} unit s.q.")
    print(F"The circumference of circle with radius {unit_circle.radius} is {unit_circle.circumference()} units.")