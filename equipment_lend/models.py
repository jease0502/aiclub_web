from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    user_password = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_class = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=30)
    user_phone = models.CharField(max_length=10)


class LendRecord(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    equipment_id = models.CharField(max_length=20)
    lend_date = models.DateTimeField(auto_now_add=True)
    borrow_date = models.DateTimeField(auto_now=False)


class BelongingsImformation(models.Model):
    equipment_id = models.CharField(max_length=20, primary_key=True)
    property_number = models.CharField(max_length=20)
    serial_number = models.CharField(max_length=20)
    property_name = models.CharField(max_length=20)
    property_price = models.CharField(max_length=20)
    purchase_date = models.DateTimeField(auto_now=False)
    placement = models.CharField(max_length=20)
    property_status = models.CharField(max_length=20)
    company_id = models.CharField(max_length=20)


class Company_information(models.Model):
    company_id = models.CharField(max_length=20, primary_key=True)
    company_editor = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20)
    company_contact_name = models.CharField(max_length=20)
    company_contact_email = models.EmailField(max_length=30)
    company_phone = models.CharField(max_length=20)
