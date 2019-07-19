from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name= '+' , on_delete = models.CASCADE)
    message = models.TextField()
    updated_at = models.DateTimeField(auto_now_add = True)
    created_at = models.DateTimeField(auto_now = True)

    # related name이 중복될시 related name을 고유이름으로 설정하던지,
    # related_name = +  를 줘서 related name 을 포기한다.