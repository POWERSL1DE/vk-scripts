from other import vk_check_errors as vce
import requests
import json
import time
import webbrowser
import os


def choose_script(parsed_args):
    if bool(getattr(parsed_args, 'list')):
        print ('1 - Add all friends\n2 - Unfollow from all people\n')
    else:
        script = getattr(parsed_args, 'script')
        token = getattr(parsed_args, 'token')
        ids = getattr(parsed_args, 'ids')
        if script == '1':
            add_all(token)
        elif script == '2':
            unfollow_all(token)
        elif script == '3':
            add_by_ids(token, ids)


def add_all(token):
    print ("Script 'add_all' was started")
    try:
        # Get requests list
        req = requests.get('https://api.vk.com/method/friends.getRequests?',
                           'out=0&need_viewed=1&access_token=' + token + '&v=5.60')
        jsn = json.loads(req.text)
        # Get count of requests
        count = int(jsn['response']['count'])
        # Add each person
        for i in range(count):
            time.sleep(0.3)
            # User id
            usr = str(jsn['response']['items'][i])
            req = requests.get('https://api.vk.com/method/friends.add?',
                               'user_id=' + usr + '&access_token=' + token + '&v=5.60')
            jsn = json.loads(req.text)
            # Check response
            status = vce.status_code_ok(jsn)
            if status == 'ok':
                print (usr + ' user was added')
            # Captcha needed
            elif status == 'captcha':
                captcha_confirm(token, jsn, 'friends.add', usr, ' user was added')
        print ("Script 'add_all' was completed")
    except:
        # Check response for error
        vce.check(jsn)


def unfollow_all(token):
    print ("Script 'unfollow_all' was started")
    try:
        # Get follow list
        req = requests.get('https://api.vk.com/method/friends.getRequests?',
                           'out=1&access_token=' + token + '&v=5.60')
        jsn = json.loads(req.text)
        # Get count of requests
        count = int(jsn['response']['count'])
        # Unfollow from all pers
        for i in range(count):
            time.sleep(0.3)
            # User id
            usr = str(jsn['response']['items'][i])
            req = requests.get('https://api.vk.com/method/friends.delete',
                               'user_id=' + usr + '&access_token=' + token + '&v=5.60')
            jsn = json.loads(req.text)
            # Check response
            status = vce.status_code_ok(jsn)
            if status == 'ok':
                print (usr + ' user was removed')
            # Captcha needed
            elif status == 'captcha':
                captcha_confirm(token, jsn, 'friends.delete', usr, ' user was removed')
        print ("Script 'unfollow_all' was completed")
    except:
        # Check response for error
        vce.check(jsn)


def add_by_ids(token, ids):
    print ("Script 'add_by_ids' was started")
    try:
        # Add persons
        for i in range(len(ids)):
            time.sleep(1)
            req = requests.get('https://api.vk.com/method/friends.add?',
                               'user_id=' + str(ids[i]) + '&access_token=' + token + '&v=5.60')
            # Check response
            jsn = json.loads(req.text)
            status = vce.status_code_ok(jsn)
            if status == 'ok':
                print (str(ids[i]) + ' user was added')
            # Captcha needed
            elif status == 'captcha':
                captcha_confirm(token, jsn, 'friends.add', str(ids[i]), ' user was added')
        print ("Script 'add_by_ids' was completed")
    except:
        # Check response for error
        vce.check(jsn)


def captcha_confirm(token, jsn, method, usr, message):
    try:
        captcha = True
        while captcha:
            if raw_input('Captcha needed. Open browser ? (y\\n)  ') == 'y':
                # Open captcha img without webbrowser notifications to console
                savout = os.dup(1)
                os.close(1)
                os.open(os.devnull, os.O_RDWR)
                webbrowser.open(jsn['error']['captcha_img'])
                os.dup2(savout, 1)
                # Get captcha
                captcha_key = raw_input('Captcha:')
                # Requests with captcha
                req = requests.get('https://api.vk.com/method/' + method +
                                   '?user_id=' + usr + '&captcha_sid=' +
                                   str(jsn['error']['captcha_sid']) +
                                   '&captcha_key=' + captcha_key + '&access_token=' + token + '&v=5.60')
                # Check response
                jsn = json.loads(req.text)
                # Get status code
                status = vce.status_code_ok(jsn)
                if status == 'ok':
                    print (usr + message)
                    # Break while
                    captcha = False
            else:
                raise SystemExit
    except SystemExit:
        print ('Bye')
        quit()
    except:
        vce.check(jsn)

