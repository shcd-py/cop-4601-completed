import requests

class GetBooksTest:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_books(self):
        url = f"{self.base_url}/BookStore/v1/Books"
        response = requests.get(url)
        if response.status_code == 200:
            print("Books retrieved successfully:", response.json())
        else:
            print(f"Error: {response.status_code} - {response.text}")
