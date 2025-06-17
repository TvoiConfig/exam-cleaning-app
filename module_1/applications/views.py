from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
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
    

class ApplicationListView(LoginRequiredMixin, ListView):
    model = ApplicationModel
    template_name = "ApplicationList.html"
    context_object_name = "applications"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
