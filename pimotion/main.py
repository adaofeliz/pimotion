from requests.exceptions import HTTPError, RequestException
from pimotion import PiMotion
from slackclient import SlackClient
from datetime import datetime
import calendar
import ConfigParser
import dropbox

Config = ConfigParser.ConfigParser()
Config.read('settings.cfg')

def callback(path):
    try:
        client = dropbox.client.DropboxClient(Config.get('dropbox', 'api_token'))

        # File Name
        fileName = str(calendar.timegm(datetime.now().utctimetuple())) + '.jpg'

        # Upload and Generate Media Link
        response = client.put_file(fileName, open(path, 'rb'))
        metadata = client.media(response['path'])

        # Notify Slack
        slack = SlackClient(Config.get('slack', 'token'))
        slack.api_call(
            "chat.postMessage", 
            channel=Config.get('slack', 'channel'), 
            text="Motion Detected :camera_with_flash:: " + str(metadata['url']),
            unfurl_links="true",
            username='PiMotion', 
            icon_emoji=':video_camera:')

    except HTTPError, e:
        print 'ERROR: '
        print '  STATUS: %s' % client.last_response.status
        print '  HEADERS: %s' % client.last_response.headers
        print '  BODY: %s' % client.last_response.json

motion = PiMotion(verbose=True, post_capture_callback=callback)
motion.start()