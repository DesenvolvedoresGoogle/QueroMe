# coding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from forms import FormUserRegistration

def register(request):
    if request.method == 'POST':
        form = FormUserRegistration(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = FormUserRegistration()
    return render(request, "registration/register.html", {
        'form': form,
        })