from .models import Board,Update,Message
from django.contrib.auth.models import User

def site_data(self):
    b=Board.objects.all()
    u=Update.objects.all()
    m=Message.objects.all()


    return{'board':b,'update':u,'message':m}