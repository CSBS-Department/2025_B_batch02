from django.shortcuts import render,  get_object_or_404, redirect
from django.views import View
from django.http import HttpResponseRedirect

import os

from .forms import FileUploadForm,PasswordForm,KeyUploadForm,PasswordfileUploadForm, FilePathForm
from django.conf import settings

from django.views.generic import TemplateView

def alert_list(request):
    alerts = Alert.objects.all().order_by('-timestamp')
    return render(request, 'monitor/alert_list.html', {'alerts': alerts})

def alert_detail(request, alert_id):
    alert = get_object_or_404(Alert, pk=alert_id)
    return render(request, 'monitor/alert_detail.html', {'alert': alert})

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'monitor/index.html')
    
def Network(request):
    
    return render(request, 'monitor/network.html')
    
class File(View):
    def get(self, request, *args, **kwargs):
        form = FileUploadForm()
        return render(request, 'monitor/file.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            
            
            return render(request, 'monitor/result.html')
        return render(request, 'monitor/file.html', {'form': form})
    
class Firewall(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'monitor/firewall.html')
    
class Alert(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'monitor/alert.html')
    
class EncryptSuccessView(TemplateView):
    template_name = 'monitor/encryption_success.html'
class DecryptSuccessView(TemplateView):
    template_name = 'monitor/decryption_success.html'


    
class EncryptView(View):
    def get(self, request, *args, **kwargs):
        file_upload_form = FileUploadForm()
        password_form = PasswordForm()
        return render(request, 'monitor/encrypt.html')

    

class DecryptView(View):
    def get(self, request, *args, **kwargs):
        file_path_form = FilePathForm()
        password_form = PasswordForm()
        return render(request, 'monitor/encrypt.html')

    
     
class Ddos(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'monitor/ddos.html')

class User_profile(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'monitor/user-profile.html')
    
class User_privacy_setting(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'monitor/app/user-privacy-setting.html')
    
class Sign_in(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'monitor/auth/sign-in.html')
    
class Sign_up(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'monitor/auth/sign-up.html')
    
class Recoverpw(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'monitor/auth/recoverpw.html')
