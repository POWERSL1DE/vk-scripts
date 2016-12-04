def check(jsn):
    if jsn is not None:
        str_jsn = str(jsn)
        if "User authorization failed: invalid access_token" in str_jsn:
            print ('Invalid access_token')
        elif "" in str_jsn:
            print ('Unknown error, json: ' + str_jsn)


def status_code_ok(jsn):
    response = jsn["response"]
    if "success" and ("1" or "2" or "3") in response:
        return True
    else:
        print ('Unknown error, json: ' + jsn)
        return False


