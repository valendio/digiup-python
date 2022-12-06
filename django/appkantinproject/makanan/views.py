from django.shortcuts import render
from django.http import HttpResponse
from .models import Makanan
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    searchMakanan = request.GET.get('nama')
    if searchMakanan:
        makanans = Makanan.objects.filter(nama__icontains=searchMakanan)
    else:
        makanans = Makanan.objects.all()

    return render(request, 'home.html', {'searchMakanan':searchMakanan,'makanans' : makanans})
    
def detail(request,makanan_id):
    makanan = get_object_or_404(Makanan,pk=makanan_id)
    return render(request,'detail.html',{'makanan' : makanan})