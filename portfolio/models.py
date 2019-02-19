from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to='images/')
    # ImageField를 쓰려면 pillow를 설치해야함. 
    # python에서 이미지를 효율적으로 처리해줄수 있게해주는 패키지
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title