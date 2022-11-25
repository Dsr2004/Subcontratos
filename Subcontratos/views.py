from django.http import HttpResponse
from django.views.generic import View

class Index(View):
    def get(self, request, *aregs, **kwargs):
        return HttpResponse("Esta en el inicio")