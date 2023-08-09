from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm # forms.py의 Q,A Form


from .forms import ImageUploadForm
from .models import UploadImage
from .classifier import classify_dog_breed

# Create your views here.

def index(request):
    """
    pybo 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1') # 페이지
    
    # 조회
    question_list = Question.objects.order_by('-create_date')
    
    # 페이징 처리
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    
    context = {'question_list' : page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id): # url 매핑에 있던 question_id-> /pybo/2/ 페이지가 호출되면 최종으로 detail 함수의 매개변수 question_id에 2가 전될됨
    """
    pybo 내용 출력
    """
    
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id) # 모델의 기본키를 이용하여 모델 객체 한건을 반환, pk에 해당하는 건이 없으면 오류 대신 404 페이지 반환
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id): 
    # request 매개변수에는 question_detail.html에서 textarea에 입력된 데이터가 파이썬 객체에 담겨 넘어옴, 이 값을 추출하기 위핸 코드가 request.POST.get('content')
    """
    pybo 답변 등록
    """
    
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question':question, 'form' : form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    """
    pybo 질문 등록
    """
    if request.method == 'POST': # POST 방식
        form = QuestionForm(request.POST) # POST 방식은 전달받은 데이터로 폼의 값이 채워지도록 객체 생성
        if form.is_valid():
            question = form.save(commit=False) # form으로 Question 모델 데이터를 저장하기 위한 코드, commit=False는 임시저장을 의미
            question.create_date = timezone.now()
            question.save() # 실제 저장
            return redirect('pybo:index')
    else: # GET 방식
        form = QuestionForm() # GET 방식은 입력값 없이 객체 생성
    
    context = {'form' : form}
    return render(request, 'pybo/question_form.html', context)




from .forms import ImageUploadForm

# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             upload_image = form.save()
            
#             # 업로드된 이미지를 딥러닝 모델에 입력으로 사용
#             img_path = upload_image.image.path  # 업로드된 이미지의 경로를 가져옴
#             predicted_class = classify_dog_breed(img_path)  # 분류 함수 호출

#             # 예측 결과를 사용자에게 반환
#             return render(request, 'pybo/result.html', {'class': predicted_class})

#     else:
#         form = ImageUploadForm()
#     return render(request, 'pybo/upload.html', {'form': form})





def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_image = form.save()
            
            # 업로드된 이미지를 딥러닝 모델에 입력으로 사용
            image_path = upload_image.image.path
            predicted_class = classify_dog_breed(image_path)

            # 업로드된 이미지의 URL을 가져옵니다.
            image_url = upload_image.image.url

            # 예측 결과와 이미지 URL을 사용자에게 반환
            return render(request, 'pybo/result.html', {'class': predicted_class, 'image_url': image_url})

    else:
        form = ImageUploadForm()
    return render(request, 'pybo/upload.html', {'form': form})
