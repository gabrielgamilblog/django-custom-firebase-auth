from django.urls import path

from restapi.auth_views import AuthenticateView


urlpatterns = [
    path('authenticate/', AuthenticateView.as_view())

]
