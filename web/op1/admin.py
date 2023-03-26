from django.contrib import admin 
from .models import client , municipality , decribe , comment ,decribe_to_check,projects

admin.site.register(client)
admin.site.register(municipality)
admin.site.register(decribe)
admin.site.register(comment)
admin.site.register(decribe_to_check)
admin.site.register(projects)

# Register your models here.
