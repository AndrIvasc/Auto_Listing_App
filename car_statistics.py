from sqlalchemy.sql import func
from car import Car


class Statistics:
    def __init__(self, session):
        self.session = session

    def get_statistics(self):
        total_cars = self.session.query(Car).count()
        avg_price = self.session.query(func.avg(Car.price)).scalar()

        min_price_subquery = self.session.query(func.min(Car.price)).scalar_subquery()
        max_price_subquery = self.session.query(func.max(Car.price)).scalar_subquery()

        cheapest_car = self.session.query(Car).filter(Car.price == min_price_subquery).first()
        most_expensive_car = self.session.query(Car).filter(Car.price == max_price_subquery).first()

        return {
            "total_cars": total_cars,
            "avg_price": avg_price,
            "cheapest_car": cheapest_car,
            "most_expensive_car": most_expensive_car,
        }

    def statistics_display(self):
        stats = self.get_statistics()

        print(f"Total Cars: {stats['total_cars']}")
        print(f"Average Price: {stats['avg_price']:.2f}")

        if stats['cheapest_car']:
            print(
                f"Cheapest Car: {stats['cheapest_car'].maker} {stats['cheapest_car'].model} "
                f"({stats['cheapest_car'].year}), Price: {stats['cheapest_car'].price}")
        else:
            print("Cheapest Car: Not available")

        if stats['most_expensive_car']:
            print(
                f"Most Expensive Car: {stats['most_expensive_car'].maker} {stats['most_expensive_car'].model} "
                f"({stats['most_expensive_car'].year}), Price: {stats['most_expensive_car'].price}")
        else:
            print("Most Expensive Car: Not available")
