from django.contrib import admin
from proyecto.models import Proyecto, Picture, Comment,Choice
# Register your models here.

admin.site.register(Proyecto)
admin.site.register(Picture)
admin.site.register(Comment)
admin.site.register(Choice)
class AlbumImageInline(admin.TabularInline):
    model = Picture
    extra = 3

class AlbumAdmin(admin.ModelAdmin):
    inlines = [ AlbumImageInline, ]