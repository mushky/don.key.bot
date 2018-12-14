#!/usr/bin/env python
# runner.py

import sys

from twitter_bot import BotRunner
from settings import MyBotSettings as Settings

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("You must specify a single command, either 'post_message' or 'reply_to_mentions'")
        result = 1
    else:
        result = BotRunner().go(Settings(), sys.argv[1])
    sys.exit(result)
