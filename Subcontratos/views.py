from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

class Index(View):
    def get(self, request, *aregs, **kwargs):
        return render(request, "index.html")