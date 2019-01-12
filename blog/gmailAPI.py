from __future__ import print_function
from httplib2 import Http
from oauth2client import file, client, tools
from email.mime.text import MIMEText
from googleapiclient.discovery import build
import base64
import csv

# parts of this code are from GMail's API documentation

SCOPES = 'https://www.googleapis.com/auth/gmail.compose'

def sendMail(name, email, text):

	# authenticating and creating a service instance
	store = file.Storage('/home/rohit/Django-Blog-App/blog/token.json')
	creds = store.get()
	if not creds or creds.invalid:
		flow = client.flow_from_clientsecrets('/home/rohit/Django-Blog-App/blog/credentials.json', SCOPES)
		creds = tools.run_flow(flow, store)
	service = build('gmail', 'v1', http=creds.authorize(Http()))
	message_text = "Dear " + name + ",\nYour feedback on Django Blog has been recorded. Feedback received:"
	message_text += text;
	# creating the message and encoding as base64
	message = MIMEText(message_text)
	message['to'] = email
	message['from'] = "rohitdwivedula@gmail.com"
	message['subject'] = "Feedback on Django Blog: Recorded"
	b64_message = {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

	# sending message via GMail API: messages.send
	return send_message(service, "me", b64_message)

def send_message(service, user_id, message):
	"""Send an email message.
	Args:
		service: Authorized Gmail API service instance.
		user_id: User's email address. The special value "me"
		can be used to indicate the authenticated user.
		message: Message to be sent.
	Returns:
		Sent Message.
	"""
	try:
		message = (service.users().messages().send(userId=user_id, body=message).execute())
		print('Message Id: %s' % message['id'])
		return message
	except errors.HttpError as error:
		print('An error occurred: %s' % error)
		return False