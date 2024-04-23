

from django.contrib import admin
from .models import Bb
from .models import Rubric

class BbAdmin(admin.ModelAdmin): # стр. 51
    list_display = ('title', 'content', 'price', 'published', 'rubric') # имена полей, которые выводятся в списке записей
    list_display_links = ('title', 'content') # имена полей, которые преобразуются в гиперссылки
    search_fields = ('title', 'content', ) # по этим полям по которым будет делаться фильтрация


admin.site.register(Bb, BbAdmin)

# admin.site.register(Bb)
