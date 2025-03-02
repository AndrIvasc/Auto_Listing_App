class RepUtility:
    """
    A utility class for handling car data operations such as updating records, displaying cars,
    validating inputs, and converting input values.
    """

    @staticmethod
    def apply_updates(car, maker, model, year, price, mileage, fuel_type, transmission, description):
        """
        Updates the given car's attributes with new values if they are provided and different from the existing ones.

        :param car: The car object to update.
        :param maker: New maker name (or None if unchanged).
        :param model: New model name (or None if unchanged).
        :param year: New manufacturing year (or None if unchanged).
        :param price: New price (or None if unchanged).
        :param mileage: New mileage (or None if unchanged).
        :param fuel_type: New fuel type (or None if unchanged).
        :param transmission: New transmission type (or None if unchanged).
        :param description: New description (or None if unchanged).
        :return: True if any update was made, otherwise False.
        """
        updated = False

        if maker and maker != car.maker:
            car.maker = maker
            updated = True
        if model and model != car.model:
            car.model = model
            updated = True
        if year and int(year) != car.year:
            car.year = int(year)
            updated = True
        if price and float(price) != car.price:
            car.price = float(price)
            updated = True
        if mileage and float(mileage) != car.mileage:
            car.mileage = float(mileage)
            updated = True
        if fuel_type and fuel_type != car.fuel_type:
            car.fuel_type = fuel_type
            updated = True
        if transmission and transmission != car.transmission:
            car.transmission = transmission
            updated = True
        if description and description != car.description:
            car.description = description
            updated = True

        return updated

    @staticmethod
    def print_cars_table(cars):
        """
        Prints a formatted table of cars.

        :param cars: A list of car objects to display.
        """
        if not cars:
            print("No cars available.")
            return

        print(
            f"{'ID':<5} {'Maker':<15} {'Model':<15} {'Year':<6} "
            f"{'Price':<10} {'Mileage':<10} {'Fuel Type':<12} {'Transmission':<12}")
        print("-" * 85)

        for car in cars:
            print(
                f"{car.id:<5} {car.maker:<15} {car.model:<15} {car.year:<6} "
                f"{car.price:<10.2f} {car.mileage:<10.2f} {car.fuel_type:<12} {car.transmission:<12}")

    @staticmethod
    def validate_fuel_type(fuel_type):
        """
        Validates and ensures the fuel type is correct.

        :param fuel_type: The fuel type input by the user.
        :return: A valid fuel type.
        """
        valid_fuel_types = ["Elektric", "Hybrid", "Petrol", "Mix"]
        while fuel_type not in valid_fuel_types:
            print(f"Invalid fuel type. Please choose one of: {', '.join(valid_fuel_types)}")
            fuel_type = input("Fuel type (Elektric, Hybrid, Petrol, Mix): ").strip()
        return fuel_type

    @staticmethod
    def validate_transmission(transmission):
        """
        Validates and ensures the transmission type is correct.

        :param transmission: The transmission type input by the user.
        :return: A valid transmission type.
        """
        valid_transmission_types = ["Manual", "Automatic"]
        while transmission not in valid_transmission_types:
            print(f"Invalid transmission type. Please choose one of: {', '.join(valid_transmission_types)}")
            transmission = input("Transmission type (Manual, Automatic): ").strip()
        return transmission

    @staticmethod
    def convert_input(value, to_type, name):
        """
        Converts user input to the specified data type, handling invalid cases.

        :param value: The user input value.
        :param to_type: The type to convert to (e.g., int, float).
        :param name: The name of the field (for error messages).
        :return: The converted value or None if invalid.
        """
        if value == '':
            return None
        try:
            return to_type(value)
        except ValueError:
            print(f"Invalid {name} input. Please enter a valid {to_type.__name__}.")
            return None
