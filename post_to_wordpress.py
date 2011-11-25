#! /usr/bin/python

"""
post_to_wordpress.py

Created by Chad Black, 05-24-2011

This script takes a markdown file with a YAML header and posts
either a draft or a published article to a wordpress.com blog. It 
also first retrieves and uploads images stored in an image folder to the
blog on deployment.

"""

import xmlrpclib
import sys
import markdown
import keyring
import cPickle as pickle
import imageUpload
from kitchen.text.converters import to_unicode

# open file, extract markdown post text, convert to unicode.
postFile = open(sys.argv[1], 'r').read()
postFile = to_unicode(postFile)


# transform the markdown into an html snippet and extract the post metadata
md = markdown.Markdown(extensions=['meta', 'footnotes', 'codehilite', 'toc'])
newPost = md.convert(postFile)
data = md.Meta

blogurl = 'https://YOURBLOG.wordpress.com/xmlrpc.php'
username = 'YOURUSERNAME'

# If using keyring, uncomment the first line. Otherwise, uncomment
# the second.
# password = keyring.get_password('KEYNAME', 'USERNAME')
# password = 'XXXXXXXX'

blogid = ''
server = xmlrpclib.ServerProxy(blogurl, allow_none=True)

if data['status'] == 'publish':
	status = '1'
else: status = '0'

# The metadata plugin for python markdown returns a dictionary with each
# value as a list. We have to coerce that to a string for the title. Also,
# the xmlrpc uses 'mt_keywords' instead of 'tags' in its struct, so we need
# to substitute those keys too. Finally, we import the converted html as the 
# post description.
data['mt_keywords'] = data['tags']
data['description'] = newPost
data['title'] = data['title'][0]

# We need to drop status and tags from the dictionary for transport.
data.pop('status')
data.pop('tags')

# Make a list of images in the post, and upload them to the blog.
# Uncomment the next two lines to enable image uploads from the
# markdown file. The script imageList.py should be in the same
# folder as this one. Images need be stored in the same folder
# in the size you want them to appear in the post.

# imageList = imageUpload.imageName(newPost)
# imageUpload.upload(server, blogid, username, password, imageList)

post_id = server.metaWeblog.newPost(blogid, username, password, data, status)

print "Created new post. ID = %s" %post_id

# Save the new postid and title to post_lists file.
# The post list could be useful in the future, for finding the 
# post-id of an already-published post or a draft, downloading
# from the server, editing, and reposting. Haven't written that code yet.

postList = pickle.load(open('/PATH/TO/post_list.txt'))
postList[post_id] = data['title']
pickle.dump(postList, open('/PATH/TO/post_list.txt', 'w')):





