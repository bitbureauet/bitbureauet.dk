from django.views.generic import TemplateView


class FrontPage(TemplateView):

    template_name = 'core/front_page.html'