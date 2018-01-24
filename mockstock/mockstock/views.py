"""Views for base app."""


from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home page view."""

    template_name = 'mockstock/home.html'


class AboutView(TemplateView):
    """The about view."""

    template_name = "mockstock/about.html"
