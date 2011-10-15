import pycurl, json, urllib

STREAM_URL = "https://stream.twitter.com/1/statuses/filter.json"
USER = "shockwaves_test"
PASS = "YoullNeverGuessTh1s!"

KEYWORDS = "ThanksToMyEx"

class Client:
	def __init__(self):
		self.buffer = ""
		self.post_params = {'track' : KEYWORDS}
		
		self.conn = pycurl.Curl()
		
		#self.conn.setopt(pycurl.VERBOSE, 1)
		self.conn.setopt(pycurl.POSTFIELDS, urllib.urlencode(self.post_params))
		self.conn.setopt(pycurl.USERPWD, "%s:%s" % (USER, PASS))
		self.conn.setopt(pycurl.URL, STREAM_URL)
		self.conn.setopt(pycurl.WRITEFUNCTION, self.on_receive)
		self.conn.perform()

	def on_receive(self, data):
		self.buffer += data
		
		# if the entire tweet has loaded (ie: not just a bit of it)
		if data.endswith("\r\n") and self.buffer.strip():
			content = json.loads(self.buffer)
			self.buffer = ""
			
			if 'text' in content:
				print content['text']

client = Client()