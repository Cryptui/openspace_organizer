import random # Import the random module
from typing import List # Typing provides support for defining type hints, names is expected to be a list of strings
from .table import Table # Relative import, from .table module import class Table

class Openspace:

    """
    A class to represent an open space.

    """
    def __init__(self, number_of_tables: int, table_capacity: int):
        """
        Initializes an Openspace object with the given number of tables and table capacity.
        Args:
            number_of_tables (int): The number of tables in the openspace.
            table_capacity (int): The maximum number of seats per table.
        """
       
        # Create a list of Table objects representing the tables in the openspace
        self.tables: List[Table] = [Table(table_capacity) for _ in range(number_of_tables)]
        
        # Store the number of tables
        self.number_of_tables: int = number_of_tables

    def organize(self, names: List[str]):
        """
        Randomly assigns people to seats in the openspace.
        Args:
            names (List[str]): A list of names of people to be assigned to seats.
        """
                
        # Shuffle the list of names randomly
        random.shuffle(names)
        # Initialize table index

        table_index = 0
        # Iterate through each name and assign seats

        for name in names:
            # Find the next table with a free spot
            while table_index < self.number_of_tables and not self.tables[table_index].has_free_spot():
                table_index += 1
            # If all tables are full
            if table_index == self.number_of_tables:
                print("Not enough space to seat all colleagues.")
                return
            
            # Assign the seat to the person
            self.tables[table_index].assign_seat(name)

            # Move to the next table (circular)
            table_index = (table_index + 1) % self.number_of_tables

    def display(self):
        """Displays the seating arrangement in a readable format."""

        for i, table in enumerate(self.tables):
            print(f"Table {i+1}: ")
            for j, seat in enumerate(table.seat):
                print(f"\tSeat {j+1}: {'Empty' if seat.free else seat.occupant}")
    

