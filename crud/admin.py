from django.contrib import admin
from .models import Detail

# Register your models here.

@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ["phone", "dob", "married", "kids", "doh", "title", "duration", "updated"]
    list_filter = ["title", "doh", "duration"]
