# from django.http import HttpResponse, JsonResponse
# from django.views.generic import View
# from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

# class Index(View):
#     def get(self, request, *aregs, **kwargs):
#         return render(request, "index.html")
    
    
# Auto Logout
class AutoLogout():
    def autoLogoutUser(request):
        logout(request)
        request.user = None
        messages.info(request, ".") # Nota: El argumento no puede estar vacío
        return HttpResponseRedirect('/Login')
    