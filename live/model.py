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
			   # return json.dumps({
			   # 					   "content":self.content,
			   # 					   "latitude":'%s' % self.latitude.to_eng_string(),
			   # 					   "longitude":'%s' % self.longitude.to_eng_string(),
			   # 					   "time":str(time.mktime(self.time.timetuple())),
			   # 					   "tags":self.tags
			   # 			   })
			x = {
					   "content":self.content,
					   "latitude":self.latitude,
					   "longitude":self.longitude,
					   "time":str(time.mktime(self.time.timetuple()))
			   }
			return json.dumps(x)

