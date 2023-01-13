from modeltranslation.translator import register, TranslationOptions
from .models import Project


@register(Project)
class ProjectsTransOptions(TranslationOptions):
    fields = ('desc',)