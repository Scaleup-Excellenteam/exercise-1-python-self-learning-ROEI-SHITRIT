from datetime import datetime
import random

def no_vinnigrete():
    """
      Prompts the user to input two dates in the format YYYY-MM-DD, and generates a random date between the two provided dates.
      If the random date falls on a Monday, it prints "אין לי וינגרט!", otherwise it prints "יש ל וינגרט".

      User inputs:
          - Two dates in the format YYYY-MM-DD.

      Returns:
          None

      Example:
          Enter a date (YYYY-MM-DD): 1912-06-23
          Enter a date (YYYY-MM-DD): 1954-06-07
          If the generated date falls on a Monday, the output will be: "אין לי וינגרט!"
          If not, the output will be: "יש ל וינגרט"
      """

    date_input1 = input("Enter a date (YYYY-MM-DD): ")
    date_input2 = input("Enter a date (YYYY-MM-DD): ")
    try:
        date1 = datetime.strptime(date_input1, "%Y-%m-%d")
        date2 = datetime.strptime(date_input2, "%Y-%m-%d")
    except ValueError:
        print(f"Error: The date '{date_input1}' is not a valid date.")
        exit(-1)
    if date1 > date2:
        date1,date2 = date2,date1
    rand_date = random_date(date1, date2)
    """ checking if the generated date falls on a Monday """
    if rand_date.weekday() == 0:
        print("Ain't gettin' no vinaigrette today :(")





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
         # >>> random_date(date1, date2)
          datetime(1939, 9, 3)
      """
    while True:
        try:
            date1_epoch = date1.timestamp()
            date2_epoch = date2.timestamp()
            """Converts the dates to epoch time (seconds since 1970) and generates a random timestamp between them."""
            random_time_epoch = random.uniform(date1_epoch, date2_epoch)
            random_date_to_send = datetime.fromtimestamp(random_time_epoch)
            random_date_to_send.strftime("%Y-%m-%d")
            return random_date

        except ValueError:
            continue

if __name__ == '__main__':
    no_vinnigrete()
