# pylint: disable=no-member

"""Tests for methods of shapes classes."""
from math import pi
from unittest import TestCase
from shapes_classes import Shape, Square, Circle, Rectangle, Triangle


class TestShape(TestCase):
    """Tests for methods of parent class Shape."""

    def setUp(self):
        answer = 'Rectangle TopRight 2 2 BottomLeft 1 1'.split()
        self.shape = Shape(answer)

    def test_get_point_success(self):
        """Test get point with valid coordinates."""
        actual = self.shape.get_point('TopRight')
        expected = (2, 2)

        self.assertEqual(actual, expected)

    def test_get_point_exception(self):
        """Test get point with invalid coordinates."""
        answer = 'Rectangle TopRight 2 2 BottomLeft a 1'.split()

        with self.assertRaises(ValueError) as exception_context:
            self.shape = Shape(answer)
            self.shape.get_point('BottomLeft')
        self.assertEqual(
            str(exception_context.exception),
            "Coordinates for points have to be integers."
        )

    def test_get_points_distance(self):
        """Test calculate distance between two points."""
        actual = self.shape.get_points_distance((3, 3), (1, 1))
        expected = round(((3 - 1)**2 + (3 - 1)**2)**0.5, 1)

        self.assertEqual(actual, expected)

    def test_get_output(self):
        """Test get output."""
        answer = 'Rectangle TopRight 2 2 BottomLeft 1 1'.split()
        self.shape = Rectangle(answer)

        actual = self.shape.get_output()
        expected = 'Rectangle Perimeter 4.00 Area 1.00'

        self.assertEqual(actual, expected)


class TestSquare(TestCase):
    """Tests for methods of class Square."""

    def setUp(self):
        answer = 'Square TopRight 1 1 Side 1'.split()
        self.square = Square(answer)

    def test_get_perimeter(self):
        """Test calculate square perimeter."""
        self.assertEqual(self.square.get_perimeter(), 4)

    def test_get_area(self):
        """Test calculate square area."""
        self.assertEqual(self.square.get_area(), 1)

    def test_negative_side(self):
        """Test that negative square side raises Value error."""
        answer = 'Square TopRight 1 1 Side -1'.split()

        with self.assertRaises(ValueError) as exception_context:
            self.square = Square(answer)
        self.assertEqual(
            str(exception_context.exception),
            'Square Side have to be greater or equal to zero.'
        )

    def test_zero_side(self):
        """Tets that zero square side is working correctly."""
        answer = 'Square TopRight 1 1 Side 0'.split()
        self.square = Square(answer)

        self.assertEqual(self.square.get_area(), 0)
        self.assertEqual(self.square.get_perimeter(), 0)

    def test_get_side_exception(self):
        """Test get square side with invalid value."""
        answer = 'Square TopRight 1 1 Side d'.split()

        with self.assertRaises(ValueError) as exception_context:
            self.square = Square(answer)
        self.assertEqual(
            str(exception_context.exception),
            "Square side have to be integer."
        )


class TestCircle(TestCase):
    """Tests for methods of class Circle."""

    def setUp(self):
        answer = 'Circle Center 1 1 Radius 3'.split()
        self.circle = Circle(answer)

    def test_get_perimeter(self):
        """Test calculate circle length."""
        self.assertEqual(round(self.circle.get_perimeter(),2), round(2*pi*3,2))

    def test_get_area(self):
        """Test calculate circle area."""
        self.assertEqual(round(self.circle.get_area(),2), round(pi*3**2,2))

    def test_negative_radius(self):
        """Test that negative circle radius raises Value error."""
        answer = 'Circle Center 1 1 Radius -3'.split()

        with self.assertRaises(ValueError) as exception_context:
            self.circle = Circle(answer)
        self.assertEqual(
            str(exception_context.exception),
            'Circle Radius have to be greater or equal to zero.'
        )

    def test_zero_radius(self):
        """Tets that zero circle radius is working correctly."""
        answer = 'Circle Center 1 1 Radius 0'.split()
        self.circle = Circle(answer)

        self.assertEqual(self.circle.get_area(), 0)
        self.assertEqual(self.circle.get_perimeter(), 0)

    def test_get_radius_exception(self):
        """Test get circle radius with invalid value."""
        answer = 'Circle Center 1 1 Radius -'.split()

        with self.assertRaises(ValueError) as exception_context:
            self.circle = Circle(answer)
        self.assertEqual(
            str(exception_context.exception),
            "Circle radius have to be integer."
        )


class TestRectangle(TestCase):
    """Tests for methods of class Rectangle."""

    def setUp(self):
        answer = 'Rectangle TopRight 3 3 BottomLeft 1 1'.split()
        self.rectangle = Rectangle(answer)

    def test_get_perimeter(self):
        """Test calculate rectangle perimeter."""
        self.assertEqual(round(self.rectangle.get_perimeter(),2), 8.00)

    def test_get_area(self):
        """Test calculate rectangle area."""
        self.assertEqual(round(self.rectangle.get_area(),2), 4.00)


class TestTriangle(TestCase):
    """Tests for methods of class Triangle."""

    def setUp(self):
        answer = 'Triangle Point1 3 3 Point2 6 6 Point3 9 3'.split()
        self.triangle = Triangle(answer)

    def test_get_perimeter(self):
        """Test calculate triangle perimeter."""
        self.assertEqual(round(self.triangle.get_perimeter(),2), 14.40)

    def test_get_area(self):
        """Test calculate triangle area."""
        self.assertEqual(round(self.triangle.get_area(),2), 9.00)
