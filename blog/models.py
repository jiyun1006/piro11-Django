# blog/models.py
from django.db import models
import re
from django.forms import ValidationError




def lnglat_validator(value):
    if not re.match(r'^([+=]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):

        raise ValidationError('Invalid LngLat Type')



class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p','Published'),
        ('w', 'Withdrawn'),
    )


    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100,
                              verbose_name='제목', help_text='포스팅 제목을 입력해주세요.') # 길이제한이 있는 문자열
    # verbose_name 은 title에 쓰면 title의 이름을 바꾼다.(언어 설정에 상관없이 이름으로 보여진다.)
    content = models.TextField(verbose_name='내용') # 길이제한이 없는 문자열
    tags = models.CharField(max_length =100, blank = True)
    lnglat = models.CharField(blank = True ,max_length =50, help_text = '경도/위도 포맷으로 입력',validators=[lnglat_validator])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
#     auto_now_add 는 저장될 때 그때의 시각을 기록
#     auto_now는 저장될 때 마다 기록 갱신
    tag_set = models.ManyToManyField('Tag')
    # relation 지정할때는 관련 클래스를 지정 그러나 이번엔 문자열로 쓴다.
    class Meta:
        ordering = ['-id']


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    author = models.CharField(max_length =20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length = 50, unique=True)
    def __str__(self):
        return self.name


# def __str__(self):
#   return self.name
# 이함수가 post.object같은 제목을 내용을 제목으로 변환시킨다.