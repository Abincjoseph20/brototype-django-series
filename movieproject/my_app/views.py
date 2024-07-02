from django .shortcuts import render,redirect
from . models import MovieInfo
from.forms import MovieForm
# Create your views here.

def edit(request,pk):
    instance_tobedit = MovieInfo.objects.get(pk=pk)
    if request.POST:
        title = request.POST.get('title')
        year = request.POST.get('year')
        decription = request.POST.get('decription')

        instance_tobedit.title = title
        instance_tobedit.year = year
        instance_tobedit.decription = decription
        instance_tobedit.save()

    frm=MovieForm(instance=instance_tobedit)
    return render(request,'create.html',{'frm':frm})




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


def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_list = MovieInfo.objects.all()
    return render(request, 'list.html', {'movies':movie_list})

def blanklayout(request):
    return render(request,'blanklayout.html')