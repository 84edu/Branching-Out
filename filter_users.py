import json


def load_users():
    """Loads the file only once and central"""
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: users.json not found.")
        return []


def print_filtered_results(filtered_users):
    """uniform output of results."""
    if not filtered_users:
        print("No users found matching your criteria.")
    else:
        for user in filtered_users:
            print(user)

def filter_users_by_name(users, name):
    filtered = [user for user in users if name.lower() in user["name"].lower()]
    print_filtered_results(filtered)

def filter_users_by_age(users, age):
    filtered = [user for user in users if user["age"] == age]
    print_filtered_results(filtered)

def filter_users_by_email(users, email):
    filtered = [user for user in users if email.lower() == user["email"].lower()]
    print_filtered_results(filtered)


def get_valid_filter_option():
    """Keep asking the user until a valid option is provided."""
    supported = ["name", "age", "email"]
    while True:
        choice = input(f"Choose filter ({'/'.join(supported)}): ").strip().lower()
        if choice in supported:
            return choice
        print("Filtering by that option is not yet supported! Try again.")


def run_filter_interface():
    # 1. loading the data
    users = load_users()
    if not users:
        return

    # 2. Filter Option
    filter_option = get_valid_filter_option()

    # 3. Execute the logic
    if filter_option == "name":
        user_input = input("Enter a name to filter users: ").strip()
        filter_users_by_name(users, user_input)
    elif filter_option == "age":
        while True:
            try:
                user_input = int(input("Enter age to filter users: "))
                filter_users_by_age(users, user_input)
                break
            except ValueError:
                print("Invalid input! Please enter a valid number (e.g., 25).")
    elif filter_option == "email":
        user_input = input("Enter email: ").strip()
        filter_users_by_email(users, user_input)
    else:
        print("Filtering by that option is not yet supported.")

if __name__ == "__main__":
    run_filter_interface()

