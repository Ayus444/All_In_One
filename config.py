#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6126007753:AAE7TAYLUTgCM1Fm9Y90YvLpkQmKqkQm5hE")
    API_ID = int(os.environ.get("API_ID", "27881923"))
    API_HASH = os.environ.get("API_HASH", "79abda5e46a51fc0dce1313f2548ce19")
    AUTH_USERS = "6059771769"
