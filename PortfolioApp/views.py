from django.views.generic import TemplateView
from .models import Project,TechStack


class Index(TemplateView):
    template_name = 'PortfolioApp/index.html'

    def get_context_data(self):
        context = super(Index, self).get_context_data()
        context['projects'] = Project.objects.all().order_by("-created_at")
        context['langs'] = TechStack.objects.all().order_by("created_at")
        return context
