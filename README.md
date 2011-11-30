# Overview

markdown2wp.com is comprised of two python scripts for posting entries written in markdown syntax to a [wordpress-dot-com](http://wordpress.com) blog, and for uploading images for the post. Right now, the imageupload doesn't work very well. But, this is public domain software that carries no guarantees. I'd still probably suggest leaving the image uploading out until I can get it to work a little better.

## Requirements

Python 2.6.x or higher.

There are a number of dependencies not in the standard library that are necessary:  
`keyring`    
`markdown`      
`kitchen`


Image uploading also requires `BeautifulSoup`.

I'll leave it to you to install those with pip or easy_install.

## Usage

The dev branch version of this script dispenses with managing metadata using yaml, and instead relies on the metadata extension in python markdown. This extension adds multimarkdown-like metadata support for files, and extracts the metadata to a dictionary comprised of lists. Title and status are required metadata fields, while categories and tags are optional. So, the beginning of a post should look like this:  

<pre>
title:       My Post Title  
categories:  category1  
             category2  
tags:        tag1  
             tag2  
status:      draft  
</pre>

Status options are: `draft` or `publish`. Drafts are uploaded to wp.com, but not published. Two lines after the metadata, write your post as normal.  

## Extensions

The metadata extension isn't the only one available. As written, the script also supports table of contents, code highlighting, and footnotes. Any extensions from [python markdown](http://www.freewisdom.org/projects/python-markdown/Available_Extensions) can be included. Just add them to line 30 in the script.  

To include a Table of Contents on your post, insert `[toc]` where you want it to be placed. Then, use header levels in your post to mark sections. Footnotes follow [PHP Markdown Extra](http://michelf.com/projects/php-markdown/extra/#footnotes) syntax, and are described [here](http://www.freewisdom.org/projects/python-markdown/Footnotes).  

Enjoy!  

For more information on using this script, see this [post](http://parezcoydigo.wordpress.com/2011/05/25/post-to-wordpress-com-with-markdown-6/) on my blog!   
