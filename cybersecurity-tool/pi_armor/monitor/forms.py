# forms.py
from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField()

class FilePathForm(forms.Form):
    file_path = forms.CharField(label='File Path', max_length=100)

class KeyUploadForm(forms.Form):
    key = forms.FileField()

class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

class PasswordfileUploadForm(forms.Form):
    passwordfile = forms.FileField()