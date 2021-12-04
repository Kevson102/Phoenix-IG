from django.test import TestCase
from .models import Profile, Image, User

# Create your tests here.
class ProfileTestCase(TestCase):
  # Set up method
  def setUp(self):
    # current_user = kevson
    user, created = User.objects.get_or_create(username='kevson',  password='password')
    self.new_profile = Profile(image = 'profile_pict', bio = 'This is my bio', user = user)
    
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
    
  # Test Update captions
  def test_updateCategory(self):
    pass
  
class ImageTestCase(TestCase):
  # set up method
  def setUp(self):
    user, created = User.objects.get_or_create(username='kevson',  password='password')
    # Create and save a profile instance for the test
    self.new_profile = Profile(image = 'profile_pict', bio = 'This is my bio', user = user)
    self.new_profile.save_profile()
    
    # Create and save an image instance for the test
    self.image = Image(1, 'my image', 'caption to image', 1, 1, '2021', user)
    self.image.save()
    
  def tearDown(self):
    Image.objects.all().delete()
    Profile.objects.all().delete()
    
  # Test Instance
  def test_instance(self):
    self.assertTrue(isinstance(self.image, Image))
    
  # Test save image method
  def test_save_image(self):
    self.image.save_image()
    saved_images = Image.objects.all()
    self.assertTrue(len(saved_images)==1)
    
  # Test get all images
  def test_get_all_images(self):
    user, created = User.objects.get_or_create(username='kevson',  password='password')
    self.image.save_image()
    self.image2 = Image(2, 'my image', 'caption to image', 2, 2, '2021', user)
    self.image2.save_image()
    saved_images = Image.get_all_images()
    self.assertTrue(len(saved_images) == 2)