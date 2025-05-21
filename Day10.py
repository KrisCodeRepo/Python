def is_leap_year(year):
    """
    Check if a year is a leap year.
    
    A year is a leap year if it is divisible by 4, but not divisible by 100,
    unless it is also divisible by 400.
    
    Args:
        year (int): The year to check.
        
    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap_year(2000))  # True