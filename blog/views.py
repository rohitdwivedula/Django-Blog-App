from django.shortcuts import render
from .models import BlogPost, Feedback
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from django.http import HttpResponseRedirect

def post_list(request):
	posts = BlogPost.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():	
			Feedback.objects.create(name = form.cleaned_data.get('name'), 
				email=form.cleaned_data.get('email'), 
				text =form.cleaned_data.get('text'))
			return HttpResponseRedirect('/submitted')
	else:
		form = ContactForm()
	return render(request, 'blog/contact.html', {'form': form})

def about(request):
	return render(request, 'blog/about.html')

def privacy_policy(request):
	return render(request, 'blog/privacy_policy.html')	

def submitted(request):
	return render(request, 'blog/submitted.html')