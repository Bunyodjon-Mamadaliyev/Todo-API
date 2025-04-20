from modeltranslation.translator import register, TranslationOptions
from .models import SubTask

@register(SubTask)
class SubTaskTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
