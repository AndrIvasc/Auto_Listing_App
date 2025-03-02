class RepUtility:
    @staticmethod
    def apply_updates(car, maker, model, year, price, mileage, fuel_type, transmission, description):
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
        valid_fuel_types = ["Elektric", "Hybrid", "Petrol", "Mix"]
        while fuel_type not in valid_fuel_types:
            print(f"Invalid fuel type. Please choose one of: {', '.join(valid_fuel_types)}")
            fuel_type = input("Fuel type (Elektric, Hybrid, Petrol, Mix): ").strip()
        return fuel_type

    @staticmethod
    def validate_transmission(transmission):
        valid_transmission_types = ["Manual", "Automatic"]
        while transmission not in valid_transmission_types:
            print(f"Invalid transmission type. Please choose one of: {', '.join(valid_transmission_types)}")
            transmission = input("Transmission type (Manual, Automatic): ").strip()
        return transmission

    @staticmethod
    def convert_input(value, to_type, name):  # Refactered on Saturday
        if value == '':
            return None
        try:
            return to_type(value)
        except ValueError:
            print(f"Invalid {name} input. Please enter a valid {to_type.__name__}.")
            return None
