import requests

class ScenarioTest:
    def __init__(self, base_url):
        self.base_url = base_url
        self.username = "Hakancan34"
        self.password = "HakanTest@123"

    def create_user(self):
        url = f"{self.base_url}/Account/v1/User"
        payload = {
            "userName": self.username,
            "password": self.password
        }
        response = requests.post(url, json=payload)
        if response.status_code == 201:
            print("User created successfully:", response.json())
            return response.json()["userID"]
        else:
            print("Error creating user:", response.status_code, response.text)
            return None

    def login_user(self):
        url = f"{self.base_url}/Account/v1/Login"
        payload = {
            "userName": self.username,
            "password": self.password
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Login successful:", response.json())
            return self.generate_token()  # Token al
        else:
            print("Login failed:", response.status_code, response.text)
            return None

    def generate_token(self):
        url = f"{self.base_url}/Account/v1/GenerateToken"
        payload = {
            "userName": self.username,
            "password": self.password
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Token generated:", response.json())
            return response.json()["token"]
        else:
            print("Token generation failed:", response.status_code, response.text)
            return None

    def delete_user(self, token, user_id):
        url = f"{self.base_url}/Account/v1/User/{user_id}"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        response = requests.delete(url, headers=headers)
        if response.status_code == 200:
            print("User deleted successfully.")
        elif response.status_code == 204:
            print("User deleted successfully (204 - No Content).")
        elif response.status_code == 401:
            print("Unauthorized. Please check your token.")
        elif response.status_code == 404:
            print("User not found.")
        else:
            print(f"Error deleting user: {response.status_code} - {response.text}")

    def run_scenario(self):
        print("Running scenario test...")
        user_id = self.create_user()
        if user_id:
            token = self.login_user()
            if token:
                self.delete_user(token, user_id)
