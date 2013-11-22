# coding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from forms import FormUserRegistration, WishlistForm
from django.contrib.auth.decorators import login_required
from filetransfers.api import prepare_upload
from django.core.urlresolvers import reverse

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

@login_required
def wish(request):
    view_url = reverse('wish')
    if request.method == 'POST':
        form = WishlistForm(request.POST, request.FILES)
        if form.is_valid():
            new_wish = form.save()
            new_wish.user = request.user
            new_wish.save()
            return HttpResponseRedirect("/")
    else:
        form = WishlistForm()

    upload_url, upload_data = prepare_upload(request, view_url)
    return render(request, "form.html", {
        'form': form,
        'upload_url': upload_url,
        'upload_data': upload_data,
        }
    )

def system_home(request):
    return render(request, "system/index.html",
        locals()
    )

def website_home(request):
    return render(request, "website/index.html",
        locals()
    )

def listar_desejos(request):
    return render(request, "system/list_desejos.html",
        locals()
    )