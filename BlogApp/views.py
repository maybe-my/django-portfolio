from django.shortcuts import render, get_object_or_404

from BlogApp.models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "BlogApp/index.html", {'posts': posts})


def detail(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    return render(request, 'BlogApp/detail.html', {'post':post})