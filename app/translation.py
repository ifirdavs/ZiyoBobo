from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Yangilik)
class YangiliklarTranslationOptions(TranslationOptions):
    fields = ('sarlavha', 'matn')               