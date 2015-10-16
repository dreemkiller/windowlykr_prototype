from django.contrib import admin

from .models import Customer, Video, Object, User, UserAction

# Register your models here.
admin.site.register(Customer)
admin.site.register(User)
admin.site.register(UserAction)

class ObjectInline(admin.TabularInline):
    model = Object
    extra = 4
    list_filter = ['video']

class VideoAdmin(admin.ModelAdmin):
    inlines = [ObjectInline]
    list_filter = ['customer']
    search_fields = ['name']
admin.site.register(Video, VideoAdmin)

class ObjectAdmin(admin.ModelAdmin):
    list_filter = ['video']
    search_fields = ['object_name']

admin.site.register(Object, ObjectAdmin)


