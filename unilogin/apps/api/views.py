from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response

from unilogin.apps.api.serializers import UserSerializer


@api_view(["GET"])
@login_required
def get_current_user(request):
    return Response(UserSerializer(request.user).data)
