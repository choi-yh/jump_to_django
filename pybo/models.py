"""
- django는 Model을 통해 데이터베이스를 처리한다.
- 데이터베이스를 ORM(Object Relational Mapping)을 사용해 쿼리문을 사용한다.
    - ORM : 데이터베이스의 테이블을 모델화해서 사용하는 방식. SQL의 단점(쿼리 형식 다양성, 시스템 성능 저하 등)이 사라진다.

- Pybo : 질문과 답변을 할 수 있는 게시판 서비스 -> 질문과 답변에 해당하는 데이터 모델 필요
"""

from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)  # 질문의 제목
    content = models.TextField()  # 질문의 내용 / 글자수 제한 X 텍스트 -> TextField 사용
    create_date = models.DateTimeField()  # 질문 작성 일시
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):  # id 값 대신 제목 표시
        return self.subject


class Answer(models.Model):
    # 질문 (어떤 질문에 대한 답인지 확인하기 위함) / ForeignKey : 기존 모델을 속성으로 연결
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()  # 답변의 내용
    create_date = models.DateTimeField()  # 답변 작성 일시
    modify_date = models.DateTimeField(null=True, blank=True)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(
        Question, null=True, blank=True, on_delete=models.CASCADE
    )
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
