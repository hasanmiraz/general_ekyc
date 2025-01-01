from django.db import models

# Create your models here.

class PersonalDetails(models.Model):
    name = models.CharField(max_length=50, null=False)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(null=True)
    
    def __str__(self):
        return self.name
    
class FamilyDetails(models.Model):
    father_name = models.CharField(max_length=50, null=True)
    mother_name = models.CharField(max_length=50, null=True)
    syblings = models.IntegerField(null=True)
    
class EducationDetails(models.Model):
    school = models.CharField(max_length=20, null=True)
    collage = models.CharField(max_length=20, null=True)
    university = models.CharField(max_length=20, null=True)
    degree = models.CharField(max_length=20, null=True)
    
class Courses(models.Model):
    name = models.CharField(max_length=20, null=False)
    code = models.CharField(max_length=20, null=False)
    credit = models.IntegerField(null=False)
    
class Universities(models.Model):
    name = models.CharField(max_length=20, null=False)
    country = models.CharField(max_length=20, null=False)
    city = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=20, null=False)