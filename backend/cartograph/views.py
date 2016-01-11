from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse
from cartograph.models import Raid


class RaidsEndpoint(View):
    def get(self, request):
        raids = Raid.objects.all()
        locations = [{'state': r.state, 'zip_code': r.zip_code, 'city': r.city} for r in raids]
        return JsonResponse({'locations': locations})
raids = RaidsEndpoint.as_view()