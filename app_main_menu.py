class App:
    def __init__(self, car_rep, statistics):
        """
        Initializes the App with a car repository and a statistics module.

        :param car_rep: An object responsible for managing car listings.
        :param statistics: An object responsible for displaying statistics.
        """
        self.car_rep = car_rep
        self.statistics = statistics

    @staticmethod
    def display_menu():
        """
        Displays the main menu for the car listing application.
        """
        print(f"=== Car Listing Menu ===\n"
              f"1. Add new car\n"
              f"2. Search cars\n"
              f"3. Update a car\n"
              f"4. Delete a car\n"
              f"5. View all cars\n"
              f"6. Statistics\n"
              f"0. Exit")

    def run_selection(self):
        """
        Runs the main loop of the application, allowing users to interact
        with the car listing system based on menu selections.
        """
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
        """
        Calls the add_car method from the car repository to add a new car.
        """
        self.car_rep.add_car()

    def search_cars(self):
        """
        Calls the search_cars method from the car repository to search for cars.
        """
        self.car_rep.search_cars()

    def update_car(self):
        """
        Calls the update_car method from the car repository to update a car listing.
        """
        self.car_rep.update_car()

    def delete_car(self):
        """
        Calls the delete_car method from the car repository to remove a car listing.
        """
        self.car_rep.delete_car()

    def view_all_cars(self):
        """
        Calls the view_all_cars method from the car repository to display all listed cars.
        """
        self.car_rep.view_all_cars()

    def view_statistics(self):
        """
        Calls the statistics_display method from the statistics module to display car-related statistics.
        """
        self.statistics.statistics_display()
