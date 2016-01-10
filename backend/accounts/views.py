from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.views.generic.base import View
from accounts.forms import LoginForm


class LoginView(View):
	def get(self, request):
		context = {'form': LoginForm}
		return render(request, 'dashboard/utility/login.html', context)

	def post(self, request):
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.get_user()
			if not user:
				return redirect('login')
			login(request, user)
			return redirect('dashboard:home')
		else:
			context = {'form': form}
			return render(request, 'dashboard/utility/login.html', context)
login_view = LoginView.as_view()


class LogoutView(View):
	def get(self, request):
		logout(request)
		return render(request, 'dashboard/utility/logout.html')
logout_view = LogoutView.as_view()