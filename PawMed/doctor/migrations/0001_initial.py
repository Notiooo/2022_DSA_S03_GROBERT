# Generated by Django 4.0.3 on 2022-05-26 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('room', models.IntegerField()),
                ('phone_number', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'doctor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DoctorSpecialization',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'doctor_specialization',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('room', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'laboratory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('registration_date', models.DateTimeField()),
                ('age', models.IntegerField()),
                ('phone_number', models.CharField(max_length=30)),
                ('birth_date', models.DateTimeField()),
                ('city', models.CharField(max_length=85)),
                ('zip_code', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('personid', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_of_issue', models.DateTimeField()),
                ('expiration_date', models.DateTimeField()),
                ('remarks', models.TextField()),
            ],
            options={
                'db_table': 'prescription',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'specialization',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'technician',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('execution_date', models.DateTimeField()),
                ('remarks', models.TextField()),
            ],
            options={
                'db_table': 'test',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('room', models.IntegerField()),
                ('remarks', models.TextField()),
                ('diagnosis', models.TextField()),
                ('medical_interview', models.TextField()),
                ('examination', models.TextField()),
                ('recommendation', models.TextField()),
                ('tookplace', models.BooleanField()),
            ],
            options={
                'db_table': 'visit',
                'managed': False,
            },
        ),
    ]
