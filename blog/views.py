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
			# saving the object here
			f = Feedback(name = name_of_person, email=email_id, text = message_text)
			
			try:
				# Try sending email: if successful, response 
				# will be an object of type Users.messages
				# Failure in sending will cause response == False 
				response = sendMail(name=name_of_person, email=email_id, text=message_text)
				assert response!=False, "Email not sent" 
				# success page along with Message ID displayed
				print(response['id'])
				f.message_id = response['id']
				f.save()
				return render(request, 'blog/submitted.html', 
					{'message_id': response['id']})

			except:
				# acknowledgement email not sent.
				f.save()
				print("LOLOLOL")
				response = False
				return render(request, 'blog/submitted.html', {'message_id': False})
	else:
		form = ContactForm()
	return render(request, 'blog/contact.html', {'form': form})

def about(request):
	return render(request, 'blog/about.html')

def privacy_policy(request):
	return render(request, 'blog/privacy_policy.html')	

def submitted(request, message_id):
	return render(request, 'blog/submitted.html')