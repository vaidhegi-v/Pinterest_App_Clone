from django.contrib import admin

from .models import News,Board,Pin,Profile,Comments,SavedPin,Update,Message


# Register your models here.

admin.site.register(News)
admin.site.register(Board)
admin.site.register(Pin)
admin.site.register(Profile)
admin.site.register(Comments)
admin.site.register(SavedPin)
admin.site.register(Update)
admin.site.register(Message)