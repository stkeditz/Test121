import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6795999766:AAGt8T3l_4d4L5_klGJdhOpGW5-_NeivuLQ")
    API_ID = int(os.environ.get("API_ID", "14621169"))
    API_HASH = os.environ.get("API_HASH", "61e480d82ff09acbf967ccea4fa2884f")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1002182918708")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
