from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def index(request):

    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        fullname = request.POST.get('fullname')
        send_mail(subject, message, settings.EMAIL_HOST_USER,
                  ['recivermail@gmail.com'], fail_silently=False)
        return render(request, 'djangomail/email_sent.html', {'fullname': fullname})

    return render(request, 'djangomail/index.html', {})
