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
import yaml
import re
import sys
import markdown
import keyring
import cPickle as pickle
import imageUpload
from kitchen.text.converters import to_unicode


# this regex is borrowed from Jonathan Chu's growl site generator
# https://github.com/jonathanchu/growl/blob/master/growl.py

RE_YAML = re.compile(r'(^---\s*$(?P<yaml>.*?)^---\s*$)?(?P<content>.*)',
                         re.M | re.S)
# open file, extract yaml, extract markdown post text

postFile = open(sys.argv[1], 'r').read()
fileInfo = RE_YAML.match(postFile)
getYAML = yaml.load(fileInfo.groupdict().get('yaml'))
postMD = fileInfo.groupdict().get('content')
postMD = to_unicode(postMD, encoding='utf-8', errors='ignore')

# transform the markdown into an html snippet

newPost = markdown.markdown(postMD, extensions=['footnotes', 'codehilite', 'toc'])

blogurl = 'https://YOURBLOG.wordpress.com/xmlrpc.php'
username = 'YOURUSERNAME'

# If using keyring, uncomment the first line. Otherwise, uncomment
# the second.
# password = keyring.get_password('KEYNAME', 'USERNAME')
# password = 'XXXXXXXX'

blogid = ''
server = xmlrpclib.ServerProxy(blogurl, allow_none=True)

if getYAML['status'] == 'publish':
	status = '1'
else: status = '0'

data = {}
data['title'] = getYAML['title']
data['description'] = newPost
data['categories'] = [getYAML['categories']]
data['mt_keywords'] = getYAML['tags']

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
pickle.dump(postList, open('/PATH/TO/post_list.txt', 'w'))




