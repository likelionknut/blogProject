from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name="detail"), #패스컨버터를 사용하여 정수형숫자로 객체들(블로그 글들)을관리, detail 함수로 blog_id를 넘겨줌
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('newblog/', views.blogpost, name="newblog"),
]