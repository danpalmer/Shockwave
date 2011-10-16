# Script to import csv data into the database

# Set up the Django project access
from datetime import *
import sys, os, time, math
os.environ['DJANGO_SETTINGS_MODULE'] = 'shockwave.settings'
from django.core.management import setup_environ
from shockwave import settings
setup_environ(settings)
import json
from decimal import *
from shockwave.api.models import Dataset, DatasetItem

sys.path.append(os.path.abspath('./shockwave'))

RAW_DATA_FOLDER = os.path.abspath('./import_data')
DATASET_NAME = 'glastonbury-2011'

def functiontimer(func):
	def wrapper(*arg):
		t1 = time.time()
		res = func(*arg)
		t2 = time.time()
		print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
		return res
	return wrapper

@functiontimer
def runimport():
	# Get all files to import
	dataset = Dataset.objects.get(name=DATASET_NAME)
	importfiles = os.listdir(RAW_DATA_FOLDER)
	for datafile in importfiles:
		f = open('%s/%s' % (RAW_DATA_FOLDER, datafile))
		# Iterate through xreadlines for big files
		content = json.loads(f.read())
		for x in content['results']['bindings']:
			d = DatasetItem()
			d.dataset = dataset
			d.content = x['event_name']['value']
			d.lat = Decimal(x['lat']['value'])
			d.long = Decimal(x['long']['value'])
			d.time = datetime.strptime(x['start']['value'], "%Y-%m-%dT%H:%M+01:00")
			d.tags = DATASET_NAME
			d.save()
			print "%s += %s, %s" % (DATASET_NAME, d.content, d.time)
		f.close()


if __name__ == "__main__":
	runimport()