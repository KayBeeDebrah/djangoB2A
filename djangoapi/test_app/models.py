from django.db import models

# Create your models here.
# Django Models
#models.CharField(max_length=255)
#models.TextField()
#models.IntegerField()
#models.BigIntegerField()
#models.PostiveInteerField()
#models.BooleanField();
#models.ManyToManyField()
#models.OneToOneField()
#models.ForeignKeyField() -> OneToManyField

class TestModel(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=True, unique=True);
    description = models.TextField()
    phone = models.PositiveIntegerField()
    is_Active = models.BooleanField()
    amount = models.FloatField()





