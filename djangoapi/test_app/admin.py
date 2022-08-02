from django.contrib import admin
#import model from models.py
from .models import TestModel, RegionModel

# Register your models here.
# aNYTIME U MAKE CHANGES TO YOUR MODEL THERE IS THE NEED TO MAKEMIGRATIONS(python manage.py makemigrations) AND
# MIGRATE(python manage.py migrate)

admin.site.register(TestModel)
admin.site.register(RegionModel)
