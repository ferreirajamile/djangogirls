from django.contrib import admin
from .models import Post

admin.site.register(Post)

admin.site.site_header = 'Meu Brógui, Véi!'
admin.site.site_title = 'Meu Primeiro brógui xuxu!'
admin.site.index_title = 'Meu título lindão'