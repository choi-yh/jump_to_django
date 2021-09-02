from django.urls import path

from . import views

app_name = "pybo" # url namespace

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),  # url 별칭 지정
]
