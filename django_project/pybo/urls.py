from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pybo'

urlpatterns = [
    path('',views.index, name='index'), #/pybo/ -> index 라는 URL별칭으로 정의
    path('<int:question_id>/', views.detail, name='detail'), #int: -> question_id에 숫자가 매핑되었음을 의미 #/pybo/2/ -> detail 이라는 URL별칭으로 정의
    # /pybo/2/ 가 요청되면 매핑규칙에 의해 /pybo/<int:question_id>/가 적용되어
    # question_id에 2라는 값이 저장되고 views.detail 함수가 실행됨
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),

    path('upload/', views.upload_image, name='upload_image'),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# 기존의 urlpatterns 아래에 추가합니다.
if settings.DEBUG:  # 개발 환경인 경우에만
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
