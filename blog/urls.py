from django.urls import path
from . import views

urlpatterns=[
    # 이 부분을 채울 예정!
    path('<int:pk>/',views.single_post_page),
    path('/',views.index),
]