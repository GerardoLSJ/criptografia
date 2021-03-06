from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from ac.serializers import UserSerializer, GroupSerializer
from .forms import CustomAuthenticationForm, SignForm
from .jwt import encode as signDocument, decode as verifyDocument
import time
import json

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# Class based views
class validateSignature(View):
    def get(self, request, *args, **kwargs):
        valid = verifyDocument(kwargs["str"].encode('utf-8'))
        return render(request, 'validar.html',{'valid':valid[0], 'payload':json.loads(valid[1].decode('utf-8'))})

class SignView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            initial = {
                "username": request.user.username,
                "fistName":request.user.first_name,
                "lastName": request.user.last_name,
                "serverLocation": "MX"
            }
            form = SignForm(initial=initial)
            return render(request, 'firmar.html', {'form': form})
        else:
            return HttpResponseRedirect('/login/')

    def post(self, request, *args, **kwargs):        
        form = SignForm(data=request.POST)
        if request.user.is_authenticated and form.is_valid():
            jwt_payload = {
                'file_name': form.cleaned_data['fileName'],
                'iat': int(time.time()),
                'first_name': form.cleaned_data['fistName'],
                'last_name': form.cleaned_data['lastName'],
                'username': form.cleaned_data['username'],
                'server_location': form.cleaned_data['serverLocation'],
            }
            e_signature = signDocument(jwt_payload)
            return render(request, 'nueva_firma.html', {'e_signature':e_signature})
            print('EFIRMA', e_signature)
        else:
            return HttpResponseRedirect('/login/')
        

class LoginView(View):
    initial = {'key': 'value'}
    template_name = 'login.html'

    # if a GET, we'll create a blank form
    def get(self, request, *args, **kwargs):
        form = CustomAuthenticationForm(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomAuthenticationForm(data=request.POST)
        print('Form {}'.format(form))
        
        if not form.is_valid():
            return render(request, self.template_name, {'form': form}) 
        
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        print('USER {}'.format(user))
        if user is not None:
            do_login(request, user)
            return HttpResponseRedirect('/firmar/')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        do_logout(request)
        return HttpResponseRedirect('/login/')