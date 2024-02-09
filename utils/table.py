#Nice 2 have test 

from typing import Optional 

"""
Optional indicates that self.occupant may have name a type of 'str' 
or may be None! Initialized as None of type 'NoneType' by default

    Example: 
    def my_function():
        pass
    result = my_function()  # result will be None
"""

class Seat: 
    """
    A class to represent a seat at the table.

    Attributes:
        free (bool): Returns if the seat is free or occupied
        occupant (Optional[str]): Name of the person occupying the seat, if any
    """

    def __init__(self):
        # initialize the seat as free with no occupant
        self.free: bool = True
        self.occupant: Optional[str] = None
    
    def set_occupant(self, name: str):
        """
        Assigns an occupant to the seat.

        Args:
            name (str): The name of the person to be assigned to the seat.
        """

        self.occupant = name
        self.free = False

    """
    The remove_occupant could be used for later upgrades of this project
    """

    """
    def remove_occupant(self):
        # Removes the occupant from the seat and marks it as free.

        # Returns:
        #    str: The name of the removed occupant.
        occupant_name = self.occupant
        self.occupant = None
        self.free = True
        return occupant_name
    
    """
    
class Table:
    """
    A class to represent a table with multiple seats.

    Attributes:
        capacity (int): The maximum number of seats at the table.
        seats (list): A list of Seat objects representing the seats at the table.
    """

    def __init__(self, capacity: int):
        # initialize the Table with a given capacity
        self.capacity: int = capacity 

        # Create a list of Seat objects to represent the seats at the table
        self.seat = [Seat() for _ in range(capacity)]
    
    def has_free_spot(self):
        """
        Checks if there is at least one free seat at the table.

        Returns:
            bool: True, if there is a free seat. False, there is no free seat.
        """

        # check if any seat at the table is free
        for seat in self.seat:
            if seat.free:
                return True
        return False
    
    def assign_seat(self, name: str):
        """
        Assigns a seat to a person if there's a free seat available.

        Args:
            name (str): The name of the person to be assigned to the seat.

        Returns:
            bool: True, if there is a free seat. False, there is no free seat.
        """
               
        # Assign a seat to a person if there's a free seat
        for seat in self.seat:
            if seat.free:
                seat.set_occupant(name)
                return True  # Return True to indicate that the seat has been assigned
        return False  # Return False if all seats are occupied