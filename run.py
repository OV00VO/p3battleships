import random
import datetime

name = input("What is your name? ")
print("Hello World dear", name + "!")

def test_system():
  """Tests the system by printing out the current time and date."""
  now = datetime.datetime.now()
  print("The current time and date is:", now)

if __name__ == "__main__":
  test_system()
