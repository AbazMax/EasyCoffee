# Generated by Django 4.1.1 on 2022-10-07 11:05

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_text', models.TextField(max_length=1000)),
                ('photo', models.ImageField(upload_to=main.models.About.get_file_name)),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('open_hours_sunday', models.CharField(max_length=100)),
                ('open_hours_monday', models.CharField(max_length=100)),
                ('open_hours_tuesday', models.CharField(max_length=100)),
                ('open_hours_wednesday', models.CharField(max_length=100)),
                ('open_hours_thursday', models.CharField(max_length=100)),
                ('open_hours_friday', models.CharField(max_length=100)),
                ('open_hours_saturday', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('tel', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro_message_1', models.TextField(max_length=500)),
                ('intro_message_2', models.TextField(max_length=500)),
                ('intro_photo', models.ImageField(upload_to=main.models.Home.get_file_name)),
            ],
            options={
                'verbose_name_plural': 'Home',
            },
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_1', models.CharField(db_index=True, max_length=200)),
                ('line2', models.CharField(db_index=True, max_length=200)),
                ('main_background', models.ImageField(upload_to=main.models.Main.get_file_name)),
            ],
            options={
                'verbose_name_plural': 'Main',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=300)),
                ('description', models.CharField(max_length=500)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.SmallIntegerField()),
                ('photo', models.ImageField(upload_to=main.models.Products.get_file_name)),
            ],
            options={
                'verbose_name_plural': 'Home',
                'ordering': ('position',),
            },
        ),
    ]
