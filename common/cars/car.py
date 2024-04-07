# car.py
print("<car.py> executed.")
from .tool import find_tool

__all__ = ['Car', 'find_car']


a = find_tool()

class Car:
    pass


def find_car():
    pass


def helper_car():
    pass


# Execute only if entry point
if __name__ == '__main__':
    print("This is print in car.py")