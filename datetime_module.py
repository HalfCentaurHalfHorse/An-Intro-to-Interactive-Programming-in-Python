"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if not (datetime.MINYEAR <= year <= datetime.MAXYEAR):
        return False
    if not (1 <= month <= 12):
        return False
    if month == 12:
        return 31
    return (datetime.date(year, month+1, 1) - datetime.date(year, month, 1)).days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if not days_in_month(year, month):
        return False
    if 0 < day <= days_in_month(year, month):
        return True
    return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if not (is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2)):
        return 0
    count_days = (datetime.date(year2, month2, day2) - datetime.date(year1, month1, day1)).days
    if count_days <= 0:
        return	0
    return count_days


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    today_date, today_month = datetime.date.today().day, datetime.date.today().month
    today_year = datetime.date.today().year
    return days_between(year, month, day, today_year, today_month, today_date)
