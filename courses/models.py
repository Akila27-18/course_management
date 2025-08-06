from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course, related_name='teachers')

    def __str__(self):
        return self.name

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return f"{self.title} ({self.course.title})"
