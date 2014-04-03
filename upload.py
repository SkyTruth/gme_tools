#! /usr/bin/env python

from subprocess import call
import datetime
import time
import sys
import os.path
import glob
import string


#src = './tiffs/**/*.tiff'
#src = '/cygdrive/i/NAIP/Pennsylvania/ByCounty/TOUPLOAD/**/*.sid'
src = '//media/sf_FRED_DATASETS/NAIP/Pennsylvania/2013/TOUPLOAD/**/*.sid'
common_tags = ['autoupload:2014-03-14:01', 'Pennsylvania']
key = '../GME-PrivateKey/3bdd03d0a00be20af4c3138fad74fe2f9acd7259-privatekey.p12'
uploader = 'gme_tools/mapsengineupload.py'


src_files = glob.glob (src)
for s in src_files:
	dir= os.path.split(os.path.split(s)[0])[1]
	tags = string.split(dir, '-') + common_tags
#	tags.extent(common_tags)
#	print tags
	
	params = [
		uploader,
		"--email=680740468408-jmdjgq5q7t6vbls8uqfj6d9v8mergb6o@developer.gserviceaccount.com",
		"--projectid=06136759344167181854",
		'--name=' + dir,
		'--attribution=Copyright SKYTRUTH',
	#	'--time=' + time,
		'--tags=' + ','.join(tags),
		'--key=' + key,
		s	
	]
	call(params)
	
		

