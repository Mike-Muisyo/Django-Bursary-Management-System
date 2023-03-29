from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 
class Student(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    CONSTITUENCY = (
        ('Kibwezi West','Kibwezi West'),
        ('Kibwezi East', 'Kibwezi East'),
        ('Mbooni', 'Mbooni'),
        ('Kilome', 'Kilome'),
    )
    WARD = (
        ('Wote', 'Wote'),
        ('Makindu', 'Makindu'),
        ('Mtito-Andei', 'Mtito-Andei'),
        ('Thange', 'Thange'),
    )
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True, choices=GENDER)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile.png", null=True,blank=True)
    id_card = models.ImageField(null=False,blank=True)
    institution = models.CharField(max_length=200, null=True)
    fees_structure = models.FileField(null=False,blank=True)
    year_of_study = models.CharField(max_length=200, null=True)
    Constituency = models.CharField(max_length=200, null=False, choices=CONSTITUENCY)
    ward = models.CharField(max_length=200, null=False, choices=WARD)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Bursary(models.Model):
    CATEGORY = (
        ('County', 'County'),
        ('Constituency', 'Constituency'),
        ('Ward', 'Ward'),
    )
    name = models.CharField(max_length=200, null=True)
    amount = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    batchNumber = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Applications(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Disbursement in Progress', 'Disbursement in Progress'),
        ('Fully Disbursed', 'Fully Disbursed'),
    )
    ApplyAmount = (
        ('KSH 8000.00', 'KSH 8000.00'),
        ('KSH 10000.00', 'KSH 10000.00'),
    )

    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL, related_name="applications")
    bursary = models.ForeignKey(Bursary, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    applyAmount = models.CharField(max_length=200, null=True, choices=ApplyAmount)


    def __str__(self):
        return self.bursary.name
