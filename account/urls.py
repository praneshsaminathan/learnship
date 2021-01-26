from account.views import LoginView
from testproj.utils.apps import get_api_url
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter(trailing_slash=True)
# router.register(r'users', UserViewSet, 'api-users')

urlpatterns = [
    path(get_api_url(), include(router.urls)),

    path(get_api_url(url_name='login'), LoginView.as_view(), name="login"),

]

