from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Car(Base):
    """
        Represents a car in the database.

        Attributes:
            id (int): Unique identifier for each car (Primary Key).
            maker (str): The manufacturer of the car (e.g., Toyota, Ford).
            model (str): The model name of the car (e.g., Corolla, Mustang).
            year (int): The manufacturing year of the car.
            price (float): The price of the car.
            mileage (float): The mileage of the car in kilometers or miles.
            fuel_type (str): The type of fuel the car uses (e.g., Petrol, Diesel, Electric).
            transmission (str): The type of transmission (e.g., Manual, Automatic).
            description (str): Additional details about the car.
            created_at (datetime): Timestamp when the car entry was created, defaults to current time.
        """
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    maker = Column(String(30))
    model = Column(String(30))
    year = Column(Integer)
    price = Column(Float)
    mileage = Column(Float)
    fuel_type = Column(String)
    transmission = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        """
        Returns a string representation of the Car object.
        """
        return (f"<Car(id={self.id}, make={self.maker}, model={self.model}, year={self.year}, "
                f"price={self.price}, mileage={self.mileage}, fuel_type={self.fuel_type}, "
                f"transmission={self.transmission})>")
