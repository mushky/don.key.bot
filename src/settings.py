import os
from twitter_bot import Settings

class MyBotSettings(Settings):
    def __init__(self):
        super().__init__()

        self.OAUTH_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
        self.OAUTH_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
        self.CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
        self.CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET_KEY')

        self.MESSAGE_PROVIDER = 'provider.MyMessageProvider'
