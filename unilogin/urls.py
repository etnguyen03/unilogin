"""unilogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, reverse
from django.views.generic import RedirectView
from oauth2_provider.views import AuthorizationView, RevokeTokenView, TokenView

urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"", include("user_sessions.urls", "user_sessions")),
    url(
        r"^login/$",
        auth_views.LoginView.as_view(template_name="auth/login.html"),
        name="login",
    ),
    url(r"^logout/$", auth_views.LogoutView.as_view(), name="logout"),
    path("", RedirectView.as_view(pattern_name="profile:profile"), name="index"),
    path("profile/", include("unilogin.apps.profile.urls", namespace="profile")),
    path("api/", include("unilogin.apps.api.urls", namespace="api")),
    # Django OAuth Toolkit doesn't restrict admin views to staff,
    # so I have to specify relevant ones manually here.
    url(r"^oauth2/authorize/$", AuthorizationView.as_view(), name="authorize"),
    url(r"^oauth2/token/$", TokenView.as_view(), name="token"),
    url(r"^oauth2/revoke_token/$", RevokeTokenView.as_view(), name="revoke-token"),
]
