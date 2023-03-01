class Car:
    """An object representing a normal everyday car"""

    def __init__(self, make: str, model: str, year: int, color: str =None):
        """Initialize attributes to describe a car"""
        self.make = make.lower()
        self.model = model.lower()
        self.year = year

        if color is not None:
            self.color = color.lower()
        else:
            # assume white if no color
            self.color = "white"

        self.odometer = 0
    
    def get_fullname(self) -> str:
        """Returns the full name of this car object"""
        return f"{self.year} {self.make.title()} {self.model.title()}"
    
    def get_odometer(self) -> int:
        """returns the current odometer reading for this car"""
        return self.odometer
    
    def go_fast_noises(self) -> str:
        """makes some cool noises :)"""
        return f"{self.make} {self.model} goes vrooom vroom!"

class ElectricCar(Car):
    """An object representing one of those new fangled 'lectric cars"""

    def __init__(self, make: str, model: str, year: int, color: str =None):
        super().__init__(make, model, year, color=color)

    def go_fast_noises(self) -> str:
        """Makes some electric car noises"""
        return f"{self.make} {self.model} is Silent but deadly :^)"

def sell_car(car: Car, collection: dict, owner: str) -> None:
        if collection[owner] == car:
            print(f"Good bye {car.get_fullname()}")
            del collection[owner]
        else:
            print("You down own that car!")


def main():
    cars = {
        "Elaina": Car("Honda", "Civic", 2004, "Silver"),
        "Brittany" : Car("Nissan", "Rogue", 2016, "Red"),
        "Those Neighbors": ElectricCar("Tesla", "Model S", 2019, "White")
    }

    for owner,car in cars.items():
        print(f"{owner} has a {car.get_fullname()}")
        print(f"{owner}'s {car.go_fast_noises()}")
    
    sell_car(cars["Elaina"], cars, "Elaina")

    for owner,car in cars.items():
        print(f"{owner} -> {car.get_fullname()}")

if __name__ == "__main__":
    main()


