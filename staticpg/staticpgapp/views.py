from django.shortcuts import render

from .models import travelinfo


# Create your views here.
def demo(request):
    var = travelinfo.objects.all()
    return render(request,'index.html',{'result': var})
