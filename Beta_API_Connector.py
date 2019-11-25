import requests
import json

# build connector
class Beta(object):
    def __init__(self):
        self.token = ''
        self.address = 'https://gorest.co.in/public-api/users'
        self.max_calls = 30

    def get_users(self):  # function to return list of users
        headers = {
            'Authorization': 'Bearer {}'.format(self.token)
        }

        ret_users = requests.get(self.address, headers=headers).json()
        if ret_users['_meta']['code'] == 200:
            ret_users = json.dumps(ret_users, indent=4)  # format json in readable format
            print(ret_users)
            return ret_users
        else:
            print("Call failed with response code {}".format(ret_users['_meta']['code']))

first_call = Beta()
first_call.get_users()
