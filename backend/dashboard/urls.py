from django.conf.urls import url
from dashboard import views


urlpatterns = [
    url(r'^dashboard/raids/mine', views.raids_mine, name='raids_mine'),

    url(r'^dashboard/raids/edit/(?P<raid_id>\w+)', views.raids_edit, name='raids_edit'),
    url(r'^dashboard/raids/add', views.raids_add, name='raids_add'),
    url(r'^dashboard/', views.home, name='home'),
]
