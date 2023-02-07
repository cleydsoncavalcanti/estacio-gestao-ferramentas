from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .services.serializers import TodoSerializer 
from rest_framework import viewsets      
from .models.booking import Booking

def home(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s  </body> </html>" % now
    # return HttpResponse(html)
    return render(request,'contas/home.html')

class TodoView(viewsets.ModelViewSet):  
    serializer_class = TodoSerializer   
    queryset = Booking.objects.all()     
