from django.shortcuts import render
from .models import BlogPost
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def post_list(request):
	posts = BlogPost.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
