
from django.contrib import admin

from .models import *


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'image')

    def admin_image(self, obj):
        if obj.id:
            return '<img src="%s"height="150"/>'%obj.image.url
        return ''
    admin_image.allow_tags = True


admin.site.register(Place, PlaceAdmin)
admin.site.register(Tourist)
admin.site.register(Hotel)
