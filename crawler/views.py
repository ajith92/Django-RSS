from django.http import HttpResponse
from django.shortcuts import render
import crawler

def base(request):
	from crawler import logic
	if request.method == "GET":
		get = request.GET.copy()	
		if get.has_key('URL'):
			url =str(get['URL'])
			#print url
			crawler.logic.crawl(url)  	
		else:
			print "Somethin Wrong"
	return render(request,'crawler.html')
