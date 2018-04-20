from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

class Api:
    def __init__(self):
        clientId = 'rWlrkeV8HRJ6FvoBfPrhzR1TdqNuY9vMN856YZ8v'
        clientSecret = 'wY8pwK2J7FrqVGZx2oL4cvayzEP7Ab6JILBho0JKH6jNRiDEk3'
        oAuth = OAuth2Session(client = BackendApplicationClient(clientId))
        token = oAuth.fetch_token(token_url='https://api.everypixel.com/oauth/token', auth=(clientId, clientSecret))
        self.api = OAuth2Session(clientId, token=token)

    def get_score_from_file(self, imageName):
        with open(imageName, 'rb') as image:
            data = {'data' : image}
            rawQuality = self.api.post('https://api.everypixel.com/v1/quality', files=data).json()
            quality = rawQuality['quality']['score']
            score = quality*100
            return score

    def get_score_from_web(self, urlName):
        params = {'url' : urlName}
        rawQuality = self.api.get('https://api.everypixel.com/v1/quality', params=params).json()
        quality = rawQuality['quality']['score']
        score = quality*100
        return score
