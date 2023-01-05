"""Script to ask user for input and return output with perimeter and area of given shape."""
from shapes_classes import Square, Circle, Rectangle, Triangle


SHAPES = frozenset((Square, Circle, Rectangle, Triangle))

input_data = input('Write your data: ')
answer = input_data.split()
shape_name = answer[0]

for shape_class in SHAPES:
    if shape_name == shape_class.__name__:
        shape = shape_class(answer)
        if shape.get_area() <= 0 or shape.get_perimeter() <= 0:
            break
        print(shape.get_output())
        break
else:
    print('Your shape is undefined.')
