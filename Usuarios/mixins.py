from django.shortcuts import redirect

class ValidateProfileUser(object):
    
    def dispatch(self, request, *args, **kwargs):
        id = kwargs['pk']
        if not id == request.user.pk:
            return redirect('miCuenta', pk = request.user.pk)
        

        return super().dispatch(request, *args, **kwargs)
    
