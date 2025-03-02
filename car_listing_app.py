from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from car import Base
from car_rep import CarRep
from car_statistics import Statistics
from app_main_menu import App

engine = create_engine('sqlite:///autolisting.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

car_rep = CarRep(session)
statistics = Statistics(session)

app = App(car_rep, statistics)
app.run_selection()
