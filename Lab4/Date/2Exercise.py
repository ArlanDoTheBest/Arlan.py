from datetime import date


today = date.today()


yesterday = today - date.timedelta(days=1)
tomorrow = today + date.timedelta(days=1)


print(f"Yesterday: {yesterday.strftime('%Y-%m-%d')}")
print(f"Today: {today.strftime('%Y-%m-%d')}")
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")