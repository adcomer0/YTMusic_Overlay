import requests

url = "http://localhost:5000/update"
data = {
    "song": "Test Song",
    "artist": "Test Artist",
    "albumArt": "https://via.placeholder.com/150"  # Example of a valid image URL
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.json())
