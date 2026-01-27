#!/usr/bin/env python3


import math


class ft_coordinate_system:
    def __init__(self, x=0, y=None, z=None):
        if isinstance(x, str):
            coords = x.split(',')
            try:
                if (coords.__len__() != 3):
                    raise ValueError("Invalid coordinate string format")
                self.x = int(coords[0])
                self.y = int(coords[1])
                self.z = int(coords[2])
                print(f"Parsed position: ({self.x}, {self.y}, {self.z})")
            except ValueError as ve:
                print(f"Error parsing coordinates: {ve}")
                print(f"Error details - Type: {type(ve)}, Args: {ve.args}")
        else:
            self.x = x
            self.y = y if y is not None else 0
            self.z = z if z is not None else 0
            print(f"Position created: ({self.x}, {self.y}, {self.z})")

    def getPos(self):
        return tuple((self.x, self.y, self.z))

    def distance_from_origin(self):
        res = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        print(f"Distance between (0, 0, 0) and \
({self.x}, {self.y}, {self.z}): {res:.2f}")

    def distance_to(self, other):
        if not isinstance(other, ft_coordinate_system):
            raise ValueError("Argument must be an instance of \
ft_coordinate_system")
        res = math.sqrt((self.x - other.x) ** 2 +
                        (self.y - other.y) ** 2 +
                        (self.z - other.z) ** 2)
        print(f"Distance between ({self.x}, {self.y}, {self.z}) and \
({other.x}, {other.y}, {other.z}): {res:.2f}")
        return res


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    pos1 = ft_coordinate_system(10, 20, 5)
    pos1.distance_from_origin()
    print()

    print("Parsing coordinates: 3,4,0")
    pos2 = ft_coordinate_system("3,4,0")
    pos2.distance_from_origin()
    print()

    print("Parsing invalid coordinates: \"abc,def,ghi\"")
    pos3 = ft_coordinate_system("abc,def,ghi")
    print()

    print("Unpacking demonstration:")
    print("Player at x=3, y=4, z=0")
    x, y, z = pos1.getPos()
    print(f"Coordinates: x={x}, y={y}, z={z}")
