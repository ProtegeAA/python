def leap_year(year):
    print("This is a leap year!")
def leap_year_not(year):
    print("This is not a leap year!")

year = input("Enter a year: ")
if (int(year) % 4) > 0:
    leap_year_not(year)
else:
    if ((int(year) % 100) == 0) and ((int(year) % 400) == 0):
        leap_year(year)
    else:
        leap_year_not(year)
        
        
            

