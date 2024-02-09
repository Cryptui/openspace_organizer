from utils.openspace import Openspace # Import Openspace class for managing seating arrangements
from utils.file_utils import load_colleagues_from_csv  # Import load_colleagues_from_csv for loading colleagues' names from a CSV file
def main():
    # Load colleagues from CSV file
    colleagues = load_colleagues_from_csv("new_colleagues.csv")  # Change file extension

    # Default setup of the open space
    number_of_tables = 6
    table_capacity = 4

    # Initialize openspace
    openspace = Openspace(number_of_tables, table_capacity)

    # Organize colleagues randomly and assign seats
    openspace.organize(colleagues)

    # Display the seating arrangement
    openspace.display()

if __name__ == "__main__":
    main()
