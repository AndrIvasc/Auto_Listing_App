from sqlalchemy.sql import func
from car import Car


class Statistics:
    """
    A class for generating statistics about the car listings in the database.

    Attributes:
        session: The SQLAlchemy session used to interact with the database.
    """

    def __init__(self, session):
        """
        Initializes the Statistics class with a database session.

        :param session: Database session for executing queries.
        """
        self.session = session

    def get_statistics(self):
        """
        Retrieves statistics about the car listings, including:
        - Total number of cars
        - Average price of cars
        - The cheapest car
        - The most expensive car

        :return: A dictionary containing the statistics.
        """
        total_cars = self.session.query(Car).count()  # Count total cars
        avg_price = self.session.query(func.avg(Car.price)).scalar()  # Calculate average price

        # Get the minimum and maximum car price using subqueries
        min_price_subquery = self.session.query(func.min(Car.price)).scalar_subquery()
        max_price_subquery = self.session.query(func.max(Car.price)).scalar_subquery()

        # Fetch the cheapest and most expensive cars
        cheapest_car = self.session.query(Car).filter(Car.price == min_price_subquery).first()
        most_expensive_car = self.session.query(Car).filter(Car.price == max_price_subquery).first()

        return {
            "total_cars": total_cars,
            "avg_price": avg_price,
            "cheapest_car": cheapest_car,
            "most_expensive_car": most_expensive_car,
        }

    def statistics_display(self):
        """
        Displays the car statistics in a user-friendly format.
        """
        stats = self.get_statistics()  # Fetch statistics

        print(f"Total Cars: {stats['total_cars']}")
        print(f"Average Price: {stats['avg_price']:.2f}")

        # Display the cheapest car if available
        if stats['cheapest_car']:
            print(
                f"Cheapest Car: {stats['cheapest_car'].maker} {stats['cheapest_car'].model} "
                f"({stats['cheapest_car'].year}), Price: {stats['cheapest_car'].price}")
        else:
            print("Cheapest Car: Not available")

        # Display the most expensive car if available
        if stats['most_expensive_car']:
            print(
                f"Most Expensive Car: {stats['most_expensive_car'].maker} {stats['most_expensive_car'].model} "
                f"({stats['most_expensive_car'].year}), Price: {stats['most_expensive_car'].price}")
        else:
            print("Most Expensive Car: Not available")
