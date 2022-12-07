from datetime import datetime, timedelta

today_is = datetime.today()

weekday = today_is.strftime('%A')
# skąd to się bierze...
# https://strftime.org/
# https://man7.org/linux/man-pages/man3/strftime.3.html
# https://docs.python.org/3/library/datetime.html

week_before = today_is - timedelta(7)
print(f"Today is {today_is}, which means: {weekday}, but in other way {today_is.date()}, week after {week_before.date()}")
