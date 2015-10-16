from django.contrib import admin

from .models import Customer
from .models import Video
from .models import Object
from .models import User
from .models import UserAction

# Register your models here.
admin.site.register(Customer)
admin.site.register(Video)
admin.site.register(Object)
admin.site.register(User)
admin.site.register(UserAction)


