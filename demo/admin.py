from django.contrib import admin

# Register your models here.
from .models import Gallery, Image

from django.utils.translation import ugettext_lazy as _

# Create your models here.

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'status', 'create_time']
    ordering = ['-create_time', ]

    #list_display = [f.name for f in Gallery._meta.fields]

class ImageAdmin(admin.ModelAdmin):
    #list_display = [f.name for f in Image._meta.fields]
    #list_display = ['title', 'user', 'status', 'create_time']
    list_display = ['gallery', 'user', 'title', 'caption', 'status', 'create_time']
    ordering = ['-create_time', ]

    def save_model(self, request, obj, form, change):
        if not obj.user: obj.user = request.user
        obj.save()

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)

