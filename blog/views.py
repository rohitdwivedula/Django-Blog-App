from django.shortcuts import render
from .models import BlogPost, Feedback
from .gmailAPI import sendMail
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
			name_of_person = form.cleaned_data.get('name')
			email_id = form.cleaned_data.get('email')
			message_text = form.cleaned_data.get('text') 
			Feedback.objects.create(name = name_of_person, email=email_id, text = message_text)
			response = sendMail(name=name_of_person, email=email_id, text=message_text)
			if response == False:
				# mail not sent: success page is not displayed
				return HttpResponseRedirect('/')
			else:
				# success page along with Message ID displayed
				message_id = response['id']
				print(message_id)
				return HttpResponseRedirect('/submitted?id=' + message_id)				
	else:
		form = ContactForm()
	return render(request, 'blog/contact.html', {'form': form})

def about(request):
	return render(request, 'blog/about.html')

def privacy_policy(request):
	return render(request, 'blog/privacy_policy.html')	

def submitted(request):
	return render(request, 'blog/submitted.html')