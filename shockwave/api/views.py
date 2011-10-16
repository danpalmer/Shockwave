from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from models import *

def get_dataset_info(request, term):
	term = term.replace(' ', ',')
	dataset = Dataset.objects.get(name=term)
	
	if not dataset:
		return HttpResponse('{"url":"%s", "stream":"true"}' % ("http://shockwave.dapl.me:8000/" + term))
	
	return HttpResponse('{"url":"%s", "stream":"false"}' % ("http://odin.local/dataset/" + term))

def get_dataset(request, term):
	term = term.replace(' ', ',')
	dataset = Dataset.objects.get(name=term)
	
	if not dataset:
		return HttpResponse("Not found", status=404)
	
	items = DatasetItem.objects.filter(dataset=dataset)
	response = render_to_response('api/dataset.json', {'data':items})
	response['Content-type'] = 'application/json'
	response.content = response.content.replace(',]',']')
	return response