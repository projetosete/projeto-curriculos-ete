# Generated by Django 4.0.3 on 2022-05-06 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import resumes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('phone_number', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=resumes.models.resume_image_name)),
                ('course', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100, null=True)),
                ('office', models.CharField(max_length=100, null=True)),
                ('start_date', models.DateField(null=True)),
                ('final_date', models.DateField(null=True)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resumes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resumes.resume')),
            ],
        ),
    ]
