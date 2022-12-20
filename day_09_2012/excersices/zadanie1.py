from datetime import datetime
from dateutil.relativedelta import relativedelta


# start_date must be in format: 20-10-2022 (day-month-year)
def my_function_precondition(month_premium: int, percentage: int, start_date: str):
    date_start = datetime.strptime(start_date, '%d-%m-%Y').date()
    date_now = datetime.now().date()

    # Get the relativedelta between two dates
    delta = relativedelta(date_now, date_start)
    years = delta.years
    months = delta.months

    if years > 0:
        months += years * 12

    result = 0
    for i in range(1, months + 1):
        result += month_premium
        result += percentage / 100 * result
        result = round(result, 2)
        print(i, 'month =', result)

    return result, months


if __name__ == '__main__':
    month_premium = 100
    percentage = 5
    start_date = '10-05-2022'

    result, months_number = my_function_precondition(month_premium, percentage, start_date)
    assert result > month_premium * months_number * percentage / 100, f"Result is {result} and it is less than {month_premium * months_number * percentage / 100}."
    assert isinstance(result, float), f"Result is not float type, but {type(result)}."
