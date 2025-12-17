import requests
from backend.src.app.core.config import settings

class BetterAuthClient:
    def __init__(self):
        self.base_url = settings.BETTER_AUTH_BASE_URL
        self.api_key = settings.BETTER_AUTH_API_KEY
        self.headers = {"X-API-Key": self.api_key, "Content-Type": "application/json"}

    def validate_token(self, token: str) -> dict | None:
        """
        Validates a given JWT token with the Better Auth service.
        Returns user information if valid, None otherwise.
        """
        url = f"{self.base_url}/auth/validate"
        try:
            response = requests.post(url, headers=self.headers, json={"token": token})
            response.raise_for_status() # Raise an exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error validating token with Better Auth: {e}")
            return None

    def authenticate_user(self, username, password) -> dict | None:
        """
        Authenticates a user with the Better Auth service.
        Returns a dictionary containing access_token if successful, None otherwise.
        """
        url = f"{self.base_url}/auth/login"
        try:
            response = requests.post(url, headers=self.headers, json={"username": username, "password": password})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error authenticating user with Better Auth: {e}")
            return None

better_auth_client = BetterAuthClient()
