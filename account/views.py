from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RegisterUserSerializer


class RegisterUserView(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Vy uspeshno zaregalis", status=201)
