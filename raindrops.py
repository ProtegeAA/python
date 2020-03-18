def raindrops(int):
  if int % 3 == 0:
    return "Pling"
  elif int % 5 == 0:
    return "Plang"
  elif int % 7 == 0:
    return "Plong"
  else:
    return int
