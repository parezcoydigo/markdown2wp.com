# Overview

markdown2wp.com is comprised of two python scripts for posting entries written in markdown syntax to a [wordpress-dot-com](http://wordpress.com) blog, and for uploading images for the post. Right now, the imageupload doesn't work very well. But, this is public domain software that carries no guarantees. I'd still probably suggest leaving the image uploading out until I can get it to work a little better.

## Requirements

Python 2.6.x or higher.

There are a number of dependencies not in the standard library that are necessary:  
`keyring  
markdown  
yaml`  


Image uploading also requires `BeautifulSoup`.

I'll leave it to you to install those with pip or easy_install.

   
