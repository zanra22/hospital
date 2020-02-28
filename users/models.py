import os
import random

from django.contrib.auth.models import AbstractUser, User
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 1239124123)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "users/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

class UserQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(is_active=True)
    def featured(self):
        return self.filter(featured=True, is_active=True)

    def search(self, query):
        lookups = Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query)
        return self.filter(lookups).distinct()

class UserManager(models.Manager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)
    def all(self):
        return self.get_queryset().active()
    def featured(self):
        return self.get_queryset().featured()
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)




class CustomUser(AbstractUser):
    hospitalName = models.CharField(max_length=100, null=True, default="N/A")
    lastName = models.CharField(max_length=100, null=True, default="N/A")
    firstName = models.CharField(max_length=100, null=True, default="N/A")
    middleName = models.CharField(max_length=100, null=True, default="N/A")
    homeAddress = models.TextField(max_length=255, null=True, default="N/A")
    city = models.CharField(max_length=30, null=True, default="N/A")
    state = models.CharField(max_length=30, null=True, default="N/A")
    postal = models.CharField(max_length=30, null=True, default="N/A")
    country = models.CharField(max_length=30, null=True, default="N/A")
    birthDate = models.CharField(max_length=100, null=True, default="N/A")

    doctorPK = models.CharField(max_length=255, blank=True)
    specialization = models.CharField(max_length=200, null=True, default="N/A")

    medications = models.TextField(max_length=300, blank=True)
    medicalDirectives = models.TextField(max_length=300, blank=True)
    medicalProblems = models.TextField(max_length=300, blank=True)
    vitalSigns = models.TextField(max_length=300, blank=True)
    physicalExam = models.TextField(max_length=300, blank=True)
    medicalHistory = models.TextField(max_length=300, blank=True)
    medicationPlan = models.TextField(max_length=300, blank=True)
    medicalOrders = models.TextField(max_length=300, blank=True)

    # Test
    alkPhos = models.CharField(max_length=10, blank=True)
    bun = models.CharField(max_length=10, blank=True)
    calcium = models.CharField(max_length=10, blank=True)
    chloride = models.CharField(max_length=10, blank=True)
    co2 = models.CharField(max_length=10, blank=True)
    creatinine = models.CharField(max_length=10, blank=True)
    po4 = models.CharField(max_length=10, blank=True)
    potassium = models.CharField(max_length=10, blank=True)
    sgot = models.CharField(max_length=10, blank=True)
    biliTotal = models.CharField(max_length=10, blank=True)
    uricAcid = models.CharField(max_length=10, blank=True)
    ldhTotal = models.CharField(max_length=10, blank=True)
    sodium = models.CharField(max_length=10, blank=True)

    # Personal
    height = models.CharField(max_length=10, blank=True)
    weight = models.CharField(max_length=10, blank=True)
    temperature = models.CharField(max_length=10, blank=True)
    tempSite = models.CharField(max_length=10, blank=True)
    pulseRate = models.CharField(max_length=10, blank=True)
    pulseRhytm = models.CharField(max_length=10, blank=True)
    respRate = models.CharField(max_length=10, blank=True)
    bpSystolic = models.CharField(max_length=10, blank=True)
    bpDiastolic = models.CharField(max_length=10, blank=True)
    cholesterol = models.CharField(max_length=10, blank=True)
    hdl = models.CharField(max_length=10, blank=True)
    ldl = models.CharField(max_length=10, blank=True)
    bgRandom = models.CharField(max_length=10, blank=True)
    cxr = models.CharField(max_length=10, blank=True)
    ekg = models.CharField(max_length=10, blank=True)
    papSmear = models.CharField(max_length=10, blank=True)
    breastExam = models.CharField(max_length=10, blank=True)
    mammogram = models.CharField(max_length=10, blank=True)
    hemoccult = models.CharField(max_length=10, blank=True)
    fluVax = models.CharField(max_length=10, blank=True)
    pneumovax = models.CharField(max_length=10, blank=True)
    tdBooster = models.CharField(max_length=10, blank=True)
    footExam = models.CharField(max_length=10, blank=True)
    eyeExam = models.CharField(max_length=10, blank=True)

    mobile_number = models.CharField(max_length=11, null=True,blank=False, validators=[RegexValidator(r'^\d{10,11}$')])
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('Prefer not to say', 'Prefer not to say')
    )
    USER_TYPE = (
        ('Doctor', 'Doctor'),
        ('Patient', 'Patient'),
        ('Nurse', 'Nurse'),
        ('Client', 'Client')
    )
    STATUS = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Legally Seperated', 'Legally Seperated'),
        ('Widowed', 'Widowed')
    )
    WARD_CHOICES = (
        ('SH-102', 'SH-102'),
        ('SH-101', 'SH-101'),
        ('SH-201', 'SH-201'),
    )
    ward = models.CharField(max_length=10, choices=WARD_CHOICES, blank=True)
    maritalStatus = models.CharField(max_length=20, null=True, choices=STATUS, blank=True)
    userType = models.CharField(max_length=100, choices=USER_TYPE, blank=False)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=False)


    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
            return self.user.email

    def get_object():
        return get_object_or_404(UserProfile, user__username=self.kwargs['username'])

