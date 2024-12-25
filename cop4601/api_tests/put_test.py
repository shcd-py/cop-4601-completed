import requests

class PutTest:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def update_user(self, user_id, new_data):
        url = f"{self.base_url}/Account/v1/User/{user_id}"
        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.put(url, headers=headers, json=new_data)
        if response.status_code == 200:
            print(f"User with ID {user_id} updated successfully.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
