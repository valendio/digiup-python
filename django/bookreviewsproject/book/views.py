from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def home(request):
    searchJudul = request.GET.get('judul')
    return render(request, 'home.html', {'searchJudul':searchJudul})
def about(request):
    return render(request,'about.html',{'appName' :'BookReview'})
def home(request):
    searchJudul = request.GET.get('judul')
    if searchJudul:
     books = Book.objects.filter(judul__icontains=searchJudul)
    else:
        books = Book.objects.all()
    return render(request, 'home.html', {'searchJudul':searchJudul,'books' : books})