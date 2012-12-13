#!/usr/bin/env python
# encoding: utf-8
"""
imageUpload.py

Created by Chad Black on 2011-05-26.

Pulls image tags from post, finds them in the filesystem, and uploads them to wordpress.com.
"""

from BeautifulSoup import BeautifulSoup
from os.path import basename
from urlparse import urlsplit
import xmlrpclib
import base64


def imageName(newPost):
	soup = BeautifulSoup(newPost)
	images = [image["src"] for image in soup.findAll("img")]
	imageNames = []
	for image in images:
		imageName = basename(urlsplit(image)[2])		
		imageNames.append(imageName)
	return imageNames
	

def upload(server, blogid, username, password, imageList):
	if imageList == []:
		print 'No images to upload.'
	else:	
		for image in imageList:
			toUpload = 'PATH/TO/YOUR/IMAGES/FOLDER'+image
			print 'Uploading: '+image
			imageData = {}
			if image[-3:] == 'jpg':
				imageData['type'] = 'image/jpeg'
			else: imageData['type'] = 'image/'+image[-3:]
			imageData['name'] = image
			imageData['bits'] = xmlrpclib.Binary(open(toUpload, 'rb').read())
			server.wp.uploadFile(blogid, username, password, imageData)
			print image+' upload completed.' 







