from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Email
from django.utils import timezone
from .forms import EmailForm
from django.http import JsonResponse
import re
from rest_framework import generics, viewsets


def search(request):
    if (
        request.method == "GET" and request.GET.get("search_box", None) != None
    ):  # they have done a search
        search_query = request.GET.get("search_box", None)
        latest_emails = Email.objects.filter(sent_to__icontains=search_query)
        return latest_emails
    return None


def read(request, email_id):
    specific_email = Email.objects.get(id=email_id)
    template = loader.get_template("email_app/emailViewer.html")
    context = {"specific_email": specific_email}
    return HttpResponse(template.render(context, request))


def email_home(request):
    latest_emails = Email.objects.filter()
    view_archived = request.GET.get("view_archived", False)
    if (view_archived == "on"):
        view_archived = True
    x = search(request)
    if x != None:
        latest_emails = x
    template = loader.get_template("email_app/emailHome.html")
    context = {"latest_emails": latest_emails, "view_archived": view_archived}
    return HttpResponse(template.render(context, request))


def email_sent(request):
    latest_emails = Email.objects.filter()
    view_archived = request.GET.get("view_archived", False)
    if (view_archived == "on"):
        view_archived = True

    x = search(request)
    if x != None:
        latest_emails = x
    template = loader.get_template("email_app/emailSent.html")
    if latest_emails != None:
        context = {"latest_emails": latest_emails, "view_archived": view_archived}
    return HttpResponse(template.render(context, request))

def archive(request, email_id):
    x = Email.objects.get(id=email_id)
    x.archived = 1
    x.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def editor(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = EmailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = Email()
            subject = request.POST.get("subject", "")
            body = request.POST.get("body", "")
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST.get("sent_to", "")]
            # make the email object for saving
            email.subject = subject
            email.body = body
            email.sent_to = recipient_list[0]
            email.send_date = timezone.now()
            email.sent_from = email_from
            email.save()
            possibleSpam = re.search("(?i)diet|nutrition|weight\s?loss|(burn|lose)\s(fat|pounds|weight)")
            print(email.id + " Was detected as spam for the following reason: Weight loss scam")
            possibleSpam = re.search("(?i)|credit|limit|inn app|prosses|congratulations|free samples|winner)")
            print(email.id + " Was detected as spam for the following reason: probably a bitcoin or credit card scam scam")
            # send_mail(subject, body, email_from, recipient_list) # this will actually send an email lol
            return redirect("/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmailForm()

    return render(request, "email_app/editor.html", {"form": form})


def ListEmailsView(request):
    return JsonResponse(request)
