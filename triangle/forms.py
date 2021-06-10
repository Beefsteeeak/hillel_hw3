from django import forms


class TriangleForm(forms.Form):
    leg_a = forms.IntegerField(required=True, min_value=1, max_value=1000)
    leg_b = forms.IntegerField(required=True, min_value=1, max_value=1000)
