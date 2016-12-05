from other import vk_check_errors as vce
import requests
import json
import time


def choose_script(parsed_args):
    if bool(getattr(parsed_args, 'list')):
        print ('1 - Add all friends\n2 - Unfollow from all people\n')
    else:
        script = getattr(parsed_args, 'script')
        token = getattr(parsed_args, 'token')
        if script == '1':
            print token
            add_all(token)
        elif script == '2':
            print token
            unfollow_all(token)


def add_all(token):
    print ('Script "add_all" was started')
    try:
        # Get requests list
        req = requests.get('https://api.vk.com/method/friends.getRequests?',
                           '&out=0&need_viewed=1&access_token=' + token + '&v=5.60')
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

        print ('Script "add_all" was completed')

    except:
        # Check response for error
        vce.check(jsn)


def unfollow_all(token):
    print ('Script "unfollow_all" was started')
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
        print ('Script "unfollow_all" was completed')
    except:
        # Check response for error
        vce.check(jsn)