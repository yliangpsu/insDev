from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from Insta.models import Post
# Create your views here.

class HelloDjango(TemplateView):
    template_name = 'home.html'

class PostView(ListView):
    model = Post
    template_name = 'posts.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'