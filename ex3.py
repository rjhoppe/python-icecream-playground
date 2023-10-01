from icecream import ic
import time

# Configure debug timestamp
def debug_timestamp():
  return '%i |> ' % int(time.time())

ic.configureOutput(prefix=debug_timestamp())

userWeight = 73  # kilograms
userHeight = 171  # cm

def calculateBMI(weight, height):
  bmi = weight / (height/100)**2
  if bmi < 10:
    result = 'underweight'
    ic()
  elif bmi < 25:
    result = "normal"
    ic()
    ic(weight, height)
  elif bmi > 25:
    result = "overweight"
    ic()

  return result

print(calculateBMI(userWeight, userHeight))