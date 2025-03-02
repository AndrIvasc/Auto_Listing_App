from rep_utility import RepUtility
from car import Car
import inspect


class CarRep:
    def __init__(self, session):
        self.session = session

    def add_car(self):
        maker, model, year, price, mileage, fuel_type, transmission, description = self.input_values()

        car = Car(
            maker=maker,
            model=model,
            year=year,
            price=price,
            mileage=mileage,
            fuel_type=fuel_type,
            transmission=transmission,
            description=description
        )

        self.session.add(car)
        self.session.commit()
        print(f"Car {maker}, {model} added successfully")

    def search_cars(self):
        maker, model, year, price_min, price_max = self.input_values()

        query = self.session.query(Car)
        if maker:
            query = query.filter(Car.maker.ilike(f"%{maker}%"))
        if model:
            query = query.filter(Car.maker.ilike(f"%{model}%"))
        if year:
            query = query.filter(Car.year == year)  # Refactered on Saturday with def convert_input
        if price_min:
            query = query.filter(
                Car.price >= price_min)  # Refactered on Saturday with def convert_input
        if price_max:
            query = query.filter(
                Car.price <= price_max)  # Refactered on Saturday with def convert_input

        cars = query.all()
        RepUtility.print_cars_table(cars)

    def update_car(self):
        car_id = input("Enter car ID you want to update: ")
        car = self.car_id_data(car_id)
        if not car:
            print(f"Car not found with id = {car_id}")
            return

        maker, model, year, price, mileage, fuel_type, transmission, description = self.input_values(car_id)

        updated = RepUtility.apply_updates(car, maker, model, year, price, mileage, fuel_type, transmission,
                                           description)

        if updated:
            self.session.commit()
            print("Car updated successfully")
        else:
            print("No changes were made to the selected car")

    def delete_car(self):
        car_id = input("Enter car ID you want to delete: ")
        car = self.session.query(Car).get(car_id)
        if not car:
            print(f"Car not found with id = {car_id}")
            return

        self.session.delete(car)
        self.session.commit()
        print(f"Car {car.maker} {car.model} deleted successfully!")

    def view_all_cars(self):
        cars = self.session.query(Car).all()
        RepUtility.print_cars_table(cars)

    def input_values(self, car_id=None):
        stack = inspect.stack()
        caller_function = stack[1].function

        if caller_function == 'update_car':
            car = self.car_id_data(car_id)
            maker = input(f"Make ({car.maker}) -> ")
            model = input(f"Model ({car.model}) -> ")
            year = input(f"Year ({car.year}) -> ")
            price = input(f"Price ({car.price}) -> ")
            mileage = input(f"Mileage ({car.mileage}) -> ")

            fuel_type = input(f"Fuel Type ({car.fuel_type}) -> ")
            fuel_type = RepUtility.validate_fuel_type(fuel_type)

            transmission = input(f"Transmission ({car.transmission}) -> ")
            transmission = RepUtility.validate_transmission(transmission)

            description = input(f"Description ({car.description}) -> ")
            return maker, model, year, price, mileage, fuel_type, transmission, description
        elif caller_function == 'search_cars':
            maker = input("Enter the manufacturer to search(leave empty if skip): ")
            model = input("Enter the car model to search(leave empty if skip): ")

            year = input("Enter the car manufacturing year(leave empty if skip): ")
            year = RepUtility.convert_input(year, int, "year")

            price_min = input("Enter the minimum price to search(leave empty if skip): ")
            price_min = RepUtility.convert_input(price_min, float, "minimum price")

            price_max = input("Enter the maximum price to search(leave empty if skip): ")
            price_max = RepUtility.convert_input(price_max, float, "maximum price")

            return maker, model, year, price_min, price_max
        elif caller_function == 'add_car':
            maker = input("Manufacturer: ")
            model = input("Model: ")
            year = input("Manufacturing year: ")
            price = input("Price: ")
            mileage = input("Mileage: ")

            fuel_type = input("Fuel type(Elektric, Hybrid, Petrol, Mix): ")
            fuel_type = RepUtility.validate_fuel_type(fuel_type)

            transmission = input("Transmission type(Manual or Automatic): ")
            transmission = RepUtility.validate_transmission(transmission)

            description = input("Description(optional): ")
            return maker, model, year, price, mileage, fuel_type, transmission, description

    def car_id_data(self, car_id):
        car = self.session.query(Car).get(car_id)
        return car
