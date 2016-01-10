from django.shortcuts import render
from common.views import ProtectedView


class HomeView(ProtectedView):
	def get(self, request):
		return render(request, 'dashboard/home.html')
home = HomeView.as_view()