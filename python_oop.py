'''chapter 6 py file: oop'''

class Car:
    """class car decleration"""
    runs = True
    wheels = 4

    @classmethod
    def get_wheels(cls):
        ''' get wheels of class default wheels'''
        return cls.wheels

    def start(self):
        """start method of class"""
        if self.runs:
            print("Car is started. Vroom vroom!")
        else:
            print("Car is broken :(")


subaru_car = Car()
print(f"does my car run: {subaru_car.runs}") # does my car run: True
subaru_car.start() # Car Started!! Vrooom`
subaru_car.wheels = 10
print(subaru_car.wheels) # car with instance wheels
print(subaru_car.get_wheels()) # car with default class wheels

my_other_car = Car()
my_other_car.runs = False
my_other_car.start()
