from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PersonModelForm
from .models import Person


def person(request):
    if request.method == "POST":
        form = PersonModelForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Person successfully added')
            except ValueError:
                messages.add_message(request, messages.ERROR, "Person wasn't created, check input data")
            return redirect('person:person')
    else:
        form = PersonModelForm()
    return render(request, 'person/person.html', context={"form": form})


def person_update(request, pk):
    item = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonModelForm(request.POST, instance=item)
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Person successfully updated')
            except ValueError:
                messages.add_message(request, messages.ERROR, "Person wasn't updated, check input data")
            return redirect('person:person-update', pk=pk)
    else:
        form = PersonModelForm(instance=item)
    return render(request, 'person/person.html', context={"form": form})
