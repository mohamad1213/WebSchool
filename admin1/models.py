from PIL import Image
from django.utils.translation import gettext as _
from django.db import models
from django.conf.urls.static import static
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	alamat = models.TextField(null=True)
	profile_pic = models.ImageField(upload_to="media/",null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name
	class Meta:
		verbose_name = _('Profile')
		verbose_name_plural = _('Profiles')

	@property
	def get_avatar(self):
		return self.profile_pic.url if self.profile_pic else static('/admin/assets/img/avatars/avatar.png')
