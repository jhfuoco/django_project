from django.db import models

# Create your models here.
class Question(models.Model): # 질문모델 작성하기
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.subject
    
class Answer(models.Model): # 답변모델 작성하기 # 답변모델은 어떤 질문에 대한 답변이므로 질문모델을 속성으로 가져야 함-> 어떤 모델이 다른 모델을 속성으로 가지면 포른키를 이용!
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 답변에 연결된 질문이 삭제되면 답변도 함께 삭제하라
    content = models.TextField()
    create_date = models.DateTimeField()




class UploadImage(models.Model):
    image = models.ImageField(upload_to='images/')
    