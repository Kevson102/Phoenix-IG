from django.test import TestCase
from .models import Profile, Image

# Create your tests here.
class ProfileTestCase(TestCase):
  # Set up method
  def setUp(self):
    self.new_profile = Profile(image = 'profile_pict', bio = 'This is my bio')
    
  #Test Instance
  def test_instance(self):
    self.assertTrue(isinstance(self.new_profile, Profile))
   
  # Test save profile method 
  def test_save_method(self):
    self.new_profile.save_profile()
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles)==1)
    
  # Test Delete profile method
  def test_delete_method(self):
    self.new_profile.save_profile()
    self.new_profile.delete_profile()
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles)==0)