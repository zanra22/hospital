from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import RegexValidator

from .models import CustomUser
from django.contrib.auth.models import AbstractUser


class UniqueEmailForm:
    def clean_email(self):
        qs = CustomUser.objects.filter(email=self.cleaned_data['email'])
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.count():
            raise forms.ValidationError(
                'That email address is already in use')
        else:
            return self.cleaned_data['email']

    def clean_contact(self):
        qs = CustomUser.objects.filter(email=self.cleaned_data['contact'])
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.count():
            raise forms.ValidationError(
                'That contact is already in use')
        else:
            return self.cleaned_data['contact']

class CustomUserCreationForm(UniqueEmailForm, UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    mobile_number = forms.CharField(required=True, max_length=11, validators=[RegexValidator(r'^\d{10,11}$')],
                              widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 10px;',
                                                            'placeholder': 'Mobile Number'}))
    password1 = forms.CharField(label='Password' ,widget=forms.PasswordInput(attrs={'class': 'form-control',
                                            'style': 'height: 10px;', 'label': 'Test', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Re-type Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'height: 10px;', 'label': 'Test', 'placeholder': 'Re-type Password'}))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'mobile_number',
                  'password1',
                  'gender',
                  'userType',
                  'hospitalName'
                  )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 10px;', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 10px;', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 10px;', 'placeholder': 'Last Name'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 10px;', 'placeholder': 'Mobile Number'}),

            'userType': forms.Select(attrs={'class': 'form-control', 'style': 'height: 42px;', 'value': 'User'}),
            'hospitalName': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'height: 10px;', 'placeholder': 'Hospital Name'}),
        }

        def clean_email(self):
            email = self.cleaned_data.get('email')
            username = self.cleaned_data.get('username')


            if email and AbstractUser.objects.filter(email=email).exclude(username=username).exists():
                raise forms.ValidationError(u'Email addresses must be unique.')
            return email

class CustomUserChangeForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'style': 'height: 42px;',
                                                            'placeholder': 'Email'}))
    # profile_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'btn btn-success'}))
    class Meta:
        model = CustomUser
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'mobile_number',
                  'gender',
                  )
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'height: 42px;', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'height: 42px;', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'height: 42px;', 'placeholder': 'Last Name'}),
            'mobile_number': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'height: 42px;', 'placeholder': 'Mobile Number'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'style': 'height: 42px;', 'placeholder': 'Gender'}),
        }

# class ScriptForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ('file', )


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'label': 'Test', 'placeholder': 'Password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user