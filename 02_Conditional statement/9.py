# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).
year = input("Enter year: ")
year_in_int = int(year)
if (year_in_int % 400 == 0) or (year_in_int % 4 == 0 and year_in_int % 100 != 0):
    print( year_in_int, "is a leap year")
else:
    print(year_in_int, "is NOT a leap year")