# blog/models.py
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100,
                             choices =(
                                 ('제목1','제목1 레이블'), # (저장될 값, ui에 보여질 레이블)
                                 ('제목2','제목2 레이블'),
                                 ('제목3','제목3 레이블'),
                             ), verbose_name='제목', help_text='포스팅 제목을 입력해주세요.') # 길이제한이 있는 문자열
    # verbose_name 은 title에 쓰면 title의 이름을 바꾼다.(언어 설정에 상관없이 이름으로 보여진다.)
    content = models.TextField(verbose_name='내용') # 길이제한이 없는 문자열
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#     auto_now_add 는 저장될 때 그때의 시각을 기록
#     auto_now는 저장될 때 마다 기록 갱신




