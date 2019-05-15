from django.shortcuts import render

from django.core.mail import EmailMessage, send_mail
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .serializers import AnsSerializers
from rest_framework.views import APIView
from rest_framework import generics
from .models import Example
import time
from .task import send_verification_mail

class AnsView(generics.ListCreateAPIView):
    queryset = Example.objects.all()
    serializer_class = AnsSerializers
    def post(self, request, *args, **kwargs):
        serializer = AnsSerializers(data=request.data)
        if serializer.is_valid():
            ans = serializer.validated_data['ans']
            serializer.save()
            for i in range(101):
                sms = f'hello there {i}, {ans}'
                send_verification_mail.delay(sms)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)