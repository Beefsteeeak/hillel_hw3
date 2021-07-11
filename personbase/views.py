from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Person


class PersonCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'email']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('personbase:list')
    login_url = '/admin/'
    success_message = 'Person was created successfully'


class PersonUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'email']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('personbase:list')
    login_url = '/admin/'
    success_message = 'Person was updated successfully'


class PersonDeleteView(LoginRequiredMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('personbase:list')
    login_url = '/admin/'


class PersonDetailView(DetailView):
    model = Person


class PersonListView(ListView):
    model = Person
    paginate_by = 2
