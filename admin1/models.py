from PIL import Image
from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	alamat = models.TextField(null=True)
	profile_pic = models.ImageField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

# resizing images
	def save(self, *args, **kwargs):
		super().save()

		img = Image.open(self.profile_pic.path)

		if img.height > 100 or img.width > 100:
			new_img = (100, 100)
			img.thumbnail(new_img)
			img.save(self.profile_pic.path)
