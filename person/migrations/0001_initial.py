# Generated by Django 2.1.5 on 2019-01-26 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=60)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('father_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('person', models.CharField(choices=[('F', 'Found Person'), ('L', 'Lost Person')], default='Found Item', max_length=1)),
                ('age', models.CharField(max_length=50)),
                ('height', models.CharField(max_length=50)),
                ('body_color', models.CharField(max_length=50)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=16)),
                ('image', models.FileField(upload_to='')),
                ('identification_mark', models.TextField(help_text='Separate each item by comma')),
                ('secret_information', models.TextField(help_text='Separate each item by comma')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-update'],
            },
        ),
    ]
