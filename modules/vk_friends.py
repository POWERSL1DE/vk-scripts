from other import vk_check_errors as vce
import requests
import json
import time


def add_all(token):
    try:
        # Get requests list\
        req = requests.get('https://api.vk.com/method/friends.getRequests?',
                           '&out=0&access_token=' + token + '&v=5.60')
        jsn = json.loads(req.text)
        # Get count of requests
        count = int(jsn["response"]["count"])
        # Add each person
        for i in range(count):
            time.sleep(0.3)
            # User id
            usr = str(jsn["response"]["items"][i])
            req = requests.get('https://api.vk.com/method/friends.add?',
                               '&user_id=' + usr + '&access_token=' + token + '&v=5.60')
            # Check response
            if vce.status_code_ok(json.loads(req.text)):
                print (usr + ' user was added\n')

    except KeyError:
        # Check response for error
        vce.check(jsn)
    except:
        print ('Error')


def unfollow_all(token):
    try:
        # Get follow list
        req = requests.get('https://api.vk.com/method/friends.getRequests?',
                           '&out=1&access_token=' + token + '&v=5.60')
        jsn = json.loads(req.text)
        # Get count of requests
        count = int(jsn["response"]["count"])
        # Unfollow from all pers
        for i in range(count):
            time.sleep(0.3)
            # User id
            usr = str(jsn["response"]["items"][i])
            req = requests.get('https://api.vk.com/method/friends.delete',
                               '&user_id=' + usr + '&access_token=' + token + '&v=5.60')
            # Check response
            if vce.status_code_ok(json.loads(req.text)):
                print (usr + ' user was removed\n')
    except KeyError:
        # Check response for error
        vce.check(jsn)
    except:
        print ('Error')