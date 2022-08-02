from django.db import models
#from django.utils import timezone

# Create your models here.
# Django Models
#models.CharField(max_length=255)
#models.TextField()
#models.IntegerField()
#models.BigIntegerField()
#models.PostiveInteerField()
#models.BooleanField();
#models.DateField(auto_now_add=True) => Adding/Creating Current Date auto_now=True => updated at
#models.DateTimeField()
#models.TimeField()
#models.ManyToManyField()
#models.OneToOneField()
#models.ForeignKeyField() -> OneToManyField

# aNYTIME U MAKE CHANGES TO YOUR MODEL THERE IS THE NEED TO MAKEMIGRATIONS(python manage.py makemigrations) AND
# MIGRATE(python manage.py migrate)

class TestModel(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=True, unique=True);
    description = models.TextField()
    phone = models.PositiveIntegerField()
    is_live = models.BooleanField()
    amount = models.FloatField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        #default display
        return f"{self.name} - {self.email} - {self.created_at.strftime(' %H: %M: %S')}"

    class Meta:
        #order based on created_at
        #ascending
        ordering = ("created_at",)
        # descending
      # ordering = ("-created_at",)






