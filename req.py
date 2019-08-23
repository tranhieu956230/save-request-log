import requests
from functools import wraps
from copy import copy


def save_request_log(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        print("save request payload")
        resp = func(*args, **kwargs)
        print("save response")
        return resp

    return decorated


copy_get = requests.get


@save_request_log
def override_get(*args, **kwargs):
    return copy_get(*args, **kwargs)


requests.get = override_get

