print("Hello")
print("Good morning John")

#Date andcTime Function
from datetime import datetime, timedelta

#Todays Date
today = datetime.now()
print("Today's date is:", strftime('%d/%m/%y %H:%M:%S'))

#For the next four days
for i in range(1,5)
next_day = today + timedelta(days=i)
print (f"Day {i}:", strftime('%d/%m/%y'))

#For thr next four weeks
for i in range (1,5)
next_week = today + timedelta(weeks=i)
print(f"Week{i}:" + strftime('%y/%m/%d'))
