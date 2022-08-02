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
    #showing how we can manipulate data before saving
    #In this instance we set a field as not editable so admin cannot have access to change.
    #then we override the save method
    nickname = models.CharField(max_length=255, editable=False, default="null")
    region = models.ForeignKey("RegionModel", null=True, on_delete=models.CASCADE, related_name="test_constant")
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        #default display
        return f"{self.nickname}"

    #Handles changes we make to the default flow of our model
    class Meta:
        #order based on created_at
        #ascending
        ordering = ("created_at",)
        # descending
      # ordering = ("-created_at",)
     # Changing the default name of model in display
        verbose_name_plural = "Test Model"

    #Overriding the save method
    def save(self, *args, **kwargs):
        self.nickname=f"{self.name} - {self.phone}"
        #superclass
        super().save(*args,**kwargs)

class RegionModel(models.Model):
    Region_ID = models.CharField(max_length=5, primary_key=True)
    Region_Name = models.CharField(max_length=100)

    def __str__(self):
        #default display
        return f"{self.Region_Name}"

    class Meta:
        # Changing the default name of model in display
        verbose_name_plural = "Region Model"







