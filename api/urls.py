from django.urls import include, path
from django.conf.urls import url
from . import views
urlpatterns = [
    # path('', include('rest_auth.urls')),
    # path('registration/', include('rest_auth.registration.urls')),
    path('welcome', views.welcome)
]
