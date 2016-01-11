from django.conf.urls import url
from cartograph import views


urlpatterns = [
    url(r'^api/v1/raids', views.raids, name='raid'),
]
