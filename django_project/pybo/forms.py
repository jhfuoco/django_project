from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm): # question_detail.html, views의 answer_create 함수에서 활용
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }



from .models import UploadImage

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = ['image']