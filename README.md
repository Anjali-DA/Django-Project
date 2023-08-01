# Django-Project
Getting Started with Django

 
## Installation:

Created views.py, index.html, index2.html
Installed Django in Pycharm IDE
Imported HttpResponse from HTTP and render from shortcuts( in views.py file)
Imported views in urls.py
python Project1/manage.py runserver
By running the server we get an http link: *http://127.0.0.1:8000/*

## Tools used in Django

Bootstrap (getbootstrap) 
Introduction
Navbar
Alert
Floating labels for introducing the comment section

## Changes made in files:

Creating another ‘analyze file’ named analyze2.html [reason: to have a backup of our old code stored in analyze.html]
Creating another index file named index2.html [same as above]
All the further changes were made in the original index and analyze file.


## Challenges faced:


Initially making a website with respect to laptops/PCs everything seemed good but when switched to a mobile view the font was disturbed.
Changed my domain from kawaianime.com to kawaianime.in. Reason kawaianime.com was already bought by someone.
While toggling the switch of removing punctuation, a bug was detected- while giving input of multiple new lines, after clicking the analyzed text it gave the o/p in the same line [no multiple new lines]
At first, I thought it was due to get requests but the bug appeared due to the nature of HTML. A new line character in HTML chops up the new line, using pre tag- <pre></pre>. Adding the pre-tag in the analyze.html file not in analyze2.html.
Changing get to post request in view.html an error popped up. CSRF: cross-site request forgery. Why use the CSRF token? : to ensure that the URL is sent by our server not by the third party….just to avoid malicious attack.
{% csrf_token %}: after adding the text in the form section, reloading the page, giving the input, and clicking the analyze text, an error popped up.
New line remover toggle switch was not working so added “\r” in char block.

### What is GET request & POST request?


To send massive messages in the comment box instead of GET request use POST


