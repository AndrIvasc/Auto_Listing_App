from rep_utility import RepUtility
from car import Car
import inspect


class CarRep:
    def __init__(self, session):
        """
        Initializes the CarRep class with a database session.

        :param session: Database session for executing queries.
        """
        self.session = session

    def add_car(self):
        """
        Prompts the user for car details and adds a new car to the database.
        """
        maker, model, year, price, mileage, fuel_type, transmission, description = self.input_values()

        # Create a new Car object
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

        # Save the car to the database
        self.session.add(car)
        self.session.commit()
        print(f"Car {maker}, {model} added successfully")

    def search_cars(self):
        """
        Prompts the user for search criteria and retrieves matching cars from the database.
        """
        maker, model, year, price_min, price_max = self.input_values()

        # Build the search query dynamically based on user input
        query = self.session.query(Car)
        if maker:
            query = query.filter(Car.maker.ilike(f"%{maker}%"))
        if model:
            query = query.filter(Car.maker.ilike(f"%{model}%"))
        if year:
            query = query.filter(Car.year == year)
        if price_min:
            query = query.filter(Car.price >= price_min)
        if price_max:
            query = query.filter(Car.price <= price_max)

        # Fetch and display the results
        cars = query.all()
        RepUtility.print_cars_table(cars)

    def update_car(self):
        """
        Prompts the user for a car ID, retrieves the car, and allows updates.
        If no changes are made, it notifies the user.
        """
        car_id = input("Enter car ID you want to update: ")
        car = self.car_id_data(car_id)
        if not car:
            print(f"Car not found with id = {car_id}")
            return

        # Get new values from the user, keeping existing values as defaults
        maker, model, year, price, mileage, fuel_type, transmission, description = self.input_values(car_id)

        # Apply updates to the car object
        updated = RepUtility.apply_updates(car, maker, model, year, price, mileage, fuel_type, transmission,
                                           description)

        # Commit changes if updates were made
        if updated:
            self.session.commit()
            print("Car updated successfully")
        else:
            print("No changes were made to the selected car")

    def delete_car(self):
        """
        Prompts the user for a car ID and deletes the corresponding car from the database.
        """
        car_id = input("Enter car ID you want to delete: ")
        car = self.session.query(Car).get(car_id)
        if not car:
            print(f"Car not found with id = {car_id}")
            return

        # Delete the car from the database
        self.session.delete(car)
        self.session.commit()
        print(f"Car {car.maker} {car.model} deleted successfully!")

    def view_all_cars(self):
        """
        Retrieves and displays all cars from the database.
        """
        cars = self.session.query(Car).all()
        RepUtility.print_cars_table(cars)

    def input_values(self, car_id=None):
        """
        Prompts the user for car details based on the calling function.

        :param car_id: The ID of the car (used for updating cars).
        :return: Tuple containing car details.
        """
        stack = inspect.stack()
        caller_function = stack[1].function  # Get the function that called input_values

        # If updating a car, show current values as default inputs
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

        # If searching for cars, allow optional criteria
        elif caller_function == 'search_cars':
            maker = input("Enter the manufacturer to search (leave empty to skip): ")
            model = input("Enter the car model to search (leave empty to skip): ")

            year = input("Enter the car manufacturing year (leave empty to skip): ")
            year = RepUtility.convert_input(year, int, "year")

            price_min = input("Enter the minimum price to search (leave empty to skip): ")
            price_min = RepUtility.convert_input(price_min, float, "minimum price")

            price_max = input("Enter the maximum price to search (leave empty to skip): ")
            price_max = RepUtility.convert_input(price_max, float, "maximum price")

            return maker, model, year, price_min, price_max

        # If adding a new car, collect all required fields
        elif caller_function == 'add_car':
            maker = input("Manufacturer: ")
            model = input("Model: ")
            year = input("Manufacturing year: ")
            price = input("Price: ")
            mileage = input("Mileage: ")

            fuel_type = input("Fuel type (Electric, Hybrid, Petrol, Mix): ")
            fuel_type = RepUtility.validate_fuel_type(fuel_type)

            transmission = input("Transmission type (Manual or Automatic): ")
            transmission = RepUtility.validate_transmission(transmission)

            description = input("Description (optional): ")
            return maker, model, year, price, mileage, fuel_type, transmission, description

    def car_id_data(self, car_id):
        """
        Retrieves a car object by its ID from the database.

        :param car_id: The ID of the car to fetch.
        :return: Car object if found, otherwise None.
        """
        car = self.session.query(Car).get(car_id)
        return car
