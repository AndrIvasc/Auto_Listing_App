from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Car(Base):
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
        return (f"<Car(id={self.id}, make={self.maker}, model={self.model}, year={self.year}, "
                f"price={self.price}, mileage={self.mileage}, fuel_type={self.fuel_type}, "
                f"transmission={self.transmission})>")