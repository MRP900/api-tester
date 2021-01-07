import requests
import time
import html

# function to test api, takes api request as string
# Responds with success message + results if desired or with Status and error code in event of failure
# first param = string, API request URL
# second param = True(Default) - will print response
# third param = True(Default) - will return response as python dictionary
def testApi(api, result=True, format=True):

    response = requests.get(api)
    seconds = time.time()
    query_time = time.ctime(seconds)
    status = response.status_code

    if status == 200:
        print(f"Response Status: Success\nOn {query_time}\n")
        response_json = response.json()
        if result:
            print(f"{response_json}\n")
        if format:
            return response_json
    else:
        print(f"Response Status: Failed\nError: {status}\nOn {query_time}\n")


    
