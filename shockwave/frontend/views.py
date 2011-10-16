from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response

def main(request):
	return render_to_response('frontend/main.html', {})

def sample(request):
	return HttpResponse("""[{\"content\": \"EVERYONE LOVES BIEBER awks that I don't\", \"latitude\": 53.2434384, \"longitude\": -6.6562406, \"time\": \"1318717107\"},
{\"content\": \"@Dylanswift619 everybody likes bieber...really!!\\n\\nHahaha\\n\\nYa right\", \"latitude\": 49.28914642, \"longitude\": -123.12394714, \"time\": \"1318717202\"},
{\"content\": \"\u201c@fernimaq: Felicitaciones a @lanonna_ por el backstage de Justin Bieber. Un lujo de entretenci\u00f3n. http://t.co/7Zo3qHvw\u201d / @dgmedios\", \"latitude\": -33.46447888, \"longitude\": -70.61177296, \"time\": \"1318717227\"},
{\"content\": \"I'm getting off twitter before I see lame comments about the trends. Specifically \\"everyone loves Bieber\\"\", \"latitude\": 29.64605249, \"longitude\": -82.3738931, \"time\": \"1318717240\"},
{\"content\": \"EVERYONE LOVES BIEBER? That's a lie. I don't\", \"latitude\": 39.96948034, \"longitude\": -86.01122791, \"time\": \"1318717323\"},
{\"content\": \"\u201c@Renolander: Igual Justin Bieber es rico. Toda la plata que tiene...\u201d :$\", \"latitude\": -33.48746844, \"longitude\": -70.57728042, \"time\": \"1318717529\"}]""")