from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=13, unique=True)
    image = models.ImageField(upload_to="student_images/", default="student_images/default.png")
    location = models.CharField(max_length=250)
    hobby = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.first_name
