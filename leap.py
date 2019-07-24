def leap_year(year):
   if (int(year) % 4) > 0:
    return False
   else:
    if ((int(year) % 400) == 0):
        return True
    else:
     if ((int(year) % 100) != 0):
        return True
     else:
      if ((int(year) % 100) == 0):
         return False          
