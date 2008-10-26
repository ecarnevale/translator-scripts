#!/usr/bin/python
# encoding: utf-8
"""
translator_json_parser.py

Created by Emanuel Carnevale on 2008-09-09.
Copyright (c) 2008 emanuelcarnevale.com . All rights reserved.

http://www.opensource.org/licenses/mit-license.php

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

import sys
import getopt
import urllib,urllib2
import simplejson
#import json

referer = u'http://emanuelcarnevale.com'

help_message = '''
translator_json_parser.py

Created by Emanuel Carnevale on 2008-09-09.
http://emanuelcarnevale.com
MIT License

Python script for accessing Google Translate API and json-zh.appspot.com

-p to get Pinyin reading from http://json-zh.appspot.com
-t string to get Google translation

'''

class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

def main(argv=None):
	pinyin = False
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "ht:p", ["help", "text=","pinyin"])
		except getopt.error, msg:
			raise Usage(msg)
		
		# option processing
		for option, value in opts:
			if option in ("-h", "--help"):
				raise Usage(help_message)
			if option in ("-t", "--text"):
				text = value
			if option in ("-p", "--pinyin"):
				pinyin = True
		try:
			text
		except:
			raise Usage(help_message)
			
	except Usage, err:
		print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
		print >> sys.stderr, "\t for help use --help"
		return 2
		
	#print text
	if pinyin:
	    url = u'http://json-zh.appspot.com/pinyin?hanzi='
	    query = url + urllib.quote(text)
	else:
	    url = u'http://ajax.googleapis.com/ajax/services/language/translate?v=1.0&q='
	    query = url + urllib.quote(text) + u'&langpair=%7Cen'
	    
	request = urllib2.Request(url = query, origin_req_host = referer)
	resp = urllib2.urlopen(request)
		
	#if you want to use json.py
	#uncomment the relatve import statement
	#result = json.read(resp.read())
	result = simplejson.loads(resp.read())
		
	if pinyin:
	    print result["pinyin"]
	else:
	    print result["responseData"]["translatedText"]

if __name__ == "__main__":
	sys.exit(main())
