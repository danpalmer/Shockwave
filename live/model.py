import json

class DataPoint():
	def __init__():
		self.content = None
		self.latitude = None
		self.longitude = None
		self.time = None
		self.tags = None
	
	def json(self):
		return json.dumps({
			"content":content,
			"latitude":latitude,
			"longitude":longitude,
			"time":time,
			"tags":tags
		})