from django import forms
from .models import Image, Profile, Comment

class CommentForm(forms.ModelForm):
  comment_message = forms.CharField(widget=forms.Textarea(attrs={
    'rows':'3',
  }))
  class Meta:
    model = Comment
    exclude = ('posted_on', 'user', 'image')
    
class ImageForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude = ('profile', 'user', 'date_posted')
    