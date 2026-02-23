# Section 1: Basic Level
# 1. Write a Python script to send a GET request to https://jsonplaceholder.typicode.com/users and print only name and email.
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    for user in users:
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("-" * 30)
else:
    print("Request failed:", response.status_code)


# 2. Send a GET request with query parameter userId=2 and print number of posts returned.

import requests

url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 2}

response = requests.get(url, params=params)

if response.status_code == 200:
    posts = response.json()
    print("Number of posts:", len(posts))
else:
    print("Request failed:", response.status_code)

print("hello Shivanshu")
# 3. Write a POST request to create a new resource and verify status code 201.

import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "My New Post",
    "body": "This is a test post",
    "userId": 1
}

response = requests.post(url, json=payload)

if response.status_code == 201:
    print("Resource created successfully!")
    print("Response:", response.json())
else:
    print("Failed with status:", response.status_code)

# 4. Explain the difference between data= and json= in requests.post().

# 5. Write code to check if response status code is not 200 and raise an exception.
url = "https://jsonplaceholder.typicode.com/users/123"
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error occurred:", e)




# Section 2: Intermediate Level
# 6. Fetch all users and print usernames in uppercase.
# 7. Implement timeout handling (2 seconds) and catch Timeout exception.
# 8. Use Session object to send multiple requests and demonstrate cookie persistence.
# 9. Upload a file using requests and print server response.
# 10. Fetch posts and save response JSON into a file named posts.json.