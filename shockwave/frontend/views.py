from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response

def main(request):
	return render_to_response('frontend/main.html', {})

def login(request):
	return render_to_response('frontend/login.html', {})
