# coding=utf-8

import time
from collections import deque

timeframe = yui.config_val('ratelimit', 'timeframe', default=60.0)
max_msg = yui.config_val('ratelimit', 'messages', default=6.0)
ignore_minutes = yui.config_val('ratelimit', 'ignoreMinutes', default=3.0)
ignore_seconds = 60.0 * ignore_minutes

buffers = {}


@yui.event('pre_recv')
def ratelimit(user, is_cmd):
    if not is_cmd:
        return

    now = time.time()
    if user not in buffers.keys():
        buffers[user] = deque([], maxlen=max_msg)

    if len(buffers[user]) < buffers[user].maxlen or now - buffers[user][0] > timeframe:
        buffers[user].append(now)
        return

    yui.ignore(ignore_seconds, user.nick)
    yui.send_notice(user.nick, "You will be ignored for %d minutes." % ignore_minutes)
    return False
