from django.http import request, Http404
from django.shortcuts import render
from .models import Image, Profile

# Create your views here.
def home(request):
  images = Image.get_all_images()
  return render(request, 'index.html', {"images":images})

# Display the details of an image
def image_detail(request, photo_id):
  try:
    image_details = Image.objects.get(pk = photo_id)
  except DoesNotExist:
    raise Http404
  return render(request, "detailedImage.html", {"details": image_details})