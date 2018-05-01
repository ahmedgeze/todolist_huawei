from django.contrib import admin
from .models import TodoList,Todo

# Register your models here.
class listAdmin(admin.ModelAdmin):
    list_display=('title','created_at','creator')

class todoAdmin(admin.ModelAdmin):
    list_display=('description','created_at','finished_at','is_finished','creator','todolist')


# Register your models here.

admin.site.register(TodoList,listAdmin)
admin.site.register(Todo,todoAdmin)
