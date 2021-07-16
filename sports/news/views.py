from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import News
from category.models import Category

def news(request):
	title = request.GET.get('title', '')
	category = request.GET.get('category', '')
	try:
		news = News.objects.filter(category__title__icontains=category, title__icontains=title)
		categoryes = Category.objects.all()
	except:
		raise Http404('Новость не найдена')

	return render(request, 'news/list.html', {'news': news, 'categoryes': categoryes})

def detail(request, id):
	try:
		news = News.objects.get(id = id)
	except:
		raise Http404('Новость не найдена')

	return render(request, 'news/detail.html', {'news': news})