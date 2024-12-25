import requests

class CreateUserTest:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_user(self):
        url = f"{self.base_url}//Account/v1/User"  
        fname = input("Enter your first name: ")
        lname = input("Enter your last name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        data = { "firstName": fname, "lastName": lname, "userName": username, "password": password }

        try:
            response = requests.post(url, json=data)  #post request example 
            if response.status_code == 201:
                print("User created successfully:", response.json())
            elif response.status_code == 400:
                print("Invalid data. ", response.json())
            else:
                print(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"An error occurred: {e}")
