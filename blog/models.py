from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True) # 시간 자동으로 저장되게 하기.
    #author: 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
