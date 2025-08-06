from django.shortcuts import render, get_object_or_404
from .models import Course, Teacher, Lesson

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'courses/teacher_list.html', {'teachers': teachers})

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})
