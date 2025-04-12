class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def info(self):
        print(f"- brand: {self.brand}")
        print(f"  model: {self.model}")
        print(f"  year: {self.year}")
        print(f"  mileage: {self.mileage} км")

    def drive(self, km):
        self.mileage = self.mileage + km

    def is_old(self):
        return self.year < 2015

class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def drive_all(self, km):
        for car in self.cars:
            car.drive(km)

    def show_all(self):
        for car in self.cars:
            car.info()

    def show_old_cars(self):
        for car in self.cars:
            if car.is_old():
                car.info()

c1 = Car(brand="Honda", model="Civic", year=2012, mileage=110000)
c2 = Car(brand="Mercedes-Benz", model="C-Class", year=2016, mileage=60000)

garage = Garage()
garage.add_car(c1)
garage.add_car(c2)

print("〖УСІ МАШИНИ〗:")
garage.show_all()

print("             ")
print("------------------")
print("〖СТАРІ МАШИНИ〗:")
garage.show_old_cars()