import os
from django.db import models

from src.users.models import User
from src.contacts.constants import(
    COMMON_CHOICES,
    DATE_CHOIECS,
    PHONE_CHOICES,
    RELATIONS,
)



class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    contact_image = models.URLField(null=True)
    first_name = models.CharField(verbose_name="Firstname", max_length=100)
    last_name = models.CharField(verbose_name="Lastname", max_length=100)
    sur_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(verbose_name="Email", max_length=100, null=True, blank=True)
    country_code = models.CharField(verbose_name="Country code", max_length=100, null=True, blank=True)
    phone_number = models.CharField(verbose_name="Phone", max_length=100, null=True, blank=True)
    mobile_number = models.CharField(verbose_name="Mobile phone", max_length=100, null=True, blank=True)
    is_favorite = models.BooleanField(default=False)
    owner= models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Company(models.Model):
    user = models.OneToOneField(Contact, on_delete=models.CASCADE, primary_key=True, unique=True)
    company_name = models.CharField(max_length=40, null=False)
    designation = models.CharField(max_length=30, null=True)

class MobileInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    email_type = models.CharField(max_length=10, choices=COMMON_CHOICES, default="W")
    address = models.TextField(max_length=150, null=True)
    address_type = models.CharField(max_length=10, choices=COMMON_CHOICES, default="W")
    contanct = models.ForeignKey(Contact, on_delete=models.CASCADE)


class DateInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    occasion = models.CharField(max_length=15, choices=DATE_CHOIECS)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

class Relationship(models.Model):
    relation = models.CharField(max_length=15, choices=RELATIONS)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Description(models.Model):
    id = models.BigAutoField(primary_key=True)
    picture = models.FilePathField(os.getcwd())
    description = models.TextField(max_length=100, null=True)
    file = models.FilePathField()
