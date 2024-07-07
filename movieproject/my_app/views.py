
from django .shortcuts import render,redirect
from . models import MovieInfo
from.forms import MovieForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login/')
def edit(request,pk):
    instance_tobedit = MovieInfo.objects.get(pk=pk)

    if request.POST:
        title = request.POST.get('title')
        year = request.POST.get('year')
        decription = request.POST.get('decription')
        imgs = request.FILES.get('imgs')

        instance_tobedit.title = title
        instance_tobedit.year = year
        instance_tobedit.decription = decription
        instance_tobedit.imgs = imgs
        instance_tobedit.save()

    frm=MovieForm(instance=instance_tobedit)
    return render(request,'create.html',{'frm':frm})


@login_required(login_url='login/')
def create(request):
    frm=MovieForm()
    if request.POST:
        frm=MovieForm(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
    else:
        frm=MovieForm()
    return render(request,'create.html',{'frm':frm})



@login_required(login_url='login/')
def list(request):
    movie_list = MovieInfo.objects.all()
    print(movie_list)
    return render(request, 'list.html', {'movies':movie_list})



@login_required(login_url='login/')
def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_list = MovieInfo.objects.all()
    return render(request, 'list.html', {'movies':movie_list})

def blanklayout(request):
    return render(request,'blanklayout.html')