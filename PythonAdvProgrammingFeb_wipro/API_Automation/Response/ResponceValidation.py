from requests.auth import HTTPBasicAuth

import  requests

try:
    headers = {
        "User-Agent": "MyApp/1.0",
        "Accept": "application/json"
    }
    #make a get request to a api endpoint
    response = requests.get("https://videogamedb.uk:443/api/v2/videogame",auth=HTTPBasicAuth('username', 'password'),timeout= 5,headers= headers)
    print(response)

    #check if type status code is 200 ok
    if response.status_code == 200:
        print("Status code is 200 k")
        #parse the json file
        data = response.json()
        #text of the response file
        print(response.text)
        #content of the response
        print(response.content)
        #print status code of the response
        print(response.status_code)
        #headers
        print(response.headers)
        #history
        print(response.history)
        #url
        print(response.url)
        #fetch the single header
        content_type = response.headers.get('content-Type')
        print(content_type)

    else:print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred : {e}")