from rest_framework import viewsets
from .models import Email
from django.shortcuts import get_object_or_404
from .serializers import EmailSerializer
from rest_framework.response import Response
class EmailViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    serializer_class = EmailSerializer
    queryset = Email
    def list(self, request):

        queryset = Email.objects.all()
        serializer = EmailSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Email.objects.all()
        email = get_object_or_404(queryset, pk=pk)
        serializer = EmailSerializer(email)
        return Response(serializer.data)