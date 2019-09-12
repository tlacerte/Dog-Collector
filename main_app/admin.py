from django.contrib import admin
from .models import Dog, Feeding, Photo, Toy

admin.site.register(Dog)
admin.site.register(Feeding)
admin.site.register(Photo)
admin.site.register(Toy)