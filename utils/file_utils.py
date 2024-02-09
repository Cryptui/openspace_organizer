import csv
from typing import List

def load_colleagues_from_csv(filename: str) -> List[str]:
    """
    Loads colleagues' names from a CSV file.

    Args:
        filename (str): The name of the CSV file containing colleagues' names.

    Returns:
        List[str]: A list of colleagues' names.
    """

    # Error Handling
    try:

        # Try to open file and load names as a list
        names = []
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    names.append(row[0])
        return names
    
    # If file not found
    except FileNotFoundError:   
        print(f"File '{filename}' not found.")
        return []
    
    # Any other error
    except Exception as e:
        print(f"Error loading colleagues from '{filename}': {e}")
        return []
