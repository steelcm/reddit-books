import time
import requests
import requests.auth
import praw

class PrawUtil:
    def __init__(self, clientId, clientSecret):
        self.clientId = clientId
        self.clientSecret = clientSecret

    def userAgent(self, username):
        return "RedditBooks/0.1 by " + username

    def getAccessToken(self, username, password):
        client_auth = requests.auth.HTTPBasicAuth(self.clientId, self.clientSecret)
        post_data = {"grant_type": "password", "username": username, "password": password}
        headers = {"User-Agent": self.userAgent(username)}
        response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
        return response.json()


# todo: move this into config
username = ""
password = ""
clientId = "6fr2-IRsBOxfRA"
clientSecret = ""


util = PrawUtil(clientId, clientSecret)
print util.getAccessToken(username, password)

