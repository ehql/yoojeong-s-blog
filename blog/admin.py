from django.contrib import admin
from .models import Post

# 'Post' 모델을 어드민 사이트에 등록합니다.
admin.site.register(Post)
