import requests
import json


def add_all(token):
    try:
        req = requests.get('https://api.vk.com/method/friends.getRequests?',
                           '&out=0&access_token=' + token + '&v=5.60')
        jsn = json.loads(req.text)
        count = int(jsn["response"]["count"])

        for i in range(count):
            requests.get('https://api.vk.com/method/friends.add?',
                         '&user_id=' + str(jsn["response"]["items"][i]) + '&access_token=' + token + '&v=5.60')
    except:
        print ('Error')