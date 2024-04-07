import common.cars.car

no_print = ['__doc__', '__package__', '__loader__', '__spec__', '__path__', '__file__', '__cached__','__builtins__']

print("\n*** self ****")
for k in dict(globals()).keys():
    if k not in no_print: print(k)

print("\n*** common ****")
for k in common.__dict__.keys():
    if k not in no_print: print(k)

print("\n*** cars package ****")
for k in common.cars.__dict__.keys():
    if k not in no_print: print(k)

print("\n*** car module ****")
for k in common.cars.car.__dict__.keys():
    if k not in no_print: print(k)

# bundle under cars packages
car = common.cars.Car()
car_tool = common.cars.Tool()


