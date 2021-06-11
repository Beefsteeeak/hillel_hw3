from django.db import models
from django.forms import ModelForm


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.first_name


class PersonModelForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
