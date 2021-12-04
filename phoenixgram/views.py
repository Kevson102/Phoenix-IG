from django.http import request
from django.shortcuts import render
from .models import Image, Profile

# Create your views here.
def home(request):
  images = Image.get_all_images()
  return render(request, 'index.html', {"images":images})