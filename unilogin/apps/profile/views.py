from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from ..users.models import User


@login_required
def profile_view(request):
    context = {
        "ALLOW_USERS_MODIFY_DETAILS": settings.ALLOW_USERS_MODIFY_DETAILS,
        "USER_DETAILS": {
            "First name": request.user.first_name,
            "Last name": request.user.last_name,
            "Email address": request.user.email,
            "Last login": request.user.last_login,
            "Date joined": request.user.date_joined,
        },
        "user_id": request.user.id,
    }
    return render(request, "profile.html", context=context)


def can_user_modify_self(user):
    return settings.USERS_MODIFY_FIELDS


class UpdateUserView(UpdateView):
    template_name = "auth/update.html"
    model = User
    fields = settings.USERS_MODIFY_FIELDS
    success_url = reverse_lazy("profile:profile")

    @method_decorator(login_required)
    @method_decorator(user_passes_test(can_user_modify_self))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
