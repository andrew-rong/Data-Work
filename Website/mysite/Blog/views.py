from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Post


# def home(request):
#    return render(request, 'Home.html', {})


class HomeView(ListView):
    model = Post
    template_name = "Home.html"


class Detail_view(DetailView):
    model = Post
    template_name = 'post_detail.html'


def about(request):
    return render(request, 'about.html', {'title': 'About'})


def contact(request):
    return render(request, 'contact.html', {'title': "Contact"})
