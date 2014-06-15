from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core import models


class FrontPage(TemplateView):

    template_name = 'core/front_page.html'


class CallEndpoint(TemplateView):
    template_name = 'call/endpoint.xml'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        profile = models.Profile.objects.get(on_call=True)
        context = {
            'number': profile.phone_number
        }
        return self.render_to_response(context)
