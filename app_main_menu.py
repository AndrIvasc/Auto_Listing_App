class App:
    def __init__(self, car_rep, statistics):
        self.car_rep = car_rep
        self.statistics = statistics

    @staticmethod
    def display_menu():
        print(f"=== Car Listing Menu ===\n"
              f"1. Add new car\n"
              f"2. Search cars\n"
              f"3. Update a car\n"
              f"4. Delete a car\n"
              f"5. View all cars\n"
              f"6. Statistics\n"
              f"0. Exit")

    def run_selection(self):
        while True:
            self.display_menu()
            choise = input("Make a selection:\n"
                           "> ")

            try:
                if choise == '1':
                    self.add_car()
                    input("Press enter to continue...")
                if choise == '2':
                    self.search_cars()
                    input("Press enter to continue...")
                if choise == '3':
                    self.update_car()
                    input("Press enter to continue...")
                if choise == '4':
                    self.delete_car()
                    input("Press enter to continue...")
                if choise == '5':
                    self.view_all_cars()
                    input("Press enter to continue...")
                if choise == '6':
                    self.view_statistics()
                    input("Press enter to continue...")
                if choise == '0':
                    print("Exiting the programm! See you next time! ;)")
                    break
            except Exception as e:
                print(f"Error has occured -> {e}")

    def add_car(self):
        self.car_rep.add_car()

    def search_cars(self):
        self.car_rep.search_cars()

    def update_car(self):
        self.car_rep.update_car()

    def delete_car(self):
        self.car_rep.delete_car()

    def view_all_cars(self):
        self.car_rep.view_all_cars()

    def view_statistics(self):
        self.statistics.statistics_display()
