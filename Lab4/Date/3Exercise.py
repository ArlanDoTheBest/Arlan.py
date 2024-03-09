import datetime

def drop_microseconds(dt):
  
  return dt.replace(microsecond=0)


now = datetime.datetime.now()
now_without_microseconds = drop_microseconds(now)

print("Original datetime:", now)
print("Datetime without microseconds:", now_without_microseconds)