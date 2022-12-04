# from django.core import mail
# from django.core.mail import send_mail
# from django.core.mail.message import EmailMessage
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import get_template
# from django.template import Context
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

def enviarCorreo(asunto:str(), plantilla:str(), contexto:dict(), para:list()):
    template = get_template(plantilla)
    msg = template.render(contexto)
    email = EmailMultiAlternatives(
        subject = asunto,
        body=msg,
        from_email = settings.EMAIL_HOST_USER,
        to=para)
    email.attach_alternative(msg, "text/html")
    email.send(fail_silently=False)
    