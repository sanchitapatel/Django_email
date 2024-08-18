from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.http import HttpResponse

def home(request):
    subject=" This_mail from Django Server",
    message="this is demo test for email",
    from_email="sanchita15pa@gmail.com",
    recipient_list=["himanshimate9@gmail.com"]
    send_mail=(subject,message,from_email,recipient_list)
    return HttpResponse("done success")
