import math
import time

def calculate_square_root(number, delay):
  
  print(f"Calculating square root of {number} in {delay} milliseconds...")
  time.sleep(delay / 1000.0)  
  print(f"Square root of {number} is {math.sqrt(number)}")


numbers = [25100, 2123]
delays = [2123, 1500]


for number, delay in zip(numbers, delays):
  calculate_square_root(number, delay)