import datetime #about the date and the time.



now = datetime.datetime.now()
print('Current date and time: ', now)
print(now.date())
print(now.time())

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)