#2
"""
from types import CodeType


Python for everone 1: week 3 - Variables
Eric Darsow, Instructor Code
Goal: compute and compare muleage and 
fuel use across small and large cars
"""


print("Welcome to road trip efficiency comparisons!")
# variable names always:
# start with a lowercase letter, and not a number # assigning a string literal on the 
# right to the variable on the left
small_vehicle = "2023 Volkswagen Jetta Sport"
large_vehicle = "2019 STI S209"
small_vehicle_mpg = 33.0
large_vehicle_mpg = 17.0
print(type(large_vehicle_mpg))
small_vehicle_url = "https://en.wikipedia.org/wiki/Volkswagen_Jetta_(A7)"
large_vehicle_url = "https://en.wikipedia.org/wiki/Subaru_WRX_STI"

print("The ", small_vehicle, " can drive ", small_vehicle_mpg, " per gallon of gasoline")
print("Info can be found at ", small_vehicle_url)
print("The ", large_vehicle, " can drive ", large_vehicle_mpg, " per gallon of gasoline")
print("Info can be found at ", large_vehicle_url)

print("------------------Mileage----------------------")
print("Road trip! How many miles? (decimal places okay)")
# read un keyboard input it into a float, store in trip_miles
trip_miles = float(input())
# gallons computed by dividing trip length by mileage per gallon
small_vehicle_gallons = trip_miles / small_vehicle_mpg
large_vehicle_gallons = trip_miles / large_vehicle_mpg
print("The", small_vehicle ,"Will require", small_vehicle_gallons, "gallons to travel", trip_miles, "miles")

print("----------------------------------------------------")