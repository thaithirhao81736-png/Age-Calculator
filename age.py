from datetime import datetime


def calculate_age(birth_year):
    current_year = datetime.now().year
    return current_year - birth_year


def is_adult(age):
    return age >= 18
