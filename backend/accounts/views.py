from django.shortcuts import render, render_to_response
from django.views.generic.base import View


class LoginView(View):
	def get(self, request):
		return render_to_response('dashboard/utility/login.html')
login = LoginView.as_view()