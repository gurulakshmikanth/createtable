from django.shortcuts import render

# Create your views here.
from app.models import *
def display_topics(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}

    return render(request,'display_topics.html',context=d)