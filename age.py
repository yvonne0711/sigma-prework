# given a date, calculate the age between the current date and the given date
# 01-01-1990 returns 35
# 04-12-1972 returns 53
# need a date
from datetime import date


def age_calculator():
    # user input as birthday
    # birthday = "04-12-1972"
    birthday = input(
        "When is your birthday? Please format it like dd-mm-yyyy: ")
    # unpacking a list
    day, month, year = birthday.split("-")
    birthday_year = int(year)

    # today's date
    today = date.today()

    # calculate age
    age = today.year - birthday_year

    # if the birthday hasn't passed this year yet, minus one from the age
    if (today.month, today.day) < (int(month), int(day)):
        age -= 1

    return age


# call function and print
print(age_calculator())
