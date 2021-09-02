from django.shortcuts import render, get_object_or_404  # render : 파이썬 데이터를 템플릿에 적용해 HTML로 반환하는 함수
from .models import Question


def index(request):
    """
    pybo 목록 출력
    """
    # 질문 목록 데이터 create_date 내림차순으로 조회
    question_list = Question.objects.order_by("-create_date")
    context = {"question_list": question_list}

    # "pybo/question_list.html": template
    return render(request, "pybo/question_list.html", context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "pybo/question_detail.html", context)
