from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.shortcuts import render
from .forms import FormRegistrazioneUser
from django.http import HttpResponseRedirect

# Create your views here.

def registrazione(request):
    if request.method == 'POST':
        form = FormRegistrazioneUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username = username, password = password, email = email)
            user = authenticate(username = username, password = password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = FormRegistrazioneUser()

    context = {'form': form}
    return render(request, 'registration/registrazione.html', context)