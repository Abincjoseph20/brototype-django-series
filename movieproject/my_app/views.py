from django .shortcuts import render,redirect
from . models import MovieInfo
from.forms import MovieForm
# Create your views here.

def edit(request):
    return render(request,'edit.html')

def create(request):
    frm=MovieForm()
    if request.POST:
        frm=MovieForm(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm=MovieForm()

    return render(request,'create.html',{'frm':frm})


def list(request):
    movie_list = MovieInfo.objects.all()
    print(movie_list)
    return render(request, 'list.html', {'movies':movie_list})

def blanklayout(request):
    return render(request,'blanklayout.html')