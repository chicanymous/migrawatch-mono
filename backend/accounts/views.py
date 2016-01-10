from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import logout
from django.views.generic.base import View


class LoginView(View):
	def get(self, request):
		return render_to_response('dashboard/utility/login.html')
login_view = LoginView.as_view()


class LogoutView(View):
	def get(self, request):
		logout(request)
		return render_to_response('dashboard/utility/logout.html')
logout_view = LogoutView.as_view()