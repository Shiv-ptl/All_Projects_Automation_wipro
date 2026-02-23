import  requests

try:

    #make a Delete request to a api endpoint
    response = requests.delete("https://videogamedb.uk:443/api/v2/videogame/1")
    print(response)

    #check if type status code is 200 ok
    if response.status_code == 200:
        print("Status code is 200")
        #parse the json file
        data = response.json()
        print(data)

    else:print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred : {e}")