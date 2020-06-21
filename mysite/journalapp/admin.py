from django.contrib import admin
from .models import User, Journal, Entry

admin.site.register(User)
admin.site.register(Journal)
admin.site.register(Entry)

# Register your models here.
