from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, TemplateView

from . import models


class CallEndpoint(TemplateView):
    template_name = 'call/endpoint.xml'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        current = models.PhoneNumber.objects.get(current=True)
        context = {
            'number': current.number
        }
        return self.render_to_response(context)
