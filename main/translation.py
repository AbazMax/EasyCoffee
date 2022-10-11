from modeltranslation.translator import register, TranslationOptions
from .models import Main, Home, About, Products, Contacts


@register(Main)
class MainTranslationOptions(TranslationOptions):
    fields = ('site_title', 'line_1', 'line_2' )


@register(Home)
class HomeTranslationOptions(TranslationOptions):
    fields = ('intro_message_1', 'intro_message_2')


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('about_text',)


@register(Products)
class ProductsTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Contacts)
class ContactsTranslationOptions(TranslationOptions):
    fields = ('title', 'address', 'tel')

