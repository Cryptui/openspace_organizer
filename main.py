#Nice 2 have  

from utils.openspace import Openspace 
from utils.file_utils import load_colleagues_from_csv  

def main():
    # Load colleagues from CSV file
    colleagues = load_colleagues_from_csv("new_colleagues.csv")  # Change file extension

    # Ask the user for the number of tables
    number_of_tables = int(input("How many tables are there in the room? "))

    # Ask the user for the table capacity
    table_capacity = int(input("How many chairs could be at each table? "))

    # Calculate the total capacity of the room
    total_capacity = number_of_tables * table_capacity

    # Check if the total capacity is enough to accommodate all colleagues
    if len(colleagues) > total_capacity:
        print("The room capacity is not enough to accommodate all colleagues.")

        # Initialize openspace
        openspace = Openspace(number_of_tables, table_capacity)

        # Organize colleagues randomly and assign seats
        openspace.organize(colleagues)

        # Display the seating arrangement
        print("Seating arrangement:")
        openspace.display()

        print("The following colleagues cannot be seated:")
        remaining_colleagues = colleagues[total_capacity:]
        for colleague in remaining_colleagues:
            print(colleague)
        
        # Store the seating arrangement in an Excel file (overwrite existing file)
        openspace.store_seat_arrangement("seating_arrangement.xlsx", remaining_colleagues)

    else:
        # Initialize openspace
        openspace = Openspace(number_of_tables, table_capacity)

        # Organize colleagues randomly and assign seats
        openspace.organize(colleagues)

        # Display the seating arrangement
        print("Seating arrangement:")
        openspace.display()

        # Print the names of colleagues who are seated
        print("\nColleagues who are seated:")
        seated_colleagues = colleagues[:total_capacity]
        for colleague in seated_colleagues:
            print(colleague)
    
        # Check if there are empty seats
        empty_seats = total_capacity - len(colleagues)
        if empty_seats > 0:
            print("\nEmpty seats:")
            for i in range(total_capacity - empty_seats, total_capacity):
                table_index = i // table_capacity
                seat_index = i % table_capacity
                print(f"Table {table_index + 1}: Seat {seat_index + 1}")
        
        # Store the seating arrangement in an Excel file (overwrite existing file)
        openspace.store_seat_arrangement("seating_arrangement.xlsx")

if __name__ == "__main__":
    main()
