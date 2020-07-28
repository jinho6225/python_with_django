from django.shortcuts import render, get_object_or_404

# Create your views here.

# ---------------------------------------- [edit] ---------------------------------------- #
from django.http import HttpResponse
from .models import Question
# ---------------------------------------------------------------------------------------- #

def index(request):
# ---------------------------------------- [edit] ---------------------------------------- #
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}

    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

    return render(request, 'pybo/question_list.html', context)
# ---------------------------------------------------------------------------------------- #

def detail(request, question_id):
# ---------------------------------------- [edit] ---------------------------------------- #
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}

    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
    
    return render(request, 'pybo/question_detail.html', context)
# ---------------------------------------------------------------------------------------- #