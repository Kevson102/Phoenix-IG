from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^details/(?P<photo_id>\d+)', views.image_detail, name='image_details'),
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^newImage/', views.post_image, name='post_image')
]
