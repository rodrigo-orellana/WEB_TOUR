#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
from django.shortcuts import render
from .models import Visita
from django.conf import settings
def index(request):
	# View code here...
    visita=Visita.objects.all();
    c = {'foo': visita,
    	 'MEDIA': settings.MEDIA_URL
    	}
    	#MEDIA_URL
    return render(request, 'index.html',c)