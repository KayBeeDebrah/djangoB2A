from django.contrib import admin
#import model from models.py
from .models import BlogModel

# Register your models here.
# aNYTIME U MAKE CHANGES TO YOUR MODEL THERE IS THE NEED TO MAKEMIGRATIONS(python manage.py makemigrations) AND
# MIGRATE(python manage.py migrate)
#Install seeder to auto populate the model
#pip install django-seed
#

admin.site.register((BlogModel,))
#admin.site.register(RegionModel)