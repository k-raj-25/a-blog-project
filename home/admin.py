from django.contrib import admin
from home.models import About, Social, Contact, Photography, Post, ContactMessage


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Photography)
class PhotographyAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    pass