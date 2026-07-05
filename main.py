from age import calculate_age, is_adult

birth_year = int(input("Enter your birth year: "))

age = calculate_age(birth_year)

print(f"\nYour age is: {age}")

if is_adult(age):
    print("Status: Adult")
else:
    print("Status: Minor")
