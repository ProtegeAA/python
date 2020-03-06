year = input("Type the year: ")
print(year)
if (int(year) % 4) > 0:
    print("This isn't a leap year")
elif (((int(year) % 400) == 0)) and (((int(year) % 99) != 0)):
        print("This is a leap year!")
else:
    print("It's unknown")
### code is in progress
