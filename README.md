# About

This is a Django application that started out as the basic blog from the DjangoGirls tutorial. Right now, these are the views/pages in the website:

* '/' or the Home Page: Displays a list of blogposts on the server.
* '/post/<integer: id>': displays the blog post which has primary key = id. 
* '/about','/privacy-policy': two static pages
* '/contact': a contact form that takes user feedback and saves it in the database as well as sending an email to the user using GMail API.

# Further Improvements

* Add option to take db backups and save on DropBox
