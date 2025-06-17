from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import ApplicationModelForm
from .models import ApplicationModel


class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = ApplicationModel
    form_class = ApplicationModelForm
    template_name = "ApplicationCreate.html"
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    