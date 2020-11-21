from django.urls import path
from .views import PostListView,PostDetailView
from . import views
urlpatterns=[
           path('', PostListView.as_view(), name='blog_home'),
           path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
           path('about/', views.about,name='blog_about'),
]
