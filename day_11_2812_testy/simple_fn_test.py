#  python -m unittest simple_fn_test.py
import unittest
import datetime
from datetime import datetime
from dateutil import relativedelta


def calculate_capital(payment_premium: float, payment_bonus_percentage: float, payment_start_date) -> float:
    assert isinstance(payment_premium, float), f"Typ wejściowy: {type(payment_premium)}"
    assert isinstance(payment_bonus_percentage, float), f"Typ wejściowy: {type(payment_premium)}"

    sum_of_premium = 0
    last_day_current_month = datetime.now() + relativedelta.relativedelta(day=31)
    last_day_of_payment_start_date = datetime.fromisoformat(payment_start_date) + relativedelta.relativedelta(day=31)
    dates_relative = relativedelta.relativedelta(last_day_current_month, last_day_of_payment_start_date)

    for _ in range(int(dates_relative.months)):
        sum_of_premium += payment_premium
        sum_of_premium += sum_of_premium * payment_bonus_percentage

    return sum_of_premium


class TestCalculate(unittest.TestCase):
    def test_sample_value_1(self):
        payment_premium = 100.0
        payment_bonus_percentage = 0.05
        payment_start_date = '2021-01-01'
        self.assertGreater(calculate_capital(payment_premium, payment_bonus_percentage, payment_start_date), 149)

    def test_sample_value_2(self):
        payment_premium = 100.0
        payment_bonus_percentage = 0.05
        payment_start_date = '2021-01-01'
        self.assertEqual(calculate_capital(payment_premium, payment_bonus_percentage, payment_start_date), 1491.7126520442582)

    def test_sample_value_3(self):
        payment_premium = 100.0
        payment_bonus_percentage = 0.3
        payment_start_date = '2021-01-01'
        self.assertGreater(calculate_capital(payment_premium, payment_bonus_percentage, payment_start_date), 2000)

# if __name__ == '__main__':
#     # to jest najprostsze
#     unittest.main()
