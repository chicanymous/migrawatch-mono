from django.shortcuts import render, render_to_response
from common.views import ProtectedView


class HomeView(ProtectedView):
	def get(self, request):
		return render_to_response('dashboard/home.html')
home = HomeView.as_view()