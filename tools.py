import re
from datetime import datetime

log = 'TYPE THE URL AND PRESS CONVERT'
fg = 'gray'


def setlog(update: str, color: str):
    global log
    log = update

    global fg
    fg = color


def getlog() -> (str, str):
    global log
    global fg

    return log, fg


def namecreator(url: str):
    def takenow():
        current = datetime.now()
        currentstr = current.strftime('%Y%m%d%H%M%S')

        return currentstr

    url = url.lower()
    url = re.sub('^(https?://(www.)?)', '', url)
    url = re.sub('[^a-zA-Z\d\s./]', '', url)
    url = url.replace('/', ' ')
    url = url.replace('.', ' ')
    url = url.upper()

    ans = f'{url[:35]} {takenow()}'
    return ans
