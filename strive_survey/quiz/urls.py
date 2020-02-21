from django.urls import path

from . import views

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('questions/<int:question_id>/', views.questions, name='questions')
]