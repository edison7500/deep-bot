import logging

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Text'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_DATA_DIR = r'/Users/xiejiaxin/PycharmProjects/jiaxin.im/2b/data'
BOT_EXTRA_PLUGIN_DIR = r'/Users/xiejiaxin/PycharmProjects/jiaxin.im/2b/plugins'

BOT_LOG_FILE = r'/Users/xiejiaxin/PycharmProjects/jiaxin.im/2b/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('@jiaxin',)  # !! Don't leave that to "@CHANGE_ME" if you connect your errbot to a chat system !!

BOT_ASYNC = True
BOT_ASYNC_POOLSIZE = 10

BOT_EXTRA_STORAGE_PLUGINS_DIR = r'/Users/xiejiaxin/PycharmProjects/jiaxin.im/err-storage-redis'
STORAGE = 'Redis'
STORAGE_CONFIG = {
    'host': '10.0.0.99',
    'port': 6379,
    'db': 0,
    # 'password': 'xyz123',
}

GEOIP_PATH = r"/Users/xiejiaxin/PycharmProjects/jiaxin.im/2b/GeoLite2-City_20180403/GeoLite2-City.mmdb"
