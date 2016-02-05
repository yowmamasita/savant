from requests import get, head
import urllib
import re

FORMATS = ('video/x-flv', 'video/mp4', 'video/webm')
PLAYBACK_REGEX = r'https\:\/\/[^\/]*\/videoplayback[^\"\|]*'
urlencode = lambda url: re.sub(r'\\u[0]+', '%', url)


def get_link(drive_url, video_format='video/mp4'):
    if video_format not in FORMATS:
        raise Exception("Unsupported filetype (%s)" % ', '.join(FORMATS))
    r = get(drive_url)
    regex = re.compile(PLAYBACK_REGEX)
    matches = regex.findall(r.text)
    urls = [urllib.unquote(urlencode(u)) for u in matches]
    for url in urls:
        r = head(url)
        if r.headers['content-type'] == video_format:
            return url
