from django.db import models

#Install seeder to auto populate the model
#pip install django-seed
#To seed your models add 'django_seed' to installed apps in settings.py
#cmd=> python manage.py seed <nameofapp> --number=<number of rows to be populated>
class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.title







