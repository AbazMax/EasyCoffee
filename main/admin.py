from django.contrib import admin
from .models import Main, Home, About, Products, Contacts
from modeltranslation.admin import TranslationAdmin


# Register your models here.
#admin.site.register(Main)
#admin.site.register(Home)
#admin.site.register(About)
#admin.site.register(Products)
#admin.site.register(Contacts)


@admin.register(Main)
class MainAdmin(TranslationAdmin):
    pass


@admin.register(Home)
class HomeAdmin(TranslationAdmin):
    pass

@admin.register(About)
class AboutAdmin(TranslationAdmin):
    pass


@admin.register(Products)
class ProductsAdmin(TranslationAdmin):
    pass


@admin.register(Contacts)
class ContactsAdmin(TranslationAdmin):
    pass