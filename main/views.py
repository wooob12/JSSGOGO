from django.shortcuts import render, redirect, get_object_or_404
from .forms import JssForm
from .models import Jasoseol
from django.http import Http404

# Create your views here.

def index(request):
    all_jss = Jasoseol.objects.all()
    return render(request, 'index.html', {'all_jss':all_jss})


def create(request):
    if request.method == "POST":
        filled_form = JssForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index')
    jss_form = JssForm()
    return render(request, 'create.html', {'jss_form':jss_form})

def detail(request, jss_id):
    
    # try:
    #     my_jss = Jasoseol.objects.get(pk=jss_id)
    # except:
    #     raise Http404
    my_jss = get_object_or_404(Jasoseol, pk=jss_id)

    return render(request, 'detail.html', {'my_jss':my_jss})

def delete(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    my_jss.delete()
    return redirect('index')


def update(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    jss_form = JssForm(instance=my_jss)
    if request.method == "POST":
        updated_form = JssForm(request.POST, instance=my_jss)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')

    return render(request, 'create.html', {'jss_form' : jss_form})