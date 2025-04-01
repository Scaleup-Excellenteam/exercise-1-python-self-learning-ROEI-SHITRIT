"""
This program generates a random date between two user-provided dates.
If the randomly chosen date falls on a Monday, it prints a specific message.
The program consists of two main functions:
1. `no_vinnigrete`: Parses user-provided dates and checks if the randomly generated date is a Monday.
2. `random_date`: Generates a random date between two `datetime` objects.
"""

from datetime import datetime
import random

def no_vinnigrete(date_input1, date_input2):
    """
    Generates a random date between two given dates and checks if it falls on a Monday.

    Args:
        date_input1 (str): The first date in the format YYYY-MM-DD.
        date_input2 (str): The second date in the format YYYY-MM-DD.

    Returns:
        None

    If the randomly generated date falls on a Monday, the function prints:
    "Ain't gettin' no vinaigrette today :("
    """

    try:
        date1 = datetime.strptime(date_input1, "%Y-%m-%d")
        date2 = datetime.strptime(date_input2, "%Y-%m-%d")
    except ValueError:
        print(f"Error: The date '{date_input1}' is not a valid date.")
        return None

    if date1 > date2:
        date1, date2 = date2, date1

    rand_date = random_date(date1, date2)
    if rand_date.weekday() == 0:  # checking if the generated date falls on a Monday
        print("Ain't gettin' no vinaigrette today :(")
    return None





def random_date(date1, date2):
    """
    Generates a random date between the two provided `datetime` objects.

    Args:
        date1 (datetime): The starting date.
        date2 (datetime): The ending date.

    Returns:
        datetime: A randomly generated date between `date1` and `date2`.

    Example:
        #>>> date1 = datetime(1912, 6, 23)
        #>>> date2 = datetime(1954, 6, 7)
        #>>> random_date(date1, date2)
        datetime(1939, 9, 3)
    """
    while True:
        try:
            date1_epoch = date1.timestamp()
            date2_epoch = date2.timestamp()

            # Converts the dates to epoch time (seconds since 1970) and generates a random timestamp between them.
            random_time_epoch = random.uniform(date1_epoch, date2_epoch)
            return datetime.fromtimestamp(random_time_epoch)

        except ValueError:
            continue

if __name__ == '__main__':
    no_vinnigrete("2023-07-10", "2023-07-10")
