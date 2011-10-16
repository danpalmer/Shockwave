import tornado.httpserver, tornado.websocket, tornado.web
from tornado.ioloop import PeriodicCallback
import time, optparse, pycurl, json, urllib, sys
from datetime import datetime
from model import DataPoint

# super-secret information
STREAM_URL = "https://stream.twitter.com/1/statuses/filter.json"
USER = "shockwaves_test"
PASS = "YoullNeverGuessTh1s!"

SOCKETS = []

# keywords that are being tracked
# TODO allow users to "vote" for keywords
KEYWORDS = "apple, bieber, korean gp, new zealand vs australia, inschooltheresalways, ireallyhatewhenpeople, thankstomyex, happy birthday john and edward"

class WebSocketHandler(tornado.websocket.WebSocketHandler):	
	# called upon establishing a new connection
	def open(self):
		print '> User Connected'
		self.write_message("Connected to Server")
		SOCKETS.append(self)
		
		## setup scheduler to automatically send messages
		# 		self.scheduler = PeriodicCallback(self.send_twitter_message, 500)
		# 		self.scheduler.start()
		
		# setup twitter stream
		stream = TwitterStream(self)
	  
	# called upon receiving a message from a user (shouldn't happen)
	def on_message(self, message):
		print '> Message Received %s' % message

	# called when a user closes their connection
	def on_close(self):
		print '> User Left'
		SOCKETS.remove(self)

	def send_sample_message(self):
		self.write_message("Hello darkness, my old friend")


class TwitterStream:
	def __init__(self, socket_handler):
		self.socket_handler = socket_handler
		self.buffer = ""
		self.post_params = {'track' : KEYWORDS}

		self.connection = pycurl.Curl()

		#self.conn.setopt(pycurl.VERBOSE, 1) # debugging
		self.connection.setopt(pycurl.POSTFIELDS, urllib.urlencode(self.post_params))
		self.connection.setopt(pycurl.USERPWD, "%s:%s" % (USER, PASS))
		self.connection.setopt(pycurl.URL, STREAM_URL)
		self.connection.setopt(pycurl.WRITEFUNCTION, self.on_receive)
		self.connection.perform()

	# called upon recieving a new tweet
	def on_receive(self, data):
		self.buffer += data

		# if the entire tweet has loaded up to newline (ie: not a fragment)
		if data.endswith("\r\n") and self.buffer.strip():
			content = json.loads(self.buffer)
			self.buffer = "" 	# reset buffer
			
			if 'text' in content:
				if len(SOCKETS) is not 0:
					for socket in SOCKETS:
						tweet = format_twitter_status(content)
						if tweet:
							socket.write_message(tweet)
						else:
							print "NONE"
						# socket.write_message(content)
				else:
					return
					
application = tornado.web.Application([
	(r'/bieber', WebSocketHandler),
])	

def format_twitter_status(status):
	"""Formats tweets into the correct format for delivery to the client
	"""
	# if status['text'].startswith('RT'):
	# 		return None
	
	if not status['geo']:
		return None
	
	print "this works"
	tweet = DataPoint()
	tweet.content = status['text']
	tweet.latitude = status['geo']['coordinates'][0]
	tweet.longitude = status['geo']['coordinates'][1]
	tweet.time = datetime.strptime(status['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
	tweet.tags = map(lambda x: x['text'], status['entities']['hashtags'])
	print "more stuff"
	return tweet.json()
		

# run on launch
if __name__ == "__main__":
	# extract port number from arguments
	opt_parser = optparse.OptionParser()
	(options, args) = opt_parser.parse_args()
	if( not args ):
		opt_parser.error("No port argument was given.")
	if( not args[0].isdigit() ):
		opt_parser.error("Port was not a number")		
	
	# setup HTTP server for WebSocket on port given in args
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(int(args[0]))
	
	# print out intro for user
	message = ["SHOCKWAVE LIVE SERVER is now running on port " + args[0], "Close with ctrl + c"]
	stars = "*" * len(message[0])
	print  stars + "\n" + message[0] + "\n" + message[1].center(len(message[0])) + '\n' + stars
	
	# begin IOloop
	loop_instance = tornado.ioloop.IOLoop.instance()
	try:
		loop_instance.start()
	except KeyboardInterrupt:
		print "... Exiting SHOCKWAVE LIVE SEVER."
		sys.exit(0)