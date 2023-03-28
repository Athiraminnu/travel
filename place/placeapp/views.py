from django.shortcuts import render, redirect
from .models import place2visit
from . forms import form1

# Create your views here.
def home(request):
    var = place2visit.objects.all()
    var1 = {
        'result': var}

    return render(request, 'home.html', var1)

def detail(request, movie_id):
    var2 = place2visit.objects.get(id=movie_id)
    return render(request, 'detail.html', {'result': var2})

def add(request):
    if request.method == 'POST':
        NAME = request.POST.get('name',)
        ABOUT = request.POST.get('desc',)
        IMG = request.FILES['img']

        var = place2visit(name=NAME, about=ABOUT, img=IMG)
        var.save()
    return render(request, 'add.html')

def update( request,id ):
    movie = place2visit.objects.get(id=id)
    form = form1(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})

def delete( request,id ):
    if request.method == 'POST':
        var = place2visit.objects.get(id=id)
        var.delete()
        return redirect('/')
    return render(request, 'delete.html' )
