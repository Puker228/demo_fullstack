from django.shortcuts import render
from .models import Demo
from .serializers import DemoSerializer
from rest_framework import viewsets


def index(request):
    return render(request, 'index.html')


class DemoAPIView(viewsets.ModelViewSet):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer
    http_method_names = ['get', 'post']
