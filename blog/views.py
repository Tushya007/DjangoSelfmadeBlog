from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogModel
from .forms import BlogCreateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login/")
def home_page_view(request):
    obj = reversed(BlogModel.objects.all())
    userLoggedIn = request.user.is_authenticated
    context={
        "objects":obj,
        "logIn":userLoggedIn
    }
    return render(request,"blogs/home_page.html",context)

@login_required(login_url="../../login/")
def blog_create_view(request):
    form = BlogCreateForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        form = BlogCreateForm()
        return redirect("/")
    context = {
        "form":form 
    }
    return render(request,"blogs/blog_create.html",context)