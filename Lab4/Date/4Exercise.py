from datetime import datetime

def date_diff_in_seconds(date1, date2):
  
  time_delta = date1 - date2
  return time_delta.total_seconds()

# Example usage
date1 = datetime(2024, 3, 7, 12, 30, 45)
date2 = datetime(2024, 3, 8, 9, 10, 10)

difference_in_seconds = date_diff_in_seconds(date1, date2)
print("Difference between dates in seconds:", difference_in_seconds)
