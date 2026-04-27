from CarClasses import Cars

Car1 = Cars("Ford", "EcoSport", 2022, "unleaded", -9999, 4, False, False)
Car2 = Cars("Toyota", "Corolla", 2024, "unleaded", -9999, 3, False, True)

def print_car(car):
    print(f"{car.make} {car.model} {car.year} {car.type} {car.mpg} {car.cylinder} {car.turbo} {car.hybrid}")

print_car(Car1)
print_car(Car2)