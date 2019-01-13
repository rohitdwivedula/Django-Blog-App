# About

This is a Django application that started out as the basic blog from the DjangoGirls tutorial. Right now, these are the views/pages in the website:

* '/' or the Home Page: Displays a list of blogposts on the server.
* '/post/<integer: id>': displays the blog post which has primary key = id. 
* '/about','/privacy-policy': two static pages
* '/contact': a contact form that takes user feedback and saves it in the database as well as sending an email to the user using GMail API.

# Using GMail API

*The GMail API is used on the Contact page to send email to users who give feedback. Every time a user gives feedback, it is saved to Django DB and an email confirmation is also sent.*

1. Follow the instructions from the [GMail Python API QuickStart](https://developers.google.com/gmail/api/quickstart/python)
2. Place the "credentials.json" and "token.json" files in the working directory. (blog/) - these files will be generated after you follow the QuickStart instructions
3. Update the email address in gmailAPI.py file to your email. 
4. Run the server.

# Further Improvements

* Add option to take db backups and save on DropBox
