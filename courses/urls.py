from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('lessons/<int:pk>/', views.lesson_detail, name='lesson_detail'),
]
