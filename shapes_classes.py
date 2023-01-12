"""Classes of shapes."""
import math
import sys


class Shape:
    """Parent class for classes of geometrical shapes."""
    def __init__(self, answer):
        self.answer = answer
        self.name = answer[0].capitalize()

    def get_point(self, point_name):
        """Method to get point coordinates or raise error if coordinates are not numbers."""
        try:
            return (int(self.answer[self.answer.index(point_name)+1]),
                    int(self.answer[self.answer.index(point_name)+2]))
        except ValueError as exc:
            raise ValueError('Coordinates for points have to be integers.') from exc

    def get_points_distance(self, point1, point2):
        """Method to calculate distance between two points."""
        return round(((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2) ** 0.5, 1)

    def get_perimeter(self):
        """Method to calculate shape's perimeter."""
        print('Calculate perimeter.')

    def get_area(self):
        """Method to calculate shape's area."""
        print('Calculate area.')

    def get_output(self):
        """Method to format output for user."""
        output = f'{self.name} Perimeter {self.get_perimeter():.2f} Area {self.get_area():.2f}'
        return output


class Square(Shape):
    """Square class inherites from Shape class."""
    def __init__(self, answer):
        Shape.__init__(self, answer)

        try:
            self.side = int(answer[-1])
        except ValueError as exc:
            raise ValueError('Square side have to be integer.') from exc

        if self.side < 0:
            raise ValueError('Square Side have to be greater or equal to zero.')

        self.top_right = self.get_point('TopRight')

    def get_perimeter(self):
        return self.side * 4

    def get_area(self):
        return self.side ** 2


class Circle(Shape):
    """Circle class inherites from Shape class."""
    def __init__(self, answer):
        Shape.__init__(self, answer)

        try:
            self.radius = int(answer[-1])
        except ValueError as exc:
            raise ValueError('Circle radius have to be integer.') from exc

        if self.radius < 0:
            raise ValueError('Circle Radius have to be greater or equal to zero.')

        self.center = self.get_point('Center')

    def get_perimeter(self):
        return self.radius * 2 * math.pi

    def get_area(self):
        return self.radius ** 2 * math.pi


class Rectangle(Shape):
    """Rectangle class inherites from Shape class."""
    def __init__(self, answer):
        Shape.__init__(self, answer)

        self.top_right = self.get_point('TopRight')
        self.bottom_left = self.get_point('BottomLeft')

        if self.top_right[0] <= self.bottom_left[0] or self.top_right[1] <= self.bottom_left[1]:
            print('TopRight coordinates should be greater than BottomLeft.')

        self.height = self.top_right[1] - self.bottom_left[1]
        self.width = self.top_right[0] - self.bottom_left[0]

    def get_perimeter(self):
        return (self.height + self.width) * 2

    def get_area(self):
        return self.height * self.width


class Triangle(Shape):
    """Triangle class inherites from Shape class."""
    def __init__(self, answer):
        Shape.__init__(self, answer)

        self.points = []
        for point in ['Point1', 'Point2', 'Point3']:
            self.points.append(self.get_point(point))

        if len(set(self.points)) != len(self.points):
            print('Coordinates for points should not be the same.')

        self.side1 = self.get_points_distance(self.points[0], self.points[1])
        self.side2 = self.get_points_distance(self.points[1], self.points[2])
        self.side3 = self.get_points_distance(self.points[2], self.points[0])

    def get_perimeter(self):
        return sum([self.side1, self.side2, self.side3])

    def get_area(self):
        return abs(self.points[0][0] * (self.points[1][1] - self.points[2][1]) +
                    self.points[1][0] * (self.points[2][1] - self.points[0][1]) +
                    self.points[2][0] * (self.points[0][1] - self.points[1][1])) * 0.5
