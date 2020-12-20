from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length = 500)

    def __str__(self): #admin 사이트에 타이틀넘버 말고 타이틀 내용이 출력되게 하는 함수.
        return self.title 
#여기 까지 하고 pillow 설치. -> 이미지를 데이터베이스에 넣는 라이브러리
