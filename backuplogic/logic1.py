import feedparser
import urllib2
from urllib2 import urlopen
import cookielib
from cookielib import CookieJar
from readability.readability import Document
import codecs

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0')]
time_std = (0,0,0,0,0,0,0,0,0)


def crawl(url):
	global time_std
	d = feedparser.parse(url)
 	version = u''.join(d.version).encode('utf-8').strip()
	if version == "" :
        	print "Not a feed"
	else:
		print version
		f = open('abc.txt','w+')
		for i in range(len(d.entries)):
			if d.entries[i].published_parsed > time_std :
				title=u''.join(d.entries[i].title).encode('utf-8').strip()
				link=u''.join(d.entries[i].links[0]['href']).encode('utf-8').strip()
				published_date=u''.join(d.entries[i].published).encode('utf-8').strip()
				f.write("Title : " + title + "\n")
				f.write("Link : " + link + "\n")
				f.write("Date : " + published_date + "\n")
				try :
					sourceCode=opener.open(link).read()
					content = Document(sourceCode).summary()
					f.write("Content : \n" + content + "\n")				
					f.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
					f.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
					f.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
					f.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
					print i+1
				except Exception, e:
					try:
						f.close()
						fout = codecs.open('abc.txt','a+','utf-8')
						fout.write("content : \n")				
						fout.write(content + "\n")				
						fout.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
						fout.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
						fout.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
						fout.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
						fout.close()
						f = open('abc.txt','a+')
						print i+1
					except Exception, e:
						print "Error : "
						print str(e)
						print link
			else :
				print "No new updates ahead"
				break
		
		time_std = d.entries[0].published_parsed
		#time_std = time.localtime(time.time())
		f.close()
		
        		
