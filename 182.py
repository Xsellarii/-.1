
import datetime


day = int(input())
month = int(input())
year = int(input())


current_date = datetime.date(year, month, day)
next_date = current_date + datetime.timedelta(days=1)

print(f"{next_date.day}. {next_date.month}. {next_date.year}")
