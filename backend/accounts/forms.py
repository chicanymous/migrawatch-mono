from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
	email = forms.EmailField(
		label='Email',
        help_text='user',   # used for the icon, not as help text
		widget=forms.EmailInput(attrs={
			'class': 'gui-input',
			'placeholder': 'Email',
			'autofocus': True,
			'required': True,
			'type': 'email'
		}))
	password = forms.CharField(
		label='Password',
        help_text='lock',   # used for the icon, not as help text
		required=True,
		widget=forms.PasswordInput(attrs={
			'class': 'gui-input',
			'placeholder': 'Password',
			'autofocus': True,
		}))

	def clean_email(self):
		return self.cleaned_data['email'].strip().lower()

	def clean_password(self):
		return self.cleaned_data['password'].strip()

	def clean(self):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')

		queryset = User.objects.filter(email=email)
		if not queryset.exists():
			raise forms.ValidationError('This email is not registered.')

		user = queryset.first()
		if not user.check_password(password):
			raise forms.ValidationError('Cannot log in with these credentials.')
		return self.cleaned_data

	def get_user(self):
		email = self.cleaned_data['email']
		password = self.cleaned_data['password'].strip()
		return authenticate(email=email, password=password)
