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
			"content":self.content,
			"latitude":'%s' % self.lat.to_eng_string(),
			"longitude":'%s' % self.long.to_eng_string(),
			"time":str(time.mktime(self.time.timetuple())),
			"tags":self.tags
		})