from PIL import Image
from django.utils.translation import gettext as _
from django.db import models
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from ckeditor_uploader.fields import RichTextUploadingField

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


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    categories = models.ManyToManyField(Category, related_name='articles')
    featured_image = models.ImageField(upload_to='articles/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
class TentangKami2(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='tentang2')
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def save(self, *args, **kwargs):
        if not self.pk and TentangKami2.objects.exists():
            raise ValidationError('Hanya satu data Tentang Kami yang diperbolehkan.')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class VisiMisi(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='visimisi')
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def save(self, *args, **kwargs):
        if not self.pk and VisiMisi.objects.exists():
            raise ValidationError('Hanya satu data Tentang Kami yang diperbolehkan.')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title