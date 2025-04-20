from modeltranslation.translator import register, TranslationOptions
from .models import Attachment

@register(Attachment)
class AttachmentTranslationOptions(TranslationOptions):
    fields = ('task', 'filename')


