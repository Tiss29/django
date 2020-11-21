from django.shortcuts import render
from .models import post
from django.views.generic import ListView,DetailView

def home(request):
 contest={
       'posts':post.objects.all()
   }
 return render(request,'blog/home.html',contest)

class PostListView(ListView):
    model = post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date']

class PostDetailView(ListView):
    model = post
    
def about(request):
  return render(request,'blog/about.html',{'title':'about'})
