from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200, default="Default Title")
    content = models.TextField(default='')  # 빈 문자열을 기본값으로 사용           
    created_date = models.DateTimeField(default=timezone.now)  # 생성 날짜
    published_date = models.DateTimeField(blank=True, null=True)  # 게시 날짜
    project_type = models.CharField(max_length=100, default='general')  # 'college' 또는 'research'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

from django.db import models

class Award(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


from .models import Award
from django.shortcuts import render

def newsroom_view(request):
    awards = Award.objects.all()  # Award 모델에서 모든 객체를 가져옵니다.
    return render(request, 'blog/newsroom.html', {'awards': awards})


