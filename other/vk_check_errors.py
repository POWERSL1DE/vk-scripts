def check(jsn):
    if jsn is not None:
        str_jsn = str(jsn)
        if 'User authorization failed: invalid access_token' in str_jsn:
            print ('Invalid access_token')
        else:
            print ('Unknown error, json: ' + str_jsn)


def status_code_ok(jsn):
    try:
        if (jsn['response'] == '1' or '2' or '4') or (jsn['response']['success'] == 1 or 2 or 4):
            return 'ok'
        else:
            print ('Unknown error, json: ' + jsn)
            return 'err'
    except:
        if 'captcha_sid' in str(jsn):
            return 'captcha'
        else:
            print ('Unknown error, json: ' + jsn)
            return 'err'

