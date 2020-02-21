from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Image
from .forms import UserRegisterForm, PostPictureForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def home (request):
    posts = Image.objects.all()
    
    return render(request, 'index.html', { 'posts': posts })



def image_form(request):
    if request.method == 'POST': 
        form = PostPictureForm(request.POST, request.FILES) 
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = request.user.profile
            form.save()
            return redirect('home') 
    else: 
        form = PostPictureForm() 
    return render(request, 'image_form.html', {'form' : form}) 


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})