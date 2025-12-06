from django.contrib import admin
from .models import About,Skill,Blog,ContactForm,SocialLink,Resume,Project,BackgroundImage
# Register your models here.

admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Blog)
admin.site.register(ContactForm)
admin.site.register(SocialLink)
admin.site.register(Resume)
admin.site.register(Project)
admin.site.register(BackgroundImage)