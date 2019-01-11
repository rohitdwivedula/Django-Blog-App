from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(label='Your name', max_length = 100)
	email = forms.EmailField(label='Your email')
	text = forms.CharField(
		label = 'Feedback',
		required=True,
		widget = forms.Textarea
	)
