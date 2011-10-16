from django.db import models
import json, time

class Dataset(models.Model):
	name = models.CharField(max_length=100, unique=True)
	
	def __unicode__(self):
		return self.name

class DatasetItem(models.Model):
	dataset = models.ForeignKey('Dataset')
	content = models.CharField(max_length=300)
	lat = models.DecimalField(decimal_places=14, max_digits=16)
	long = models.DecimalField(decimal_places=14, max_digits=16)
	time = models.DateTimeField()
	tags = models.CharField(max_length=300)
	
	def json(self):
		return json.dumps({
			"content":self.content,
			"latitude":'%s' % self.lat.to_eng_string(),
			"longitude":'%s' % self.long.to_eng_string(),
			"time":str(time.mktime(self.time.timetuple())),
			"tags":self.tags
		})