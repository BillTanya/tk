import sys
from figures import *



def handle_figure(figure):
    try:
        if figure[0] == 'Square':
            top_right_x = int(figure[2])
            top_right_y = int(figure[3])
            side = int(figure[-1])
            square = Square(top_right_x, top_right_y, side)
            return f'Square Perimeter {square.perimeter()} Area {square.area()}'
        elif figure[0] == 'Rectangle':
            top_right_x = int(figure[2])
            top_right_y = int(figure[3])
            bottom_left_x = int(figure[-2])
            bottom_left_y = int(figure[-1])
            rectangle = Rectangle(top_right_x, top_right_y, bottom_left_x, bottom_left_y)
            return f'Rectangle Perimeter {rectangle.perimeter()} Area {rectangle.area()}'
        elif figure[0] == 'Circle':
            center_x = int(figure[2])
            center_y = int(figure[3])
            radius = int(figure[-1])
            circle = Circle(center_x, center_y, radius)
            return f'Circle Perimeter {circle.perimeter()} Area {circle.area()}'
        elif figure[0] == 'Triangle':
            point_1_x = int(figure[2])
            point_1_y = int(figure[3])
            point_2_x = int(figure[5])
            point_2_y = int(figure[6])
            point_3_x = int(figure[8])
            point_3_y = int(figure[9])
            triangle = Triangle(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y)
            return f'Triangle Perimeter {triangle.perimeter()} Area {triangle.area()}'
    except ValueError as ec:
        return ec





if __name__ == "__main__":
    input_data = sys.stdin.readlines()
    list_data = [x.split() for x in input_data]

    for figure in list_data:
        handle_figure(figure)



