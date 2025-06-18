from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ApplicationForm


class ApplicationCreateView(CreateView):
    form_class = ApplicationForm
    template_name = "application_create.html"