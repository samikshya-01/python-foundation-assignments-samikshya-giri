"""
Exercise: Customer Record Cleaner
Student: Samikshya Giri
Day: 1
"""

# Raw input values
raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "

# Cleaning
clean_name = raw_name.strip().title()
clean_city = raw_city.strip().title()
clean_age = int(raw_age.strip())
clean_email = raw_email.strip().lower()

# Ternary expression for adult status
status = "Adult" if clean_age >= 18 else "Minor"

# Output
print(f"Name: {clean_name}")
print(f"City: {clean_city}")
print(f"Age: {clean_age}")
print(f"Email: {clean_email}")
print(f"Status: {status}")