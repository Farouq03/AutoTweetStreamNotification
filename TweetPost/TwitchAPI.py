import requests
import json

headers = {
    'Authorization': 'Bearer YOUR TOKEN',
    'Client-Id': 'YOUR CLIENT ID',
}

params = {
    'user_login': [
        'YOUR CHANNEL NAME'
    ],
}

response = requests.get('https://api.twitch.tv/helix/streams', params=params, headers=headers) #if the user currently not LIVE, you will not receive any response 

def userCheck():
    try :
        datajson = response.json()
        if 'data' in datajson:
            if datajson["data"][0]["type"] != "":
                return True
            else:
                return False
    
    except :
        return False

