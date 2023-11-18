import base64

client_id = 'dsO5edfeQneSJl0czptGMw'
client_secret = '1Q7p96uSdEJvHLFVbxGlhOTCPnCACHX4'
zoom_client_credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
print(zoom_client_credentials)
# Now set ZOOM_CLIENT_CREDENTIALS in your .env file to the value of zoom_client_credentials
