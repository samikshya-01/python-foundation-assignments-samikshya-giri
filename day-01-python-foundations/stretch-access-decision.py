"""
Exercise: Dataset Access Decision (Stretch)
Student: Samikshya Giri
Day: 1
"""

allowed_roles = ["analyst", "scientist", "engineer"]
restricted_datasets = ["salary_data", "personal_data"]


def check_access(user_role, is_active, requested_dataset):
    """Decide whether a user can access a dataset and print the reason."""
    if not is_active:
        print("Access denied because the user is inactive.")
    elif user_role not in allowed_roles:
        print("Access denied because the role is not allowed.")
    elif requested_dataset in restricted_datasets:
        print("Access denied because the dataset is restricted.")
    else:
        print(f"Access granted to '{requested_dataset}' for role '{user_role}'.")
    print("-" * 40)


# Scenario 1: everything valid -> access granted
user_role = "analyst"
is_active = True
requested_dataset = "sales_data"
check_access(user_role, is_active, requested_dataset)

# Scenario 2: inactive user -> denied
user_role = "scientist"
is_active = False
requested_dataset = "sales_data"
check_access(user_role, is_active, requested_dataset)

# Scenario 3: role not allowed -> denied
user_role = "manager"
is_active = True
requested_dataset = "sales_data"
check_access(user_role, is_active, requested_dataset)

# Scenario 4: restricted dataset -> denied
user_role = "engineer"
is_active = True
requested_dataset = "salary_data"
check_access(user_role, is_active, requested_dataset)