from django.views.generic import CreateView
from django.urls import reverse_lazy
from . import forms


# Create your views here.
class SingUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
