from django.db import models
import uuid
import os
from ckeditor.fields import RichTextField
# Create your models here.


class Main(models.Model):

    def get_file_name(self, filename:str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('background/', new_filename)

    site_title = models.CharField(max_length=50)
    site_logo = models.ImageField(upload_to=get_file_name, help_text='Should be a small icon')
    line_1 = models.CharField(max_length=200, db_index=True)
    line_2 = models.CharField(max_length=200, db_index=True)
    main_background = models.ImageField(upload_to=get_file_name)

    class Meta:
        verbose_name_plural = 'Main'

    def __str__(self):
        return f'{self.__class__.__name__}'


class Home(models.Model):

    def get_file_name(self, filename:str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('Home/', new_filename)

    intro_message_1 = RichTextField(max_length=500)
    intro_message_2 = RichTextField(max_length=500)
    intro_photo = models.ImageField(upload_to=get_file_name)

    class Meta:
        verbose_name_plural = 'Home'

    def __str__(self):
        return f'{self.__class__.__name__}'


class About(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('About/', new_filename)

    about_text = RichTextField(max_length=1000)
    photo = models.ImageField(upload_to=get_file_name)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return f'{self.__class__.__name__}'


class Products(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('Products/', new_filename)

    name = RichTextField(max_length=300, db_index=True)
    description = RichTextField(max_length=500)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('position', )

    def __str__(self):
        return f'{self.name} position - {self.position}'


class Contacts(models.Model):
    title = RichTextField(max_length=300)
    open_hours_sunday = models.CharField(max_length=100)
    open_hours_monday = models.CharField(max_length=100)
    open_hours_tuesday = models.CharField(max_length=100)
    open_hours_wednesday = models.CharField(max_length=100)
    open_hours_thursday = models.CharField(max_length=100)
    open_hours_friday = models.CharField(max_length=100)
    open_hours_saturday = models.CharField(max_length=100)
    address = RichTextField(max_length=300)
    tel = RichTextField(max_length=200)

    class Meta:
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f'{self.__class__.__name__}'
