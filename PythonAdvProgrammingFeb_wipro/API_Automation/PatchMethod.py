import  requests

try:

    data = {
        # "category": "Platform",
        "name": "Shivanshu Patel(Updated partially)"#,
        # "rating": "Mature",
        # "releaseDate": "2012-05-04",
        # "reviewScore": 85
    }
    #make a Patch request to a api endpoint
    response = requests.patch("https://api.restful-api.dev/objects/ff8081819c5368bb019c55a4277f046e",json=data)
    print(response)

    #check if type status code is 200 ok
    if response.status_code == 200:
        print("Status code is 200 k")
        #parse the json file
        data = response.json()
        print(data)

    else:print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred : {e}")