from modeltranslation.translator import register, TranslationOptions
from .models import Comment

@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('task', 'text')
