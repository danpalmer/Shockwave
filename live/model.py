import json
import time

class DataPoint():
	def __init__(self):
		self.content = None
		self.latitude = None
		self.longitude = None
		self.time = None
		self.tags = None
	
	def json(self):
		return json.dumps({
			"content":self.content,
			"latitude":self.latitude,
			"longitude":self.longitude,
			"time":str(time.mktime(self.time.timetuple()))
		})