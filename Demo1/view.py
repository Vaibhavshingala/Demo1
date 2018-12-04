from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request,'homepage.html')
	
def contact(request):
	return render(request,'contact.html')
	
def services(request):
	return render(request,'services.html', {'name':'my name is vaibhav'})

def serviceslist(request):
	return HttpResponse('<ol><li>simple</li><br/><li>complex</li></ol>')

def products(request):
	return render(request,'page1.html')

def wordcount(request):
	return render(request,'wordc.html')
	
def countword(request):
	data = request.GET['t1']
	#print(data)
	x = data.split(" ")
	ans = {}
	for i in x:
		if i not in ans:
			temp = { i : x.count(i)}
			ans.update(temp)
	# print(ans)
	sorted_list = sorted(ans.items(), key = operator.itemgetter(1), reverse = True)
	return render(request,'count_word.html', {'length':len(x),'text': ans, 'worddictonary':sorted_list})

def name(request):
	return render(request,'name.html')

def about(request):
	return render(request,'about.html')
	
def address(request):
	return render(request,'address.html')

	