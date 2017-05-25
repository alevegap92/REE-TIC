from django.contrib import admin
from proyecto.models import proyecto, Galeria, Comment
# Register your models here.

admin.site.register(proyecto)
admin.site.register(Comment)
admin.site.register(Galeria)
