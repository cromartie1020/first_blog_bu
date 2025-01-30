from django.shortcuts import render, get_object_or_404
from . models import Blog

def home(request):
    blogs=Blog.objects.all()
    return render(request, 'blog/list.html',{'blogs':blogs})

def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/detail.html', {'blog': blog})