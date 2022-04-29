from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class About(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to ='profilepic.jpg', blank=True)
    about = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name


class Social(models.Model):
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    website = models.URLField(blank=True)
    discord = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)


class Contact(models.Model):
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.email


class Photography(models.Model):
    image = models.ImageField(upload_to ='photography/')
    title = models.CharField(max_length=50)
    tags = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=50, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


def cover_pic_path(instance, filename):
    return f'posts/{instance.pk}/cover.jpg'

def posts_pic_path(instance, filename):
    return f'posts/{instance.pk}/{filename}'

class Post(models.Model):
    post_title = models.CharField(max_length=255)
    preview = models.CharField(max_length=500, blank=True)
    description = RichTextField()
    cover_pic = models.ImageField(upload_to = cover_pic_path)
    image_1 = models.ImageField(upload_to = posts_pic_path, blank=True)
    image_2 = models.ImageField(upload_to = posts_pic_path, blank=True)
    image_3 = models.ImageField(upload_to = posts_pic_path, blank=True)
    tags = models.CharField(max_length=500, blank=True)
    author = models.ForeignKey(About, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_title

    def get_main_tag(self):
        return self.tags.split(',')[0]
    
    def get_tags_list(self):
        return self.tags.split(',')