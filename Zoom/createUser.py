from dotenv import load_dotenv, find_dotenv
import requests
import os

# Load environment variables
load_dotenv(find_dotenv())

# Function to generate an OAuth access token
def generate_oauth_token():
    url = "https://zoom.us/oauth/token"
    payload = {
        'grant_type': 'client_credentials'
    }
    headers = {
        'Authorization': 'Basic ' + os.getenv('ZOOM_CLIENT_CREDENTIALS')
    }
    response = requests.post(url, headers=headers, data=payload)
    token = response.json().get('access_token', None)
    scopes = response.json().get('scope', None)
    if not token:
        raise Exception("Failed to retrieve access token")
    return token, scopes

# Generate the OAuth token
oauth_token, scopes = generate_oauth_token()

# Print the OAuth token
print(oauth_token)
print("scopes: ", scopes)
# Set the authorization header with the OAuth tokenD
headers = {
    'Authorization': f"Bearer {oauth_token}",
    'Content-Type': "application/json"
}

# Payload for creating a new user
payload = {
  "action": "create",
  "user_info": {
    "email": "jchill@example.com",
    "first_name": "Jill",
    "last_name": "Chill",
    "display_name": "Jill Chill",
    "password": "if42!LfH@",
    "type": 1,
    "feature": {
      "zoom_phone": True,
      "zoom_one_type": 16
    },
    "plan_united_type": "1"
  }
}

# Make the API request to create a new user
response = requests.post("https://api.zoom.us/v2/users", headers=headers, json=payload)

# Print the status code and JSON response
print(response.status_code)
print(response.json())
