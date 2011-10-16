from datetime import datetime
from model import DataPoint

def format_twitter_status(status):
	   """Formats tweets into the correct format for delivery to the client
	   """
	   if status['text'].startswith('RT'):
			   return None

	   if not status['geo']:
			   return None

	   tweet = DataPoint()
	   tweet.content = status['text']
	   tweet.latitude = status['geo']['coordinates'](0)
	   tweet.longitude = status['geo']['coordinates'](1)
	   tweet.time = datetime.strptime(status['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
	   tweet.tags = map(lambda x: x['text'], status['entities']['hashtags'])

	   return tweet.json()