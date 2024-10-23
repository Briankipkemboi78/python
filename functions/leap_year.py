def is_leap_year(year):
    if year % 400 == 0:
        return "Leap Year"
    elif year % 100 == 0:
        return "Not a Leap Year"
    elif year % 4 == 0:
        return "Leap Year"
    else:
        return "Not a Leap Year"

# Get user input and check if it's a leap year
year_input = int(input("Please enter your year: "))
result = is_leap_year(year_input)

print(result)