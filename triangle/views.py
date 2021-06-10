from django.shortcuts import render

from .forms import TriangleForm


def triangle(request):
    """
    Returns the hypotenuse having 2 legs
    """
    if request.method == "POST":
        form = TriangleForm(request.POST)
        if form.is_valid():
            leg_a = form.cleaned_data["leg_a"]
            leg_b = form.cleaned_data["leg_b"]
            hypotenuse = (leg_a ** 2 + leg_b ** 2) ** 0.5
            return render(request, "triangle/triangle.html", context={"hypotenuse": hypotenuse})
    else:
        form = TriangleForm()
    return render(request, "triangle/triangle.html", context={"form": form})
