from django.conf.urls import url, include
from rest_framework import routers
from rest_framework import response, schemas
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from core.views import StudentViewSet, UniversityViewSet



