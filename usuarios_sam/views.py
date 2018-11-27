from django.shortcuts import render, redirect

from django.core.files.storage import FileSystemStorage

import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from usuarios_sam.models import CustomUser as User




from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from usuarios_sam.authhelper import get_consent_url , get_signin_url, get_token_from_code, get_access_token, get_token_from_shared_secret

import time
from usuarios_sam.outlookservice import get_me, get_my_messages, get_my_photo, get_users

from PIL import Image
from io import BytesIO

import os

def login_view_app(request):
    redirect_uri = request.build_absolute_uri(reverse('usuarios_sam:gettokenapp'))
    sign_in_url = get_consent_url(redirect_uri)


    return redirect(sign_in_url)


def login_view(request):
    request.session["redirect"] = request.GET.get("next","")
    redirect_uri = request.build_absolute_uri(reverse('usuarios_sam:gettoken'))
    sign_in_url = get_signin_url(redirect_uri)

    return redirect(sign_in_url)

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect (index)
        else:
            return render (request, "gentelella/production/login.html", {})
    else:
        return render (request, "gentelella/production/login.html", {})


def gettoken(request):
    auth_code = request.GET['code']
    redirect_uri = request.build_absolute_uri(reverse('usuarios_sam:gettoken'))
    token = get_token_from_code(auth_code, redirect_uri)
    access_token = token['access_token']
    refresh_token = token['refresh_token']
    expires_in = token['expires_in']

    user = get_me(access_token)

    first_name = user['givenName']
    name = user['displayName']
    last_name = name[len(first_name)+1:len(name)]

    # expires_in is in seconds
    # Get current timestamp (seconds since Unix Epoch) and
    # add expires_in to get expiration time
    # Subtract 5 minutes to allow for clock differences
    expiration = int(time.time()) + expires_in - 300

    # Save the token in the session
    request.session['access_token'] = access_token
    request.session['refresh_token'] = refresh_token
    request.session['token_expires'] = expiration
    request.session['user_email'] = user['mail']

    user_email = str(user["mail"])


    user = authenticate(email=user_email, token =access_token, first_name = first_name, last_name = last_name, name = name, request = request)
    if user is not None:
        login(request, user)
        return redirect(request.session["redirect"])
    else:
        return redirect(request.session["redirect"])



def gettokenapp(request):
    #redirect_uri = request.build_absolute_uri(reverse('usuarios_sam:gettokenapp'))
    token = get_token_from_shared_secret()
    access_token = token['access_token']
    #refresh_token = token['refresh_token']
    expires_in = token['expires_in']

    #user = get_me(access_token)

    #first_name = user['givenName']
    #name = user['displayName']
    #last_name = name[len(name)-len(first_name):len(name)]

    # expires_in is in seconds
    # Get current timestamp (seconds since Unix Epoch) and
    # add expires_in to get expiration time
    # Subtract 5 minutes to allow for clock differences
    expiration = int(time.time()) + expires_in - 300

    # Save the token in the session
    request.session['access_token'] = access_token
    #request.session['refresh_token'] = refresh_token
    request.session['token_expires'] = expiration

    #user_email = str(user["mail"])


    user = authenticate(email="rodrigo@montebelloacademy.org", token =access_token, first_name = None, last_name = None, name = None, request = request)
    if user is not None:
        login(request, user)
        return redirect("https://canaldocente.montebelloacademy.org/canales/")
    else:
        return redirect("https://canaldocente.montebelloacademy.org/canales/")
    #return HttpResponseRedirect(reverse('api:mail'))

     
def logout_view(request):
    logout(request)
    return redirect("https://login.windows.net/common/oauth2/logout?post_logout_redirect_uri={0}".format("https://192.99.20.125{0}".format(reverse('usuarios_sam:login'))))
    #return HttpResponseRedirect(reverse('usuarios_sam:login'))


@login_required(login_url="/user/login/")    
def index(request):
    if request.method == "POST" and request.FILES['photo']:
        photo = request.FILES["photo"]
        fs = FileSystemStorage()
        new_photo = fs.save("static/user/profile_photo/"+photo.name, photo)
        user = User.objects.get(pk = request.user.pk)
        user.user_photo = new_photo
        user.save()
        request.user = user
        return render(request, "custom/profile.html", {})
    else:
        return render(request, "custom/profile.html", {})


@login_required()    
def profile_view(request, usuario_id):
    user = User.objects.get(pk = usuario_id)
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        new_password_2 = request.POST.get("new_password_2")
        if new_password != new_password_2:
            return render (request, "gentelella/production/change_password.html", {"error":"Las contrasenas no son iguales"})
        else:
            user.set_password(new_password)
            user.save()
            login(request, user)
            return redirect("/user")
    else:
        return render (request, "usuarios_sam/perfil_usuario.html", {"usuario":user})
    
    
# Create your views here.
