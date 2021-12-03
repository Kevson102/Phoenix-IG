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
    
