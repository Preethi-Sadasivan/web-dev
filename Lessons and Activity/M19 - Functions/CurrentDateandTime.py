
from datetime import date, time,datetime

today = date.today()
now = datetime.now()

print("Today's date:", today)
print("Current date and time:", now)    

print ("Date Components",today.year, today.month, today.day)