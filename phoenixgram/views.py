from django.http import request, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Image, Profile, Like, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
  images = Image.get_all_images()
  return render(request, 'index.html', {"images":images})

# Display the details of an image
@login_required(login_url='/accounts/login/')
def image_detail(request, photo_id):
  try:
    image_details = Image.objects.get(pk = photo_id)
    image_comments = Comment.objects.filter(image_id= photo_id).all()
  except DoesNotExist:
    raise Http404

  if request.method == "POST":
    form = CommentForm(request.POST)
    image = image_details
    if form.is_valid():
      comment_message = form.cleaned_data.get('comment_message')
      form.instance.user = request.user
      form.instance.image = image
      form.save()
      return redirect('home')
  else:
    form = CommentForm()
  return render(request, "detailedImage.html", {"details":image_details, "form":form, "comments":image_comments})

@login_required(login_url='/accounts/login/')
def profile(request):
  return render(request, 'profile.html')
# def add_comment(request):
#   if request.method == "POST":
#     form = CommentForm(request.POST)
#     if form.is_valid():
#       return HttpResponseRedirect('image_details')
#   else:
#     form = CommentForm()
    
#   return render(request, )