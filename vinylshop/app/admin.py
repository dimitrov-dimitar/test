from django.contrib import admin
from .models import Album, Profile, Comment
# Register your models here.


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist_name', 'album_name', 'price')


admin.site.register(Album, AlbumAdmin)
admin.site.register(Profile)
admin.site.register(Comment)
