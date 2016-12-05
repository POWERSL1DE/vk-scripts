def check(jsn):
    if jsn is not None:
        str_jsn = str(jsn)
        if "User authorization failed: invalid access_token" in str_jsn:
            print ('Invalid access_token')
        else:
            print ('Unknown error, json: ' + str_jsn)


def status_code_ok(jsn):
    response = jsn["response"]
    if response == "1" or "2" or "4":
        return True
    else:
        print ('Unknown error, json: ' + jsn)
        return False


