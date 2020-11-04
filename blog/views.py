from django.shortcuts import render
from .models import post
# Create your views here.

def home(request):
 contest={
       'posts':post.objects.all()
   }
 return render(request,'blog/home.html',contest)
def about(request):
  return render(request,'blog/about.html',{'title':'about'})
