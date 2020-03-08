from django.contrib import admin
from .models import *


class MenuInline(admin.TabularInline):
    model = Menu
    fk_name = 'parent'
    fields = ('name', 'slug')


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_main')
    ordering = ('-is_main', )
    inlines = [MenuInline]


admin.site.register(Menu, MenuAdmin)
