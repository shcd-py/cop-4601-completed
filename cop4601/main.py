from api_tests.get_books_test import GetBooksTest
from api_tests.create_user_test import CreateUserTest
from api_tests.delete_user_test import DeleteUserTest
from api_tests.put_test import PutTest
from ui_tests.login_test import LoginTest
from ui_tests.collection_test import ButtonTest
from ui_tests.delete_all_books import DeleteAllBooksTest
from ui_tests.delete_account_test import DeleteAccountTest
from api_tests.scenario_test import ScenarioTest

def get_books_test(base_url):
    test = GetBooksTest(base_url)
    test.get_books()

def create_user_test(base_url):
    test = CreateUserTest(base_url)
    test.create_user()

def delete_user_test(base_url, token):
    test = DeleteUserTest(base_url, token)
    user_id = input("Enter user ID to delete: ")
    test.delete_user(user_id)

def update_user_test(base_url, token):
    test = PutTest(base_url, token)
    user_id = input("Enter user ID to update: ")
    new_data = {"userName": input("Enter new username: ")}
    test.update_user(user_id, new_data)

def login_test(driver_path):
    test = LoginTest(driver_path)
    url = f"{base_url}/login"
    username = input("Enter username: ")
    password = input("Enter password: ")
    test.login(url, username, password)

def button_test(driver_path):
    test = ButtonTest(driver_path)
    url = f"{base_url}/buttons"
    test.test_buttons(url)

def delete_all_books_test(base_url, driver_path):
    test = DeleteAllBooksTest(driver_path)
    username = input("Enter username: ")
    password = input("Enter password: ")
    test.delete_books(base_url, username, password)

def scenario_test(base_url):
    test = ScenarioTest(base_url)
    test.run_scenario()

def delete_account_test(base_url, driver_path):
    test = DeleteAccountTest(driver_path)
    username = input("Enter username: ")
    password = input("Enter password: ")
    test.delete_account(base_url, username, password)

if __name__ == "__main__":
    base_url = "https://demoqa.com"
    token = "YOUR_ACCESS_TOKEN"
    driver_path = "msedgedriver.exe"

    options = {
    

        1: lambda: get_books_test(base_url),
        2: lambda: create_user_test(base_url),
        3: lambda: delete_user_test(base_url, token),
        4: lambda: update_user_test(base_url, token),
        5: lambda: login_test(driver_path),
        6: lambda: button_test(driver_path),
        7: lambda: delete_all_books_test(base_url, driver_path),
        7: lambda: delete_account_test(base_url, driver_path),
        9: lambda: scenario_test(base_url),
        0: lambda: print("Exiting..."),
    }

    while True:
        print("\nSelect an option:")
        print("1. Run API Get Books Test")
        print("2. Run API Create User Test")
        print("3. Run API Delete User Test")
        print("4. Run API Update User Test")
        print("5. Run UI Login Test")
        print("6. Run UI Button Click Test")
        print("7. Run UI Delete All Books")
        print("8. Run UI Delete Account")
        print("9. Run Apı scenario test")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice: "))
            action = options.get(choice, lambda: print("Invalid choice."))
            action()
            if choice == 0:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
