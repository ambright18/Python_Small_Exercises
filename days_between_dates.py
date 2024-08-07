# a very simple python exercise to calculate the days between pre-defined dates

from datetime import date

first_date = date(2024, 1, 2)

second_date = date(2024, 8, 27)

delta = second_date - first_date

print(delta.days)

