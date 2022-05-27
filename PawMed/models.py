# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Doctor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    room = models.IntegerField()
    phone_number = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'doctor'


class DoctorSpecialization(models.Model):
    id = models.IntegerField(primary_key=True)
    doctorid = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='doctorid')
    specialization = models.ForeignKey('Specialization', models.DO_NOTHING, db_column='specialization')

    class Meta:
        managed = False
        db_table = 'doctor_specialization'


class Laboratory(models.Model):
    id = models.IntegerField(primary_key=True)
    room = models.IntegerField()
    type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'laboratory'


class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    registration_date = models.DateTimeField()
    age = models.IntegerField()
    phone_number = models.CharField(max_length=30)
    birth_date = models.DateTimeField()
    city = models.CharField(max_length=85)
    zip_code = models.IntegerField()
    gender = models.CharField(max_length=1)
    personid = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'patient'


class Prescription(models.Model):
    id = models.IntegerField(primary_key=True)
    visit = models.ForeignKey('Visit', models.DO_NOTHING, db_column='visit')
    date_of_issue = models.DateTimeField()
    expiration_date = models.DateTimeField()
    remarks = models.TextField()

    class Meta:
        managed = False
        db_table = 'prescription'


class Specialization(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'specialization'


class Technician(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'technician'


class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=50)
    execution_date = models.DateTimeField()
    executive = models.ForeignKey(Technician, models.DO_NOTHING, db_column='executive')
    remarks = models.TextField()
    laboratory_room = models.ForeignKey(Laboratory, models.DO_NOTHING, db_column='laboratory_room')
    visit = models.ForeignKey('Visit', models.DO_NOTHING, db_column='visit')

    class Meta:
        managed = False
        db_table = 'test'


class Visit(models.Model):
    id = models.IntegerField(primary_key=True)
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='doctor')
    patient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patient')
    date = models.DateTimeField()
    room = models.IntegerField()
    remarks = models.TextField()
    diagnosis = models.TextField()
    medical_interview = models.TextField()
    examination = models.TextField()
    recommendation = models.TextField()
    tookplace = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'visit'
