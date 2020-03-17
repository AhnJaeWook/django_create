from django.shortcuts import render, redirect
from .forms import CreateBlog

# Create your views here.
def home(request):
    return render(request, "home.html")

def new(request):

    if request.method == "POST":
        create = CreateBlog(request.POST)

        if create.is_valid():
            create.save()
            return redirect('/')
        else:
            return redirect('new/')
    else:
        create = CreateBlog()
        
        return render(request, "new.html", {'create':create})