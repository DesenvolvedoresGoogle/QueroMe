# coding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from forms import FormUserRegistration, WishlistForm
from django.contrib.auth.decorators import login_required
from filetransfers.api import prepare_upload
from django.core.urlresolvers import reverse
from django.contrib.auth import login as authlogin
from models import Wishlist
from django.shortcuts import get_object_or_404

def register(request):
    controler = "register"
    method = "user"
    if request.method == 'POST':
        form = FormUserRegistration(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.backend = 'django.contrib.auth.backends.ModelBackend'
            authlogin(request, new_user)
            return HttpResponseRedirect("/")
    else:
        form = FormUserRegistration()
    return render(request, "registration/register.html",
        locals()
    )

@login_required
def wish(request):
    controler = "wish"
    method = "new_wish"
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
    return render(request, "form.html",
        locals(),
    )

def system_home(request):
    controler = "system_home"
    method = "see"
    return render(request, "system/index.html",
        locals()
    )

def website_home(request):
    controler = "website_home"
    method = "see"
    return render(request, "website/index.html",
        locals()
    )

@login_required
def listar_desejos(request):
    controler = "wish"
    method = "listar_desejos"
    return render(request, "system/list_desejos.html",
        locals()
    )

@login_required
def show(request, wish_id):
    controler = "show"
    method = "see"
    wish = get_object_or_404(Wishlist,id=wish_id, user = request.user)
    return render(request, "system/show.html",
        locals()
    )