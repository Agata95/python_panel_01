from datetime import datetime, timedelta
import calendar


def two_weeks_ago(date_from_user: str) -> str:
    user_date = datetime.strptime(date_from_user, '%d-%m-%Y').date()
    days = timedelta(days=14)
    ago = user_date - days

    return calendar.day_name[ago.weekday()]


value = '20-12-2022'
result = two_weeks_ago(value)
print(f'Two weeks ago from {value} was {result}.')
