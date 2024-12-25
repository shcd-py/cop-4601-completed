import requests

class DeleteUserTest:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def delete_user(self, user_id):
        url = f"{self.base_url}/Account/v1/User/{user_id}"
        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.delete(url, headers=headers)
        if response.status_code == 204:
            print(f"User with ID {user_id} deleted successfully.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
