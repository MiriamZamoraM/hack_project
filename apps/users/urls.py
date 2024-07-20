from django.urls import path
from users.views import LoginView
from users.views import RefreshTokenView
from users.views import RegistryView

urlpatterns = [
    path(route="registry/", view=RegistryView.as_view(), name="registry"),
    path(route="login/", view=LoginView.as_view(), name="login"),
    path(route="refreshToken/", view=RefreshTokenView.as_view(), name="refresh_token"),
]
