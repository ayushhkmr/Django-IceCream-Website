from django.contrib import admin
from home.models import Contact

admin.site.register(Contact)

class Contact(admin.ModelAdmin):
    list_display = ('name',)
# Register your models here.
